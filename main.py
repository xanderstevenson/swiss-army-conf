
from netmiko import ConnectHandler
from getpass import getpass

# prompt for authorization credentials
username = input("Username: ")
password = getpass("Password: ")


device = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt.cisco.com', port=8181, username=username, password=password)
output = device.send_command("show version")
print (output)
device.disconnect()