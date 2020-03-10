from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xe import Cisco_IOS_XE_device_hardware_oper as xe_hardware
import device

ios_xe = device.xe_sandbox()
# create NETCONF provider
provider = NetconfServiceProvider(address=ios_xe.hostname,
                                  port=ios_xe.port,
                                  username=ios_xe.username,
                                  password=ios_xe.password,
                                  protocol=ios_xe.protocol)

# create CRUD service
crud = CRUDService()

hardware = xe_hardware.DeviceHardwareData.DeviceHardware()
hardware = crud.read(provider, hardware)

for hw_entry in range(hardware.device_inventory.__len__()):
    print("{desc} a pour SN : {sn}\n".format(desc=hardware.device_inventory[hw_entry].hw_description, sn=hardware.device_inventory[hw_entry].serial_number))

