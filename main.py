from dotenv import load_dotenv
import mqtt
import json

# load .env
load_dotenv()

mqtt_instance = mqtt.Mqtt('MqttLocalSiteP', 'local')

mqtt_connection = mqtt_instance.mqttConnection()

mqtt_instance.connectMqtt(mqtt_connection)
mqtt_instance.sendMqttMessage(mqtt_connection)