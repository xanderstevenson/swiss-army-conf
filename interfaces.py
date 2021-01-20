
from netmiko import ConnectHandler
from prettytable import PrettyTable
import os
from main_menu import main_menu


# function for displaying interfaces
def interfaces(username, password):
    # username and password defined in main.py
    device = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt.cisco.com', port=8181, username=username, password=password)
    output = device.send_command("show interfaces")
    interface_list = []
    output_list = output.split()
    # create a ist of interfaces
    for word in output_list:
        if 'GigabitEthernet' in word:
            interface_list.append(word) 
    # print list of interfaces
    def print_interfaces():
        print("\n\n\n")
        print("INTERFACES")
        print("----------") 
        print()    
        item_num = 1 
        for a_device in interface_list:
            print('________________________')
            print(item_num, "  " + a_device)
            print('************************')
            print()
            item_num += 1
        # prompt user to select interface
        choice_interface = int(input("Please select an interface: "))
        os.system('clear')
        interface_config = device.send_command(f"show ip interface GigabitEthernet {choice_interface}")
        print('________________________')
        print(f"GigabitEthernet {choice_interface}")
        print('************************')
        print(interface_config)
        print()
        false_wait =input("Press any key to continue")
        os.system('clear')
        print_interfaces()
    print_interfaces()
    # main_menu()
    # device.disconnect()
    
    