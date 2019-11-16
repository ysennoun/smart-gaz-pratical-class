import os
import time
import paho.mqtt.client as mqtt
from utils import iot_data
from utils.es_client import insert_to_es


MQTT_HOST = os.environ["MQTT_HOST"]
MQTT_PORT = int(os.environ.get("MQTT_PORT", "1883"))
MQTT_TOPIC = os.environ["MQTT_TOPIC"]
KEEP_ALIVE = int(os.environ.get("KEEP_ALIVE", "60"))

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #TODO subscribe client to topic

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    decoded_message = iot_data.get_decoded_message(msg.payload)
    gaz_metrics = iot_data.get_gaz_metrics(decoded_message)
    number_of_moles = iot_data.get_number_of_moles(gaz_metrics)
    document_to_insert = iot_data.get_document_to_insert(number_of_moles, gaz_metrics)
    insert_to_es(document_to_insert)


time.sleep(30)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#TODO connect client by specifying host, port and keep alive

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
