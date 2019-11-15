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

	# TODO Complete unit test
	def test_get_data_as_hexadecimal(self):
		# Given
		#TODO define variables pressure is 244 bar, temperature is 25 °C and volume is 50L and the expected result is "0xf41932"
		pressure = 244
		temperature = 25
		volume = 50
		expected_data_as_hexadecimal = "0xf41932"

		# When
		#TODO invoke function get_data_as_hex
		data_as_hexadecimal = iot_data.get_data_as_hex(pressure, temperature, volume)

		# Then
		#TODO verify that result of the function called is equal to the expected result
		self.assertEqual(expected_data_as_hexadecimal, data_as_hexadecimal)
		#self.assertEqual(True, False) # to be removed