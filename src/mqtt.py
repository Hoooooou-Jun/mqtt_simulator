import os

from awscrt import io, mqtt
from awsiot import mqtt_connection_builder
from datetime import datetime, timedelta

class Mqtt:
    def __init__(self, client_id, topic):
        self.client_id = client_id
        self.topic = topic
        self.endpoint = os.environ.get('MQTT_ENDPOINT')
        self.path_to_certificate = "CA/e5952f1f1c3c48302499f008b27a278404691f1727eb3c0b4eacb500dec5cc76-certificate.pem.crt"
        self.path_to_private_key = "CA/e5952f1f1c3c48302499f008b27a278404691f1727eb3c0b4eacb500dec5cc76-private.pem.key"
        self.path_to_amazon_root_ca_1 = "CA/AmazonRootCA1.pem"
    def mqttConnection(self):
        event_loop_group = io.EventLoopGroup(1)
        host_resolver = io.DefaultHostResolver(event_loop_group)
        client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

        return mqtt_connection_builder.mtls_from_path(
            endpoint=self.endpoint,
            cert_filepath=self.path_to_certificate,
            pri_key_filepath=self.path_to_private_key,
            client_bootstrap=client_bootstrap,
            ca_filepath=self.path_to_amazon_root_ca_1,
            client_id=self.client_id,
            clean_session=False,
            keep_alive_secs=6
        )
    def connectMqtt(self, mqtt_connection):
        print("Connecting to {} with client ID '{}'...".format(self.endpoint, self.client_id))
        connection_instance = mqtt_connection.connect()
        connection_instance.result()
        return print("MQTT Connected")

    def sendMqttMessage(self, mqtt_connection, temId, lat, lng):
        # Set now datetime
        current_time = datetime.now() - timedelta(hours=9)

        # Set MQTT message
        temId = temId
        timestamp = current_time.strftime('%Y%m%d%H%M%S')
        lng = float(lng)
        lat = float(lat)
        shock = "0.0"
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
        print("Send to message...")
        # Send MQTT Message
        mqtt_connection.publish(topic=self.topic, payload=message, qos=mqtt.QoS.AT_LEAST_ONCE)
        print("Success send MQTT message.")
        print("**********Sended message**********")
        print(message)
        print("**********************************")
