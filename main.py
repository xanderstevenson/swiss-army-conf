
# import stsndard and non-standard libraries
from netmiko import ConnectHandler
from getpass import getpass
from prettytable import PrettyTable
import os

# import other modules
from ssh.ssh_interfaces import ssh_interfaces
from ssh.ssh_startup_config import ssh_startup_config
from ssh.ssh_runnin_config import ssh_runnin_config
from restconf.restconf_config import restconf_config
from netconf.netconf_running_config import netconf_running_config


# prompt for authorization credentials
os.system('clear')
username = input("Username: ")
password = getpass("Password: ")
os.system('clear')

# main loop with logo and menu
while True:
    os.system('clear')
    print("""
 _____          _            ___                         _____              __  
/  ___|        (_)          / _ \                       /  __ \            / _| 
\ `-- __      ___ ___ ___  / /_\ \_ __ _ __ ___  _   _  | /  \/ ___  _ __ | |_  
 `--. \ \ /\ / / / __/ __| |  _  | '__| '_ ` _ \| | | | | |    / _ \| '_ \|  _| 
/\__/ /\ V  V /| \__ \__ \ | | | | |  | | | | | | |_| | | \__/\ (_) | | | | |   
\____/  \_/\_/ |_|___/___/ \_| |_/_|  |_| |_| |_|\__, |  \____/\___/|_| |_|_|   
                                                 __/ |                         
                                                |___/                          
            """)
    menu = PrettyTable(['OPTION', 'CONFIGURATION', 'PROTOCOL', 'OUTPUT'])
    menu.add_row(["1", "Running", "NETCONF", "XML"])
    menu.add_row(["-------", "----------------", "---------", "--------"])
    menu.add_row(["2", "Running", "RESTCONF", "JSON"]) 
    menu.add_row(["-------", "----------------", "---------", "--------"])
    menu.add_row(["3", "Running", "SSH", "Text"])
    menu.add_row(["4", "Interfaces", "SSH", "Text"])
    menu.add_row(["5", "Startup", "SSH", "Text"])    
    menu.add_row(["-------", "----------------", "---------", "--------"]) 
    menu.add_row(["6", "Exit", "", ""])
    print(menu)
    choice = int(input("Please select an option: "))
    os.system('clear')

    if choice == 1:
        netconf_running_config(username, password)
    
    elif choice == 2:
        restconf_config(username, password)
        
    elif choice == 3:
        ssh_runnin_config(username, password)

    elif choice == 4:
        ssh_interfaces(username, password)

    elif choice == 5:
        ssh_startup_config(username, password)
    
    elif choice == 6:
        break
    
    else:
        print("Please select an option from 1 to 4: ")
        











