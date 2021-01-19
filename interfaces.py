
from netmiko import ConnectHandler
from prettytable import PrettyTable

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
    choice = int(input("Please select an interface: "))

    device.disconnect()