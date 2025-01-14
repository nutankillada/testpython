server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

##### Function for Retrieval:
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')
    # get value of key "server_name"(variable) and if not found return empty dict{}; and then again perform same operation to get value of the key i.e. on the previous output of server_config.get(server_name, {}); if found returns "status" and if not found, returns "Server not found"

##### Example Usage:
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")

server_name = 'server9'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")
