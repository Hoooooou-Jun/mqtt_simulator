from dotenv import load_dotenv
import os
from awscrt import io, mqtt
from awsiot import mqtt_connection_builder
from datetime import datetime, timedelta
import json

# load .env
load_dotenv()

# Set config
current_time = datetime.now() - timedelta(hours=9)
ENDPOINT = os.environ.get('MQTT_ENDPOINT')
CLIENT_ID = "MqttLocalSiteP"
PATH_TO_CERTIFICATE = "CA/e5952f1f1c3c48302499f008b27a278404691f1727eb3c0b4eacb500dec5cc76-certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "CA/e5952f1f1c3c48302499f008b27a278404691f1727eb3c0b4eacb500dec5cc76-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "CA/AmazonRootCA1.pem"

event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

# MQTT Connection
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=PATH_TO_CERTIFICATE,
    pri_key_filepath=PATH_TO_PRIVATE_KEY,
    client_bootstrap=client_bootstrap,
    ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
    client_id=CLIENT_ID,
    clean_session=False,
    keep_alive_secs=6
)
print("Connecting to {} with client ID '{}'...".format(ENDPOINT, CLIENT_ID))

connection_future = mqtt_connection.connect()
connection_future.result()
print("MQTT Connected")

# Set MQTT message
temId = "PA000009"
timestamp = current_time.strftime('%Y%m%d%H%M%S')
lng = 126.9786567
lat = 37.666826
shock = "3.3"
volt = "0.0"
compress = 0
onType = "S"
startYn = "Y"

message = '201,{"temId":"%s","dataTime":"%s","lng":%f,"lat":%f,"shock":%s,"volt":%s,"compress":%d,"onType":"%s","startYn":"%s"}' % (
    temId,
    timestamp,
    lng,
    lat,
    shock,
    volt,
    compress,
    onType,
    startYn
)

# Send MQTT Message
mqtt_connection.publish(topic="local", payload=message, qos=mqtt.QoS.AT_LEAST_ONCE)

print("**********Sended message**********")
print(message)
print("**********************************")

print("Success send MQTT message.")
