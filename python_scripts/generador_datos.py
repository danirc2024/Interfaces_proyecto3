# generador_datos.py
import numpy as np
import json
from datetime import datetime

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
        'timestamp': datetime.utcnow().isoformat() + 'Z'  # Timestamp en UTC
    }

def mostrar_datos(datos):
    """Muestra los datos generados en consola"""
    print(f"Temperatura: {datos['te']}°C | Humedad: {datos['hr']}% | Presión: {datos['pa']}hPa")
    print(f"MP1.0: {datos['p01']} | MP2.5: {datos['p25']} | MP10: {datos['p10']} ug/m3")
    print(f"Timestamp: {datos['timestamp']}")

if __name__ == "__main__":
    # Ejemplo de uso
    datos = generar_datos()
    print("=== Datos dUMA Generados ===")
    mostrar_datos(datos)
    print("\nJSON completo:")
    print(json.dumps(datos, indent=2))