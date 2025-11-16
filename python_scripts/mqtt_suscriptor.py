# mqtt_suscriptor_nodered.py
import paho.mqtt.client as mqtt
import json
import requests
import time

# Configuración
BROKER = "localhost"
PORT = 1883
TOPIC = "sensores"
USERNAME = "usuario1"
PASSWORD = "123"
NODERED_URL = "http://localhost:1880/dUMA"

class MQTTToNodeRedBridge:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.username_pw_set(USERNAME, PASSWORD)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Suscriptor MQTT conectado al broker")
            client.subscribe(TOPIC)
            print(f"Suscrito al tópico: {TOPIC}")
        else:
            print(f"Error de conexión. Código: {rc}")
            
    def on_message(self, client, userdata, msg):
        try:
            datos_mqtt = json.loads(msg.payload.decode())
            print(f"📥 Mensaje MQTT recibido: {datos_mqtt['te']:.1f}°C, {datos_mqtt['hr']:.1f}%")
            self.reenviar_a_nodered(datos_mqtt)
            
        except Exception as e:
            print(f"Error procesando mensaje: {e}")
    
    def reenviar_a_nodered(self, datos):
        try:
            headers = {'Content-Type': 'application/json'}
            response = requests.post(
                NODERED_URL, 
                json=datos, 
                headers=headers, 
                timeout=5
            )
            
            if response.status_code == 200:
                print("Datos reenviados a NodeRed exitosamente")
            else:
                print(f"NodeRed respondió con código: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("❌ No se pudo conectar a NodeRed")
        except Exception as e:
            print(f"Error reenviando a NodeRed: {e}")
    
    def iniciar(self):
        try:
            print("Iniciando puente MQTT → NodeRed...")
            self.client.connect(BROKER, PORT, 60)
            self.client.loop_forever()
            
        except KeyboardInterrupt:
            print("\nPuente MQTT detenido")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.client.disconnect()

if __name__ == "__main__":
    bridge = MQTTToNodeRedBridge()
    bridge.iniciar()