
# pip install influxdb-client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from generador_datos import generar_datos, mostrar_datos
import time

# Configuración de InfluxDB (ajusta estos valores a tu instalación)
token = "cA-Tsn4ki4F4OQ38zppwPrWHxh9aEkPU5_BxV9CWXPKQtAOyqzWv-lKfFLXcBceZXi_Lhez8h0Mp1SlVoo-nFQ=="
org = "Mi_organizacion"
bucket = "Interfaces"
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

def enviar_a_influxdb(datos):
	point = Point("sensores") \
		.field("te", datos["te"]) \
		.field("hr", datos["hr"]) \
		.field("pa", datos["pa"]) \
		.field("p01", datos["p01"]) \
		.field("p25", datos["p25"]) \
		.field("p10", datos["p10"]) \
		.field("h03", datos["h03"]) \
		.field("h05", datos["h05"]) \
		.field("h01", datos["h01"]) \
		.field("h25", datos["h25"]) \
		.field("h50", datos["h50"]) \
		.field("h10", datos["h10"]) \
		.time(datos["timestamp"], WritePrecision.NS)
	write_api.write(bucket=bucket, org=org, record=point)
	print("✅ Dato enviado a InfluxDB")

if __name__ == "__main__":
	print("Enviando datos a InfluxDB cada 5 segundos. Ctrl+C para detener.")
	try:
		while True:
			datos = generar_datos()
			mostrar_datos(datos)
			enviar_a_influxdb(datos)
			time.sleep(5)
	except KeyboardInterrupt:
		print("\n🛑 Envío detenido.")
