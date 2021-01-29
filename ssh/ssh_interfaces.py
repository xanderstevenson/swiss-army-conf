
from netmiko import ConnectHandler
from prettytable import PrettyTable
import os
import datetime

# function for displaying interfaces
def ssh_interfaces(username, password):
    # username and password defined in main.py
    device = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt.cisco.com', port=8181, username=username, password=password)
    # output = device.send_command("show interfaces brief")
    ip_int_br_output = device.send_command("show ip interface brief")
    interfaces_file = open("logs/ssh_interfaces.txt", "a")
    now = datetime.datetime.now()
    interfaces_file.write('\n' + '*********************************************************\n')
    timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
    interfaces_file.write(timestamp + '\n')
    interfaces_file.write('*********************************************************\n')
    interfaces_file.write(ip_int_br_output)
    interfaces_file.close()
    interface_list = []
    output_list = ip_int_br_output.split()
    # create a ist of interfaces
    for word in output_list:
        if 'GigabitEthernet' in word or 'Loopback' in word:
            interface_list.append(word) 
    # print list of interfaces
    def print_interfaces():
        print(ip_int_br_output)
        print() 
        print("INTERFACES")
        print("----------")    
        item_num = 1 
        for a_device in interface_list:
            print('___________________________')
            print(item_num, "  " + a_device)
            print('***************************')
            item_num += 1
        print()
        print('***************************************************************************')
        print('A COPY OF RESULTS FROM show ip interface brief HAS BEEN SAVED TO: interfaces.txt')
        print('--------------------------------------------------------')
        print('***************************************************************************')
        print()
                # prompt user to select interface
        choice_interface = int(input("Please select an interface: "))
        if choice_interface < 1 or choice_interface >= len(interface_list):
             choice_interface = int(input("Please select an interface: "))
        os.system('clear')
        interface_config = device.send_command(f"show ip interface {interface_list[choice_interface - 1]}")
        print('___________________________')
        print(f"{interface_list[choice_interface - 1]}")
        print('***************************')
        print(interface_config)
        print()
        false_wait =input("Press ENTER to continue or 'menu' + ENTER for main menu: ")
        os.system('clear')
        if false_wait == 'menu' or false_wait == 'Menu' or false_wait == "MENU":
            return
        print_interfaces()
    print_interfaces()
    # main_menu()
    # device.disconnect()
    
    