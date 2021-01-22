
from netmiko import ConnectHandler
from getpass import getpass
import re
from prettytable import PrettyTable
from interfaces import interfaces
from startup_config import startup_config
import os
import datetime
# prompt for authorization credentials
os.system('clear')
username = input("Username: ")
password = getpass("Password: ")
os.system('clear')
#menu
while True:
    menu = PrettyTable(['OPTION', 'CONFIG'])
    menu.add_row(["1", "Running Config - View and Print Log"])
    menu.add_row(["2", "Interfaces - View and Print Log(s)"])
    menu.add_row(["3", "Startup Config - View and Print Log"])    
    menu.add_row(["4", "Exit"])
    print(menu)
    choice = int(input("Please select an option: "))
    os.system('clear')

    # device = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt.cisco.com', port=8181, username=username, password=password)

    # Function to run if user selects #1 from main menu
    def running_config(username, password):
        run_config_device = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt.cisco.com', port=8181, username=username, password=password)
        run_config_output = run_config_device.send_command("show running-config")
        print(run_config_output)
        print()
        print('***************************************************************************')
        print('A COPY OF THIS RUNNING CONFIGURATION HAS BEEN LOGGED TO: runnin_config.txt')
        print('--------------------------------------------------------')
        print('***************************************************************************')
        print()
        # print this log to a text file and save locally
        runnin_config_file = open("runnin_config.txt", "a")
        now = datetime.datetime.now()
        runnin_config_file.write('\n' + '*********************************************************\n')
        timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
        runnin_config_file.write(timestamp + '\n')
        runnin_config_file.write('*********************************************************\n')
        runnin_config_file.write(run_config_output)
        runnin_config_file.close()
        
        run_config_device.disconnect()
        


    if choice == 1:
        running_config(username, password)

    if choice == 2:
        interfaces(username, password)

    if choice == 3:
        startup_config(username, password)
    
    if choice == 4:
        break










