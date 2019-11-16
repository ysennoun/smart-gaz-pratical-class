import unittest
from datetime import datetime
from utils import iot_data


class TestIoTData(unittest.TestCase):

    def test_get_gaz_metrics(self):
        # Given
        raw_data = "0xf41932"
        expected_gaz_metrics = iot_data.GazMetrics(
            pressure_in_bar=244,
            temperature_in_c=25,
            volume_in_l=50,
            timestamp=datetime.now()
        )

        # When
        gaz_metrics = iot_data.get_gaz_metrics(raw_data)
        
        # Then
        self.assertEqual(gaz_metrics.pressure_in_bar, expected_gaz_metrics.pressure_in_bar)
        self.assertEqual(gaz_metrics.temperature_in_c, expected_gaz_metrics.temperature_in_c)
        self.assertEqual(gaz_metrics.volume_in_l, expected_gaz_metrics.volume_in_l)

    def test_get_number_of_moles(self):
        # Given
        pressure_in_bar = 250
        temperature_in_c = 25
        volume_in_l = 50
        timestamp = datetime.now()
        gaz_metrics = iot_data.GazMetrics(pressure_in_bar, temperature_in_c, volume_in_l, timestamp)
        expected_number_of_moles = 504

        # When
        number_of_moles = iot_data.get_number_of_moles(gaz_metrics)

        # Then
        self.assertEqual(number_of_moles, expected_number_of_moles)

    def test_get_document_to_insert(self):
        # Given
        pressure_in_bar = 250
        temperature_in_c = 25
        volume_in_l = 500
        timestamp = datetime.now()
        gaz_metrics = iot_data.GazMetrics(pressure_in_bar, temperature_in_c, volume_in_l, timestamp)
        number_of_moles = 504
        expected_document = {
            "pressure_in_bar": pressure_in_bar,
            "temperature_in_c": temperature_in_c,
            "volume_in_l": volume_in_l,
            "timestamp": timestamp,
            "number_of_moles": number_of_moles
        }

        # When
        document_to_insert = iot_data.get_document_to_insert(number_of_moles, gaz_metrics)

        # Then
        self.assertEqual(document_to_insert, expected_document)