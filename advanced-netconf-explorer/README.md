## Advanced Netconf Explorer

ANX is a NETCONF explorer, and a NETCONF client library. It's maintained in the repo below :

> https://github.com/cisco-ie/anx

### Installation

Clone the repo :

```shell script
git clone https://github.com/cisco-ie/anx
```

Use docker-compose to build and run the container :

```shell script
docker-compose up -d
```

More information about the installation in the ANX repo.

### Accessing the server

- Connect to `http://localhost:9269`.
- Use any equipment, such as the [DevNet Sandboxes](https://developer.cisco.com/site/sandbox/), or your own.

## Exercices

We will first use [ncclient](https://github.com/ncclient/ncclient) to get the information we need from the device.
We will then use [YDK](https://github.com/CiscoDevNet/ydk-py) to do the same ; and compare the two.