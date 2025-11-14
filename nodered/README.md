# NodeRed Configuration

Esta carpeta contiene la configuración y flujos de NodeRed para el dashboard ambiental.

## 📁 Archivos

### `flows.json`
Exportación de los flujos de NodeRed que incluyen:
- Endpoint HTTP POST para recibir datos
- Suscriptor MQTT al tópico 'sensores'
- Dashboard UI con visualizaciones
- Procesamiento de datos dUMA

### `package.json`
Dependencias de NodeRed y nodos adicionales necesarios:
- `node-red-dashboard`: Dashboard UI
- `node-red-contrib-mqtt-broker`: Cliente MQTT
- Otros nodos personalizados

### `settings.js`
Configuración de NodeRed:
- Puerto del servidor (por defecto 1880)
- Configuración de seguridad
- Rutas de archivos
- Configuración del editor

### `run_nodered.bat`
Script de Windows para iniciar NodeRed fácilmente.

## 🚀 Inicio Rápido

### 1. Instalar NodeRed
```bash
npm install -g node-red
```

### 2. Instalar dependencias
```bash
cd nodered
npm install
```

### 3. Iniciar NodeRed

**Opción A - Usando el script:**
```bash
.\run_nodered.bat
```

**Opción B - Manual:**
```bash
node-red --userDir .
```

### 4. Acceder al editor
Abrir en el navegador: `http://localhost:1880`

### 5. Importar flujos
1. Ir a menú → Import
2. Seleccionar `flows.json`
3. Deploy

## 📊 Dashboard

Acceder al dashboard en: `http://localhost:1880/ui`

**Características:**
- IAQ Index (Índice de calidad del aire)
- Gráficos de temperatura en tiempo real
- Gráficos de humedad
- Gráficos de presión atmosférica
- Indicadores de material particulado
- Configuración de callback

## 🔧 Configuración MQTT

Configurar en el flujo de NodeRed:
- Broker: `localhost:1883`
- Tópico: `sensores`
- Usuario/Contraseña: Ver `config/credentials.env`

## 📝 Notas

- Asegúrate de que Mosquitto Broker esté corriendo antes de iniciar
- Los flujos se guardan automáticamente en `flows.json`
- El dashboard es accesible en la red local
