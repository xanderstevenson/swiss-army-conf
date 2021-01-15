
from netmiko import ConnectHandler
from getpass import getpass
import re
from Gelatin.util import compile, generate
# prompt for authorization credentials
username = input("Username: ")
password = getpass("Password: ")


device = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt.cisco.com', port=8181, username=username, password=password)
# output = device.send_command("show version")
# print (output)
# device.send_command("config terminal")
# device.send_command("cdp enable")
# device.send_command("end")
output = device.send_command("show interfaces")
print(output)
# for interface in output:
#     print (interface)
#     print ('#########')

# for host in output:
#     print(host)
# text_file = open("output.txt", "w")
# text_file.write(output)
# text_file.close()
# print(generate("output.txt"))
device.disconnect()