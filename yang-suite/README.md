
## Yang-suite installation and use
### Installation
To ensure you have the latest release of the YANG Suite Docker container, download the docker-compose.yml and dockerfile files from the YANG Suite wiki and run this command from a terminal or PowerShell window:

```shell script
docker-compose up
docker-compose run yangsuite /setuser.sh
```

**Remember to save the login and password!!**

### Accessing the server

- Connect to http://localhost:8480.
- Default (administrator) login is the username and password you defined when running the setuser.sh script.