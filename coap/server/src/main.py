import os
import time
from coapthon.server.coap import CoAP
from utils.iot_resource import IoTResource

COAP_PORT = int(os.environ.get("COAP_PORT", "5683"))
IOT_RESOURCE = os.environ["IOT_RESOURCE"]


class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource(IOT_RESOURCE, IoTResource()) #TODO add resource by specifying path and an instantiation of class resource (here IoTResource)


def main():
    server = CoAPServer("0.0.0.0", COAP_PORT) #TODO instantiate a CoAP server by specifying host="0.0.0.0" and port
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")


if __name__ == '__main__':
    time.sleep(30)
    main()