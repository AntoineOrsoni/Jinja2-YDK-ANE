from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xe import Cisco_IOS_XE_interfaces_oper as xe_interface
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

interfaces_filter = xe_interface.Interfaces()
interfaces = crud.read(provider, interfaces_filter)

for int_entry in range(interfaces.interface.__len__()):
    print("{int} has @IP : {ip}".format(int=interfaces.interface[int_entry].name, ip=interfaces.interface[int_entry].ipv4))
