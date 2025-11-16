# mqtt_publicador.py
import paho.mqtt.client as mqtt
import json
import time
import sys
from generador_datos import generar_datos, mostrar_datos

# Configuración MQTT
broker = "localhost"
port = 1883
topic = "sensores"
username = "usuario1"
password = "123"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado exitosamente al broker MQTT")
    else:
        print(f"❌ Error de conexión. Código: {rc}")
        sys.exit(1)

def on_publish(client, userdata, mid):
    print(f"📤 Mensaje publicado (ID: {mid})")

def main():
    client = mqtt.Client()
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_publish = on_publish

    try:
        print("🔌 Conectando al broker MQTT...")
        client.connect(broker, port, 60)
        client.loop_start()
        
        contador = 0
        print("🚀 Iniciando envío de datos MQTT...")
        print("Presiona Ctrl+C para detener\n")
        
        while True:
            contador += 1
            datos = generar_datos()
            
            print(f"\n--- Envío MQTT #{contador} ---")
            mostrar_datos(datos)
            
            # Publicar mensaje MQTT
            result = client.publish(topic, json.dumps(datos))
            
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                print("✅ Mensaje MQTT enviado exitosamente")
            else:
                print(f"❌ Error publicando mensaje MQTT: {result.rc}")
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n🛑 Publicador MQTT detenido")
    except Exception as e:
        print(f"💥 Error: {e}")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()