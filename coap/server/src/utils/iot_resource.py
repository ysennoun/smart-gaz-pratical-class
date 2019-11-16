from coapthon.resources.resource import Resource
from utils import iot_data
from utils.es_client import insert_to_es


class IoTResource(Resource):
    def __init__(self, name="IoTResource", coap_server=None):
        super(IoTResource, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "IoT Resource"

    def render_POST(self, request):
        print(request.payload)
        gaz_metrics = iot_data.get_gaz_metrics(request.payload)
        number_of_moles = iot_data.get_number_of_moles(gaz_metrics)
        document_to_insert = iot_data.get_document_to_insert(number_of_moles, gaz_metrics)
        insert_to_es(document_to_insert)
        print(document_to_insert)

        res = IoTResource()
        res.payload = "Data inserted"
        return res
