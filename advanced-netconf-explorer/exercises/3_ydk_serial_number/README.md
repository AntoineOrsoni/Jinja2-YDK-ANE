## Objectives
* Connect to the device, via NETCONF, using YDK,
* Getting the serial number of the device, for each component,
* Printing it nicely.

## Files that need to be edited

This is your mission, meaning that this EXERCISE will not be much guided. Feel free to implement to solution how you want it.

* `Dockerfile` is already complete. You do not need to edit it.
* `./my-app/run.py`
  * Import the right module from ydk.models.cisco_ios_xe
  * Get the serial number of each component of the device, and print them nicely.
    * Construct an instance of the NetconfServiceProvider class.
    * Set the right filter
    * Use the `CRUDService API`
    * Print the serial numbers nicely.
        * if the component does not have a SN, say it.

## Running the docker container

```shell script
docker build -t 3_ydk_serial_number .
docker run 3_ydk_serial_number
```
## Example of expected output

```config: 
Cisco CSR1000V Chassis has the SN : 92B76LAEGEU.
Cisco CSR1000V Route Processor has the SN : JAB1303001C.
Cisco CSR1000V Embedded Services Processor does not have a SN.
Physical Memory does not have a SN.
 Intel(R) Xeon(R) CPU E5-4669 v4 @ 2.20 does not have a SN.
```

# Documentation

## YDK Github repo

> https://github.com/CiscoDevNet/ydk-py

## YDK documentation

> http://ydk.cisco.com/py/docs/

### Getting started

> http://ydk.cisco.com/py/docs/guides/introduction.html



