import os
import time
from coapthon.client.helperclient import HelperClient
from utils import iot_data


COAP_HOST = os.environ["COAP_HOST"]
COAP_PORT = int(os.environ.get("COAP_PORT", "5683"))
IOT_RESOURCE = os.environ["IOT_RESOURCE"]
pressure = iot_data.MAX_PRESSURE
temperature = iot_data.TEMPERATURE
volume = iot_data.VOLUME

time.sleep(30)

while True:
    client = HelperClient(server=(COAP_HOST, COAP_PORT)) #TODO instantiate a CoAP client by specifying host and port
    data_as_hex = iot_data.get_data_as_hex(pressure, temperature, volume)
    response = client.post(path=IOT_RESOURCE, payload=data_as_hex, no_response=True) #TODO send data with post method by specifying path and payload (add option no_response=True)
    client.stop()
    time.sleep(10)
    pressure = iot_data.get_new_pressure(pressure)
