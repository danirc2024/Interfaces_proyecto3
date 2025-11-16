# http_post_nodered.py
import requests
import json
import time
from generador_datos import generar_datos, mostrar_datos

# Configuración NodeRed
NODERED_URL = "http://localhost:1880/dUMA"

def enviar_a_nodered(datos):
    """Envía datos a NodeRed via HTTP POST"""
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(NODERED_URL, json=datos, headers=headers, timeout=5)
        
        if response.status_code == 200:
            print(f"✅ Datos enviados a NodeRed - Código: {response.status_code}")
            return True
        else:
            print(f"❌ Error NodeRed - Código: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ No se pudo conectar a NodeRed. ¿Está ejecutándose?")
        return False
    except Exception as e:
        print(f"❌ Error enviando a NodeRed: {e}")
        return False

def main():
    print("=== Enviador de Datos a NodeRed ===")
    print(f"URL: {NODERED_URL}")
    print("Enviando datos cada 5 segundos...")
    print("Presiona Ctrl+C para detener\n")
    
    contador = 0
    try:
        while True:
            contador += 1
            datos = generar_datos()
            
            print(f"\n--- Envío #{contador} a NodeRed ---")
            mostrar_datos(datos)
            
            # Enviar a NodeRed
            enviar_a_nodered(datos)
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n🛑 Enviador NodeRed detenido")
    except Exception as e:
        print(f"💥 Error inesperado: {e}")

if __name__ == "__main__":
    main()