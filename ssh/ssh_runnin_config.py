import datetime
from netmiko import ConnectHandler
# Function to run if user selects #1 from main menu
def ssh_runnin_config(username, password):
    run_config_device = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt.cisco.com', port=8181, username=username, password=password)
    run_config_output = run_config_device.send_command("show running-config")
    print(run_config_output)
    print()
    print('***************************************************************************')
    print('A COPY OF THIS RUNNING CONFIGURATION HAS BEEN LOGGED TO: ssh_runnin_config.txt')
    print('--------------------------------------------------------')
    print('***************************************************************************')
    print()
    # print this log to a text file and save locally
    runnin_config_file = open("logs/ssh_runnin_config.txt", "a")
    now = datetime.datetime.now()
    runnin_config_file.write('\n' + '*********************************************************\n')
    timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
    runnin_config_file.write(timestamp + '\n')
    runnin_config_file.write('*********************************************************\n')
    runnin_config_file.write(run_config_output)
    runnin_config_file.close()
    
    false_wait =input("Press any key to continue: ")
    
    run_config_device.disconnect()