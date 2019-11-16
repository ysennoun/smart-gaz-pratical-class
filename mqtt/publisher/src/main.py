import os
import time
import paho.mqtt.client as mqtt
from utils import iot_data



MQTT_HOST = os.environ["MQTT_HOST"]
MQTT_PORT = int(os.environ.get("MQTT_PORT", "1883"))
MQTT_TOPIC = os.environ["MQTT_TOPIC"]
KEEP_ALIVE = int(os.environ.get("KEEP_ALIVE", "60"))
pressure = iot_data.MAX_PRESSURE
temperature = iot_data.TEMPERATURE
volume = iot_data.VOLUME

time.sleep(30)

while True:
	client = mqtt.Client()
	#TODO connect client by specifying host, port and keep alive
	data_as_hex = iot_data.get_data_as_hex(pressure, temperature, volume)
	res = client.publish(MQTT_TOPIC, data_as_hex)
	print(str(res))
	time.sleep(10)
	pressure = iot_data.get_new_pressure(pressure)