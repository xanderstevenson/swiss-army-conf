
from netmiko import ConnectHandler
from getpass import getpass
import re
from prettytable import PrettyTable
from interfaces import interfaces
from startup_config import startup_config
from runnin_config import runnin_config
from netconf_everything_config import netconf_everything_config
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
    menu.add_row(["4", "Everything Configuration - View and Print Log"])
    menu.add_row(["5", "Exit"])
    print(menu)
    choice = int(input("Please select an option: "))
    os.system('clear')
    # device = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt.cisco.com', port=8181, username=username, password=password)

    if choice == 1:
        runnin_config(username, password)

    elif choice == 2:
        interfaces(username, password)

    elif choice == 3:
        startup_config(username, password)
    
    elif choice == 4:
        netconf_everything_config(username, password)
    
    elif choice == 5:
        break
    
    else:
        print("Please select an option from 1 to 4: ")
        











