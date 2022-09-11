# Azure-IOT
All notes and codes related to Azure cloud And MQTT Protocol

Install Mosquitto server:

⇒ sudo apt install -y mosquitto   
(To install mosquitto in ubuntu)

⇒ sudo systemctl start/stop/status mosquitto (To start stop , to know the status of the mosquitto server)

⇒ sudo apt install -y mosquitto.

Another Way to install mosquitto 

Add: following library in ubuntu :

sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa

sudo apt-get update

Then :

⇒ Snap install mosquitto


MQTT:

Publisher: Client that sends the messages

Subscriber: Client that receives the messages.

Command line notations

-t topic

-p port

-i id

-P password

-u user

-m message

-d debug

-f filename.

-h ip address
