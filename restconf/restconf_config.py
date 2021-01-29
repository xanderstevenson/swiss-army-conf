import requests
import json
import datetime
# Suppress HTTPS warnings
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# the main function
def restconf_config(username, password):

    # Print a stream of bytes as pretty JSON
    def printBytesAsJSON(bytes):
        print(json.dumps(json.loads(bytes), indent=2))
    # the http rest call
    restconf_base_url = 'https://ios-xe-mgmt.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native'
    headers ={
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json",
            }
    url=restconf_base_url
    response = requests.request("GET", url, headers=headers, auth=(username, password), verify= False)
    
    
    # create/print the log
    restconf_cofig_file = open("logs/restconf_config.txt", "a")
    # get the date
    now = datetime.datetime.now()
    restconf_cofig_file.write('\n' + '---------------------------')
    restconf_cofig_file.write('\n' + 'RUNNIG CONFIG via RESTCONF')
    timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
    restconf_cofig_file.write('\n' + timestamp)
    restconf_cofig_file.write('\n' + '---------------------------' + '\n') 
    restconf_cofig_file.write(json.dumps(json.loads(response.text), indent=2))
    restconf_cofig_file.close()
    
    # print the log header
    print('\n' + '---------------------------') 
    print('RUNNIG CONFIG via RESTCONF')
    print('---------------------------') 
    print(timestamp)
    print('---------------------------') 
    # Pretty print our JSON response 
    printBytesAsJSON(response.text)

    # freezes the view and prompts the user before continuing
    throwaway_input = input('Press Any Key to Continue')