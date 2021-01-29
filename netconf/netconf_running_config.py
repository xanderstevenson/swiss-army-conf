
import os
import datetime
from ncclient import manager
import xml.dom.minidom

# this function will make a NETCONF request for the running config and convert the output to XML
def netconf_running_config(username, password):
 
    device = manager.connect(host='ios-xe-mgmt.cisco.com', port=10000, username=username, password=password, hostkey_verify=False, device_params={'name':"iosxe"})
    hostname_filter = '''
                    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                        </native>
                    </filter>
                    '''
    # Pretty print the XML reply to netconf_everything_config.txt
    xmlDom = xml.dom.minidom.parseString( str( device.get_config('running', hostname_filter)))
    netconf_cofig_file = open("logs/netconf_running_config.txt", "a")
    # get the date
    now = datetime.datetime.now()
    netconf_cofig_file.write('\n' + '---------------------------')
    netconf_cofig_file.write('\n' + 'RUNNIG CONFIG via NETCONF')
    timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
    netconf_cofig_file.write('\n' + timestamp)
    netconf_cofig_file.write('\n' + '---------------------------' + '\n') 
    netconf_cofig_file.write(xmlDom.toprettyxml( indent = "  " ))
    netconf_cofig_file.close()
    
    # Printing the pretty XML to the temrinal
    print('\n' + '---------------------------') 
    print('RUNNIG CONFIG via NETCONF')
    print('---------------------------') 
    timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
    print(timestamp)
    print('---------------------------') 
    print(xmlDom.toprettyxml( indent = "  " ))
    
    # freezes the view and prompts the user before continuing
    throwaway_input = input('Press Any Key to Continue')