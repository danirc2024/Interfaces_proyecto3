# mqtt_publicador_mejorado.py
import paho.mqtt.client as mqtt
import json
import numpy as np
import time
import sys

broker = "localhost"
port = 1883
topic = "sensores"
username = "usuario1"
password = "123"

def generar_datos():
    return {
        'te': int(np.random.normal(20, 2, 1)[0]),
        'hr': int(np.random.normal(70, 2, 1)[0]),
        'pa': int(np.random.normal(900, 10, 1)[0]),
        'p01': int(np.random.normal(20, 2, 1)[0]),
        'p25': int(np.random.normal(30, 2, 1)[0]),
        'p10': int(np.random.normal(30, 2, 1)[0]),
        'h03': int(np.random.normal(1000, 10, 1)[0]),
        'h05': int(np.random.normal(1000, 10, 1)[0]),
        'h01': int(np.random.normal(1000, 10, 1)[0]),
        'h25': int(np.random.normal(1000, 10, 1)[0]),
        'h50': int(np.random.normal(1000, 10, 1)[0]),
        'h10': int(np.random.normal(1000, 10, 1)[0]),
        'timestamp': time.time()
    }

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado exitosamente al broker MQTT")
    else:
        print(f"Error de conexión. Código: {rc}")
        sys.exit(1)

def on_publish(client, userdata, mid):
    print(f"Mensaje publicado (ID: {mid})")

client = mqtt.Client()
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_publish = on_publish

try:
    print("Conectando al broker...")
    client.connect(broker, port, 60)
    client.loop_start()
    
    contador = 0
    while True:
        contador += 1
        datos = generar_datos()
        
        # ppublicar mensaje
        result = client.publish(topic, json.dumps(datos))
        
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"Envío #{contador} - Temp: {datos['te']:.1f}°C | Hum: {datos['hr']:.1f}%")
        else:
            print(f"Error publicando mensaje: {result.rc}")
        
        time.sleep(5)
        
except KeyboardInterrupt:
    print("\nPublicador detenido")
except Exception as e:
    print(f"Error: {e}")
finally:
    client.loop_stop()
    client.disconnect()