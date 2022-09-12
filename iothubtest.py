import json
import time
import datetime
import random
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
    try:
        timestamp = time.mktime(datetime.datetime.now().timetuple())
        #print(timestamp)
        temp1 = random.uniform(0.0, 35.0)
        temperature = float("{:.2f}".format(temp1))
        #print(temperature)
        hum1 = random.uniform(0.0, 35.0)
        humidity = float("{:.2f}".format(hum1))
        #print(humidity)

        sensor_data = {}
        sensor_data["timestamp"] = timestamp
        sensor_data['temperature'] = temperature
        sensor_data['humidity'] = humidity
        json_sensor_data = json.dumps(sensor_data)
        print(json_sensor_data)
        time.sleep(2)
        
        # send data to azure iot hub. 
        myClient.send_message(json_sensor_data)
    
    except KeyboardInterrupt:
        myClient.disconnect()
        print("Graceful Exit")
        break