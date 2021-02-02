# Swiss-Army-Conf
:floppy_disk:
This is my first attempt at creating a network automation demo for submission to [Cisco DevNet's Automation Exchange](https://developer.cisco.com/network-automation/)

### **About the LAB to run the demo:**
We will be interacting with an Always-On Sandbox instance of a Cisco Cloud Services Router - CSR1000v

**Sandbox URL:** https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology

**CSR1000V Host:** ios-xe-mgmt.cisco.com

**SSH Port:** 8181

**NETCONF Port:** 10000

**RESTCONF Ports:** 9443 (HTTPS)

**Credentials of this public available Sandbox to specify when prompted for it:**

**Username:** developer

**Password:** C1sco12345

**Dependencies:** See requirements.txt 

------------------------------------------

## Walk

1. Create and activate a virtual environment to conduct this lab in
2. Fork and clone the GitHub repository: 
git clone https://github.com/xanderstevenson/network-automation-demo.git
3. Install required dependencies:
- cd network-automation-demo
- pip install -r requirements.txt
4. Run the script
python main.py
5. You will be prompted to enter the credentials (username & password listed above)
6. Make a choice from the options in this menu: <br>

<img src="https://github.com/xanderstevenson/swiss-army-conf/blob/main/swiss-army-conf-menu.PNG">

For the main 5 choices, a copy of the relevant log will be automatically copied as backup to a text file in your local repo.

## Related Sandbox: 
[IOS XE on CSR Recommended Code Always On Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology)

## README.md
https://github.com/xanderstevenson/swiss-army-conf/blob/main/README.md 

**Acknowledgements**:
------------------------------------------

- For SSH, I used the [config_manager Use Case](https://developer.cisco.com/network-automation/detail/fba0ebc1-40c1-11eb-915c-36b321b824da/) in DevNet Automation Exchange by Cisco engineer Alex Manuelian, as a starting point. 

- For NETCONF, I used the [NC-get-config repo in GitHub](https://github.com/CiscoDevNet/python_code_samples_network/tree/master/NC-get-config), by Joe Clarke, as a reference.

- For the RESTCONF, I based my some of my module on an artile on UltraConfig.com.au by Matt Albrecht titled [RESTCONF Tutorial - Everything you need to know about RESTCONF in 2020](https://ultraconfig.com.au/blog/restconf-tutorial-everything-you-need-to-know-about-restconf-in-2020/). I also referenced [RC-get-config.py](https://github.com/CiscoDevNet/python_code_samples_network/blob/master/RC-get-config/RC-get-config.py), by Joe Clarke, which is found in the CiscoDevNet python_code_samples_network.

- I owe a major thank you to Tony Roman at DevNet, whose [Model Driven Network
Automation with IOS-XE LTRCRT-2700](https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2019/pdf/5eU6DfQV/LTRCRT-2700-LG.pdf) from Cisco Live 2019 saved me. I based a lot of my request calls on the paramenters and other nuances of using RESTCONF, NETCONF and SSH for network automation a a DevNEt Sandbox router:

If you read this entire README.md, then congratulations! Have a cookie: :cookie:
