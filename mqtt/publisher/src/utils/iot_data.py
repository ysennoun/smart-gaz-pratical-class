import random

MAX_PRESSURE = 200 # bars
TEMPERATURE = 20 # °C
VOLUME = 25 # L


def get_new_pressure(current_pressure: int) -> int:
    #TODO compute new pressure from a current pressure minus a number randomly chosen between 1 and 10
    #TODO if new pressure is below 1 return 1 as residue
	loss = random.randint(1, 10)
	if current_pressure > loss:
		return current_pressure - loss
	return 1 # residue


def get_data_as_hex(pressure: int, temperature: int, volume: int) -> str:
    #TODO get data as hexadecimal e.g: pressure:244bar -> f4 in hex, temperature: 25°C -> 19 in hex, volume: 50L -> 32 in hex => data_as_hex = 0xf41932
    hex_pressure = format(pressure, "x")
    hex_temperature = format(temperature, "x")
    hex_volume = format(volume, "x")
    data_as_hex = "0x" + str(hex_pressure) + str(hex_temperature) + str(hex_volume)
    return data_as_hex
