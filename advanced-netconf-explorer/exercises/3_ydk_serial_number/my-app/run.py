from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
# EXERCISE : import the right module
from ydk.models.cisco_ios_xe import EXERCISE
import device

ios_xe = device.xe_sandbox()

# EXERCISE : get the serial number of each component of the device, and print them nicely.
# If the component does not have a SN, say it.
