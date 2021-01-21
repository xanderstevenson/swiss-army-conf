from netmiko import ConnectHandler
from prettytable import PrettyTable
import os
import datetime

def port_open_all(username, password):
    device_port = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt.cisco.com', port=8181, username=username, password=password)
    port_output_list = device_port.send_command("show ip interface brief")
    port_list = []
    port_output_list = port_output_list.split()
    # create a ist of interfaces
    for word in port_output_list:
        if 'GigabitEthernet' in word or 'Loopback' in word:
            port_list.append(word) 
    device_port.send_command("conf t") 
    for port in port_list:
        device_port.send_command("after 5000")
        device_port.send_command(f"int {port}")
        device_port.send_command("after 5000")
        device_port.send_command("no shutdown")
        device_port.send_command("after 5000")
        device_port.send_command("exit")
        
        
    # device_port.send_command("exit")
    # show_ip_int_brief = device_port.send_command("show ip interface brief")
    # print(show_ip_int_brief)