from ncclient import manager
import yaml
import xml.dom.minidom

# EXERCISE : Getting the device information from the devices.yaml file
# Store this information in a variable (e.g : xe_sandbox)

# EXERCISE : Using ncclient to get the running-config of the device, as xml
# Replace the EXERCISE by the correct value of the xe_sandbox dictionnary.
with manager.connect(host=EXERCISE, port=EXERCISE,
                     username=EXERCISE, password=EXERCISE, hostkey_verify=False) as m:

    # Using the xml.dom.minidom library to pretty print the configuration
    config_xml = xml.dom.minidom.parseString(m.get_config(source="running").data_xml)
    print("Configuration =\n{conf}".format(conf=config_xml.toprettyxml()))
