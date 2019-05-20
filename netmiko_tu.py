from netmiko import ConnectHandler

devices = [{
    "device_type": "arista_eos",
    "ip": "192.168.239.201",
    "username": "admin",
    "password": "admin",
}, {
    "device_type": "arista_eos",
    "ip": "192.168.239.202",
    "username": "admin",
    "password": "admin",
}, {
    "device_type": "arista_eos",
    "ip": "192.168.239.203",
    "username": "admin",
    "password": "admin",
}, {
    "device_type": "arista_eos",
    "ip": "192.168.239.204",
    "username": "admin",
    "password": "admin",
}]

for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip int brief")
    net_connect.disconnect()
    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print (output)
    print ("---------------------------------------------------------------------------------\n")
