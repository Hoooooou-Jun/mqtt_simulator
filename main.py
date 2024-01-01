from dotenv import load_dotenv
import json
from src import mqtt
from src.random_coordinate import random_coordinate
from src.read_json import read_json

# load .env
load_dotenv()

# Return result coordinate
my_coordinates = (37.485882, 126.7529)
result = random_coordinate(my_coordinates[0], my_coordinates[1], 5, 10)
for coord in result:
    print(f"Latitude: {coord[0]}, Longitude: {coord[1]}")

# read json
data = read_json().items()
for key, value in data:
    print(key)
    for coord in value:
        print(coord)

# mqtt_instance = mqtt.Mqtt('MqttLocalSiteP', 'local')
#
# mqtt_connection = mqtt_instance.mqttConnection()
#
# mqtt_instance.connectMqtt(mqtt_connection)
# mqtt_instance.sendMqttMessage(mqtt_connection)
