
from netmiko import ConnectHandler
from getpass import getpass
import re
from prettytable import PrettyTable
import os
import datetime  
    
def ssh_startup_config(username, password):
    start_config_device = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt.cisco.com', port=8181, username=username, password=password)
    start_config_output = start_config_device.send_command("show startup-config")
    print(start_config_output)
    print()
    print('***************************************************************************')
    print('A COPY OF THIS STARTUP CONFIGURATION HAS BEEN LOGGED TO: ssh_startup_config.txt')
    print('--------------------------------------------------------')
    print('***************************************************************************')
    print()
    # print this log to a text file and save locally
    start_config_file = open("logs/ssh_startup_config.txt", "a")
    now = datetime.datetime.now()
    start_config_file.write('\n' + '*********************************************************\n')
    timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
    start_config_file.write(timestamp + '\n')
    start_config_file.write('*********************************************************\n')
    start_config_file.write(start_config_output)
    start_config_file.close()
    
    false_wait =input("Press any key to continue: ")
    
    start_config_device.disconnect()