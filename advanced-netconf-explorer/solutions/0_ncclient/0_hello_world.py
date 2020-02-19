from ncclient import manager
import yaml
import xml.dom.minidom

# Getting the device information from the .yaml file
with open("devices.yaml", 'r') as devices:
    xe_sandbox = yaml.safe_load(devices)["xe_sandbox"]

# Using ncclient to get the running-config of the device, as xml
with manager.connect(host=xe_sandbox["host"], port=xe_sandbox["port"],
                     username=xe_sandbox["username"], password=xe_sandbox["password"], hostkey_verify=False) as m:

    # Using the xml.dom.minidom library to pretty print the configuration
    config_xml = xml.dom.minidom.parseString(m.get_config(source="running").data_xml)
    print("Configuration =\n{conf}".format(conf=config_xml.toprettyxml()))
