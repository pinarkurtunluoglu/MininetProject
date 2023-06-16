import requests
import json
import time

controller_ip = "192.168.0.1" 

def calculate_intensity(pc_t, pc_t1):
    return pc_t1 - pc_t

def get_flow_stats(switch_id):
    url = f"http://{controller_ip}:8181/restconf/operational/opendaylight-flow-statistics:flow-statistics/flow-node-inventory:table/0/flow/{switch_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46YWRtaW4="
    }

    response = requests.get(url, headers=headers)
    flow_stats = response.json()
    packet_count_t = flow_stats["flow-statistics"]["packet-count"]
    time.sleep(1)
    response = requests.get(url, headers=headers)
    flow_stats = response.json()
    packet_count_t1 = flow_stats["flow-statistics"]["packet-count"]

    return packet_count_t, packet_count_t1

def find_shortest_path():
    url = f"http://{controller_ip}:8181/restconf/operational/opendaylight-inventory:nodes"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46YWRtaW4="
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    switches = data["nodes"]["node"]
    switch_intensities = {}

    for switch in switches:
        switch_id = switch["id"]
        packet_count_t, packet_count_t1 = get_flow_stats(switch_id)

        intensity = calculate_intensity(packet_count_t, packet_count_t1)
        switch_intensities[switch_id] = intensity

    shortest_path = min(switch_intensities, key=switch_intensities.get)
    return shortest_path

def embed_flow_rules(shortest_path):
    url = f"http://{controller_ip}:8181/restconf/config/opendaylight-inventory:nodes/node/{shortest_path}/table/0/flow/1"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46YWRtaW4="
    }
    data = {
        "flow-node-inventory:flow": [
            {
                "id": "1",
                "table_id": 0,
                "priority": 1,
                "match": {
                    "ethernet-match": {
                        "ethernet-type": {
                            "type": 2048
                        }
                    }
                },
                "instructions": {
                    "instruction": [
                        {
                            "order": 0,
                            "apply-actions": {
                                "action": {
                                    "output-action": {
                                        "output-node-connector": "2"
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }

    response = requests.put(url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print("Flow rules embedded successfully.")
    else:
        print("Failed to embed flow rules.")

shortest_path = find_shortest_path()
print("Shortest path:", shortest_path)
embed_flow_rules(shortest_path)
