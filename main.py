
from netmiko import ConnectHandler
from getpass import getpass
import re
from Gelatin.util import compile, generate
from prettytable import PrettyTable
from interfaces import interfaces

# prompt for authorization credentials
username = input("Username: ")
password = getpass("Password: ")

#menu
menu = PrettyTable(['OPTION', 'CONFIG'])
menu.add_row(["1", "NTP"])
menu.add_row(["2", "Interfaces"])
menu.add_row(["3", "LOGGING"])
print(menu)
choice = int(input("Please select an option: "))


# device = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt.cisco.com', port=8181, username=username, password=password)

if choice == 2:
    interfaces(username, password)








# text_file = open("output.txt", "w")
# text_file.write(output)
# text_file.close()

device.disconnect()