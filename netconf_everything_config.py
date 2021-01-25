import sys
from ncclient import manager
import xml.dom.minidom
from netmiko import ConnectHandler

def netconf_everything_config(username, password):


        # parser = ArgumentParser(description='Select options.')
        # # Input parameters
        # parser.add_argument('--host', type=str, required=True,
        #                     help="The device IP or DN")
        # parser.add_argument('-u', '--username', type=str, default='cisco',
        #                     help="Go on, guess!")
        # parser.add_argument('-p', '--password', type=str, default='cisco',
        #                     help="Yep, this one too! ;-)")
        # parser.add_argument('--port', type=int, default=830,
        #                     help="Specify this if you want a non-default port")
        # args = parser.parse_args()

    device = manager.connect(host='ios-xe-mgmt.cisco.com', port=10000, username=username, password=password, hostkey_verify=False, device_params={'name':"iosxe"})

    # m.send_command("conf t")
    # de_config = m.send_command("conf t")
    # print(de_config)
    hostname_filter = '''
                    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                        </native>
                    </filter>
                    '''

    # Pretty print the XML reply
    xmlDom = xml.dom.minidom.parseString( str( device.get_config('running', hostname_filter)))
    print(xmlDom.toprettyxml( indent = "  " ))