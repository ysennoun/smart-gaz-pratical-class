import re
from datetime import datetime
from dataclasses import dataclass, asdict

R = 8.3144621 # J K−1 mol−1

@dataclass
class GazMetrics:
    pressure_in_bar: float
    temperature_in_c: float
    volume_in_l: float
    timestamp: datetime


def get_decoded_message(payload: bytes) -> str:
	return str(payload.decode("utf-8"))


def get_gaz_metrics(raw_data: str) -> GazMetrics:
	data = raw_data.split("x")[1]
	hex_values = re.findall('.{1,2}', data)
	values = [int(hv, 16) for hv in hex_values]
	return GazMetrics(
		pressure_in_bar=values[0],
		temperature_in_c=values[1],
		volume_in_l=values[2],
		timestamp=datetime.now()
	)


def get_number_of_moles(gaz_metrics: GazMetrics) -> int:
	print("get_number_of_moles")
	print(gaz_metrics)

	pressure_in_pa = gaz_metrics.pressure_in_bar * 100000
	temperature_in_kelvin = gaz_metrics.temperature_in_c + 273.15
	volume_in_m3 = gaz_metrics.volume_in_l * 0.001
	print(pressure_in_pa)
	print(temperature_in_kelvin)
	print(volume_in_m3)
	num = int(( pressure_in_pa * volume_in_m3 ) / ( R * temperature_in_kelvin ))
	print(num)
	return num


def get_document_to_insert(number_of_moles: int, gaz_metrics: GazMetrics) -> dict:
	document = asdict(gaz_metrics)
	document["number_of_moles"] = number_of_moles
	return document



