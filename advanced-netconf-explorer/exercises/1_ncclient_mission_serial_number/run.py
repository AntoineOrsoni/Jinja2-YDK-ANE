from ncclient import manager
import yaml
import xml.dom.minidom
import lxml.etree as et
import xmltodict

# EXERCISE : use Advance Netconf Explorer to build your payload in order to get the serial-number.
payload = """
EXERCISE
"""

# Getting the device information from the .yaml file
with open("devices.yaml", 'r') as devices:
    xe_sandbox = yaml.safe_load(devices)["xe_sandbox"]

# Using ncclient to get the running-config of the device, as xml
with manager.connect(host=xe_sandbox["host"], port=xe_sandbox["port"],
                     username=xe_sandbox["username"], password=xe_sandbox["password"], hostkey_verify=False) as m:

    # EXERCISE : using `m`, get the response from the device
    # Don't forget to send the payload as well.


    # EXERCISE : Print the output.
    # You  can use the xml.dom.minidom.parseString(string) method to convert it to XML.
    # It returns a <class 'xml.dom.minidom.Document'>
    # You can then use the method .toprettyxml() on a <class 'xml.dom.minidom.Document'> to pretty print the XML output.




    # Just getting what we need
    # First, converting the xml as a dict
    response_dict = xmltodict.parse(response_xml.toxml())["data"]["device-hardware-data"]["device-hardware"]["device-inventory"]

    # Printing each hw_type with its serial_number
    for element in range(response_dict.__len__()):
        for key, value in response_dict[element].items():
            if key == "hw-type":
                hw_type = value
            if key == "serial-number":
                serial_number = value
        print("{hw} has SN : {sn}".format(hw=hw_type, sn=serial_number))
