# generador_datos.py
import numpy as np
import json
import requests
import time
import paho.mqtt.client as mqtt
from datetime import datetime


NODERED_URL = "http://localhost:1880/dUMA"
GRAFANA_URL = "" 
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "sensores"
MQTT_USERNAME = "usuario1"
MQTT_PASSWORD = "123"

def generar_datos():
    return {
        'te': int(np.random.normal(20, 2, 1)[0]),      # Temperatura °C
        'hr': int(np.random.normal(70, 2, 1)[0]),      # Humedad relativa %
        'pa': int(np.random.normal(900, 10, 1)[0]),    # Presión atmosférica hPa
        'p01': int(np.random.normal(20, 2, 1)[0]),     # MP 1.0 ug/m3
        'p25': int(np.random.normal(30, 2, 1)[0]),     # MP 2.5 ug/m3
        'p10': int(np.random.normal(30, 2, 1)[0]),     # MP 10 ug/m3
        'h03': int(np.random.normal(1000, 10, 1)[0]),  # Histograma MP 0.3 um
        'h05': int(np.random.normal(1000, 10, 1)[0]),  # Histograma MP 0.5 um
        'h01': int(np.random.normal(1000, 10, 1)[0]),  # Histograma MP 1.0 um
        'h25': int(np.random.normal(1000, 10, 1)[0]),  # Histograma MP 2.5 um
        'h50': int(np.random.normal(1000, 10, 1)[0]),  # Histograma MP 5.0 um
        'h10': int(np.random.normal(1000, 10, 1)[0]),  # Histograma MP 10 um
        'timestamp': datetime.now().isoformat()          # Timestamp
    }

def enviar_http_post_nodered(datos):
    """Envía datos a NodeRed via HTTP POST"""
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(NODERED_URL, json=datos, headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"✓ Datos enviados a NodeRed: {response.status_code}")
        else:
            print(f"✗ Error NodeRed: {response.status_code}")
    except Exception as e:
        print(f"✗ Error conectando a NodeRed: {e}")

def enviar_http_post_grafana(datos):
    """Envía datos a Grafana via HTTP POST"""
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(GRAFANA_URL, json=datos, headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"✓ Datos enviados a Grafana: {response.status_code}")
        else:
            print(f"✗ Error Grafana: {response.status_code}")
    except Exception as e:
        print(f"✗ Error conectando a Grafana: {e}")

def enviar_mqtt(datos):
    """Envía datos via MQTT"""
    try:
        client = mqtt.Client()
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.publish(MQTT_TOPIC, json.dumps(datos))
        client.disconnect()
        print("✓ Datos enviados via MQTT")
    except Exception as e:
        print(f"✗ Error MQTT: {e}")

def main():
    print("=== Generador de Datos Ambientales dUMA ===")
    print("Enviando datos cada 5 segundos...")
    print("Presiona Ctrl+C para detener")
    print()
    
    contador = 0
    try:
        while True:
            contador += 1
            datos = generar_datos()
            
            print(f"\n--- Envío #{contador} {datos['timestamp']} ---")
            print(f"Temperatura: {datos['te']:.1f}°C | Humedad: {datos['hr']:.1f}% | Presión: {datos['pa']:.1f}hPa")
            print(f"MP1.0: {datos['p01']:.1f} | MP2.5: {datos['p25']:.1f} | MP10: {datos['p10']:.1f} ug/m3")
            
            # Enviar por todos los métodos
            enviar_http_post_nodered(datos)
            # enviar_http_post_grafana(datos)  # Descomentar cuando Grafana esté configurado
            enviar_mqtt(datos)
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n\n¡Generador detenido!")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()