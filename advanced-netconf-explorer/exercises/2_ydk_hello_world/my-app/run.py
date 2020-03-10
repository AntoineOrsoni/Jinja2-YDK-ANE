from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xe import Cisco_IOS_XE_interfaces_oper as xe_interface
import device

ios_xe = device.xe_sandbox()
# EXERCISE : Construct an instance of the NetconfServiceProvider class.
# Use the YDK documentation on NETCONF Service Provider to understand which parameters you need to pass.
# Parameters are stored in the `device` class (which is imported line 4).
provider = NetconfServiceProvider(EXERCISE)

# create CRUD service
crud = CRUDService()

# EXERCISE : Set the right filter, using Advanced Netconf Explorer, using the right attribute(s) of the imported
# `Cisco_IOS_XE_interfaces_oper` module
interfaces_filter = EXERCISE

# EXERCISE : Use the `CRUDService API` to get (READ) the operational state of the interfaces of the device.
# Store the object in a new variable `interfaces`
interfaces = EXERCISE

# EXERCISE : now that you have an object, containing the interfaces operational state, get each interface name, and each interface IP.
