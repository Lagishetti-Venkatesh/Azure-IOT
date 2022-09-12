
#importing the library from iot hu 
from azure.iot.device import IoTHubDeviceClient

#1. declare iot hub device client instance
device_connection_string = "Primary_string_should_be_placed"
myClient = IoTHubDeviceClient.create_from_connection_string(device_connection_string)

#start iothub device client
myClient.connect()

def message_handler(message):
    print("Received Message from Cloud")
    print(message.data)

myClient.on_message_received = message_handler

while True:
    print("Waiting for message from cloud")
    time.sleep(1)
    