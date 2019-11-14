import random

MAX_PRESSURE = 200 # bars
TEMPERATURE = 20 # °C
VOLUME = 25 # L


def get_new_pressure(current_pressure: int) -> int:
	loss = random.randint(1, 10)
	if current_pressure > loss:
		return current_pressure - loss
	return 1 # residue


def get_data_as_hex(pressure: int, temperature: int, volume: int) -> str:
    hex_pressure = format(pressure, "x")
    hex_temperature = format(temperature, "x")
    hex_volume = format(volume, "x")
    data_as_hex = "0x" + str(hex_pressure) + str(hex_temperature) + str(hex_volume)
    return data_as_hex
