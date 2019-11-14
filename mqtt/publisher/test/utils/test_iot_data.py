import unittest
from utils import iot_data


class TestIoTData(unittest.TestCase):

	def test_get_new_pressure_greater_than_loss(self):
		# Given
		pressure = 120

		# When
		new_pressure = iot_data.get_new_pressure(pressure)

		# Then
		self.assertGreaterEqual(10, pressure - new_pressure)
		self.assertGreaterEqual(pressure - new_pressure, 1)

	def test_get_new_pressure_lower_than_loss(self):
		# Given
		current_pressure = 0

		# When
		new_pressure = iot_data.get_new_pressure(current_pressure)

		# Then
		self.assertEqual(new_pressure, 1)

	def test_get_data_as_hexadecimal(self):
		# Given
		pressure = 244
		temperature = 25
		volume = 50
		expected_data_as_hexadecimal = "0xf41932"

		# When
		data_as_hexadecimal = iot_data.get_data_as_hex(244, 25, 50)

		# Then
		self.assertEqual(expected_data_as_hexadecimal, data_as_hexadecimal)