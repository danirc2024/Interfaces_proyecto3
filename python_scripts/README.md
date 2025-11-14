# Python Scripts - Dashboard Ambiental

Esta carpeta contiene todos los scripts Python del proyecto.

## 📁 Archivos

### `generador_datos.py`
Genera el JSON **dUMA** con datos ambientales simulados usando `numpy`.

**Datos generados:**
- `te`: Temperatura (°C)
- `hr`: Humedad del aire (%)
- `pa`: Presión atmosférica (hPa)
- `p01`, `p25`, `p10`: Material particulado
- `h03`, `h05`, `h01`, `h25`, `h50`, `h10`: Histogramas MP

**Uso:**
```bash
python generador_datos.py
```

### `http_post_nodered.py`
Envía datos JSON al dashboard de NodeRed mediante HTTP POST.

**Configuración:**
- URL: `http://localhost:1880/sensores` (ajustar según tu setup)

**Uso:**
```bash
python http_post_nodered.py
```

### `http_post_grafana.py`
Envía datos JSON a Grafana mediante HTTP POST.

**Configuración:**
- URL: `http://localhost:3000/api/live/push`
- Requiere API Key de Grafana

**Uso:**
```bash
python http_post_grafana.py
```

### `mqtt_publisher.py`
Publica datos JSON al tópico `sensores` en el broker Mosquitto.

**Configuración:**
- Broker: `localhost:1883`
- Tópico: `sensores`
- Requiere usuario y contraseña

**Uso:**
```bash
python mqtt_publisher.py
```

### `mqtt_subscriber.py`
Se suscribe al tópico `sensores` y recibe datos JSON.

**Configuración:**
- Broker: `localhost:1883`
- Tópico: `sensores`
- Requiere usuario y contraseña

**Uso:**
```bash
python mqtt_subscriber.py
```

## 🔧 Dependencias

Instalar con pip:
```bash
pip install numpy paho-mqtt requests
```

O usando el archivo requirements.txt (si existe):
```bash
pip install -r requirements.txt
```

## 📝 Notas

- Ajustar las URLs y credenciales en cada script según tu configuración
- Los scripts están diseñados para ejecutarse de forma independiente
- Usar las credenciales del archivo `config/credentials.env`
