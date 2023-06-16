import requests

controller_ip = '192.168.0.1'  
controller_port = 8080  

switches = ['s1', 's2', 's3']

for switch in switches:
    url = f'http://{controller_ip}:{controller_port}/api/switches/{switch}/rules'

    rule = {
        'priority': 10,
        'match': {
            'eth_type': '0x0800',  
            'ip_proto': '6',  
            'tcp_dst': '80'  
        },
        'actions': [
            {
                'type': 'OUTPUT',
                'port': 'CONTROLLER'  
            }
        ]
    }

    try:
        response = requests.post(url, json=rule)
        if response.status_code == 201:
            print(f'OpenFlow rule successfully installed on {switch}')
        else:
            print(f'Failed to install OpenFlow rule on {switch}. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error occurred while sending the request to {url}: {e}')
