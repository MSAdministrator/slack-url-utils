# slack-url-utils

> slack-url-utils is a slash command utility that obfuscates or deobfuscates a URL

This utility spawned out of necessity to assist with sharing of malicious URLs in Slack.  Slack will automatically render or make a HTTP request when a URl is entered.  To assist myself and other security teams, I created this slash command application that will obfuscate and deobfuscate provided URLs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

In order order to use this application, you will need:

* A system/server to run the Flask application itself (preferably a Ubuntu Server)
    * A $5 a month DigitalOcean box works great
* Have access to create/implement a slash command in Slack

### Prerequisites

What things you need to install the software and how to install them

#### Python Requirements on Ubuntu

If you use Ubuntu Server, you will need to make sure that it is up to date and you will need to install some dependencies

```
# Update Ubuntu
apt-get update

# Install Python3, pip3, setuptools and other dependencies
sudo apt-get install python3-pip python-setuptools python-dev build-essential
```

### Installing

Using `scp` to copy the repository from your local machine to the remote Ubuntu server

```
# First create a folder or use an existing one on the ubuntu server
mkdir /usr/user/utils

# Use scp to copy local folder to remote folder
scp -r /Users/{user}/slack-url-utils root@{server_ip_address}:/usr/user/utils
```

Next, create a file for `gunicorn` to manage and run the app in the event of failure or reboots

```
# mkdir if not exists
mkdir /etc/init

# create configuration file for gunicorn
nano /etc/init/slack-url-utils.conf
```

Now, add the following to this file you just created:

```
description "Gunicorn application server running slack-url-utils"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
```

Now, we will install our application from the folder directory you copied to the Ubuntu server

```bash
python3 setup.py install
```

To run our application we do the following:


```bash
# Bind to whichever port you want, default below is 8000

gunicorn --bind 0.0.0.0:8000 wsgi
```

## Deployment to Slack

To add the slash command, follow these instructions:

* Go to https://[yourTeam].slack.com/apps/build/custom-integration
* Enter `/obfuscate` to add your new Slack slash command
* Enter the command of '/obfuscate` 
* Enter the URL of the your ubuntu server with the port and the endpoint you want
    * There are two endpoints curently:
        * `/obfuscate` and `/deobfuscate`
    * Example: `http://5.5.5.5:8000/obfuscate`
    * Example: `http://5.5.5.5:8000/deobfuscate`
* Make sure the method is POST
* Add any descriptions or context that is needed
* Click save!
* Test it out in slack

See this [link](https://www.hongkiat.com/blog/custom-slash-command-slack/) for more information.

## Built With

* [carcass](https://github.com/MSAdministrator/carcass) - Python packaging template

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. 

## Authors

* Josh Rickard - *Initial work* - [MSAdministrator}](https://github.com/MSAdministrator)

See also the list of [contributors](https://github.com/MSAdministrator/slack-url-utils/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details