from ncclient import manager
import yaml
import xml.dom.minidom
import lxml.etree as et
import xmltodict

payload = """
  <filter>
    <device-hardware-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-device-hardware-oper">
      <device-hardware>
        <device-inventory>
          <serial-number/>
          <hw-type/>
          <hw-dev-index/>
        </device-inventory>
      </device-hardware>
    </device-hardware-data>
  </filter>
"""

# Getting the device information from the .yaml file
with open("devices.yaml", 'r') as devices:
    xe_sandbox = yaml.safe_load(devices)["xe_sandbox"]

# Using ncclient to get the running-config of the device, as xml
with manager.connect(host=xe_sandbox["host"], port=xe_sandbox["port"],
                     username=xe_sandbox["username"], password=xe_sandbox["password"], hostkey_verify=False) as m:

    # getting the response. Converting to xml using the .data_xml attribute.
    # Using the xml.dom.minidom library to pretty print the configuration
    response_xml = xml.dom.minidom.parseString(m.get(payload).data_xml)

    # Showing the full xml output
    print("Response =\n{response}".format(response=response_xml.toprettyxml()))

    # print(type(m.get(payload))) => returns a <class 'ncclient.operations.retrieve.GetReply'>
    # print(type(m.get(payload).data_xml)) => returns a <class 'str'>
    # print(type(response_xml)) => returns <class 'xml.dom.minidom.Document'>

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
