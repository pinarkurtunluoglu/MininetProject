from opendaylight import ODLClient

def get_forwarding_services():
    client = ODLClient('controller_ip', 'controller_port')
    services = client.get_forwarding_services()
    return services

forwarding_services = get_forwarding_services()
print(forwarding_services)
