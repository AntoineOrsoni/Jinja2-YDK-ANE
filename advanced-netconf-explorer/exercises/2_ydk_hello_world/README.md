## Objectives
* Connec to the device, via NETCONF, using YDK,
* Getting the list of interfaces of a device,
* Printing it nicely.

## Files that need to be edited

* `Dockerfile` is already complete. You do not need to edit it.
* `./my-app/run.py`
    * Construct an instance of the NetconfServiceProvider class.
        * Use the YDK documentation on NETCONF Service Provider to understand which parameters you need to pass.
        * Parameters are stored in the `device` class (which is imported line 4).
        * Documentation : http://ydk.cisco.com/py/docs/api/providers/netconf_provider.html
    * Create a variable, `interfaces_filter`, which contains the filter to get the interfaces operational state, using the attribute(s) of the imported `Cisco_IOS_XE_interfaces_oper` module.
        * Use Advanced NETCONF Explorer to help you. 
    * Use the `CRUDService API` to get (READ) the operational state of the interfaces of the device. Store the output it in a variable.
        * Documentation : http://ydk.cisco.com/py/docs/api/services/crud_service.html
    * Now that you have an object, containing the interfaces operational state, get each interface name, and each interface IP.
    
## Running the docker container

```shell script
docker build -t 2_ydk_hello_world .
docker run 2_ydk_hello_world 
```
## Example of expected output

```config
GigabitEthernet1 has @IP : 10.10.20.48
GigabitEthernet2 has @IP : None
GigabitEthernet3 has @IP : None
Loopback0 has @IP : 1.1.1.1
Control Plane has @IP : None
```

# Documentation

## YDK Github repo

> https://github.com/CiscoDevNet/ydk-py

## YDK documentation

> http://ydk.cisco.com/py/docs/

### Getting started

> http://ydk.cisco.com/py/docs/guides/introduction.html



