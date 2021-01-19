
from netmiko import ConnectHandler


def interfaces(username, password):
    device = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt.cisco.com', port=8181, username=username, password=password)
    output = device.send_command("show interfaces")
    interface_list = []
    output_list = output.split()
    for word in output_list:
        if 'GigabitEthernet' in word:
            interface_list.append(word)      
    print(interface_list)
    device.disconnect()