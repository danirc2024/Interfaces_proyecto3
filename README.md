# Dashboard Ambiental - Estoy Frito Ltda

Prototipo de Dashboard ambiental para análisis de calidad del aire y condiciones ambientales.

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema completo de monitoreo ambiental que incluye:
- Generación de datos simulados de sensores ambientales
- Publicación y suscripción de datos mediante protocolo MQTT
- Visualización en dashboards interactivos (NodeRed y Grafana)

## 🏗️ Estructura del Proyecto

```
Interfaces_proyecto3/
│
├── python_scripts/           # Scripts de Python (más claro)
│   ├── generador_datos.py    # Genera el JSON dUMA
│   ├── http_post_nodered.py  # Envía datos a NodeRed vía HTTP
│   ├── http_post_grafana.py  # Envía datos a Grafana vía HTTP
│   ├── mqtt_publicador.py    # Publicador MQTT
│   ├── mqtt_suscriptor.py    # Suscriptor MQTT
│   └── README.md             # Documentación de scripts
│
├── nodered/                  # Configuración NodeRed
│   ├── flows.json           # Flujos de NodeRed
│   ├── package.json         # Dependencias npm
│   ├── settings.js          # Configuración del servidor
│   ├── run_nodered.bat      # Script para iniciar NodeRed
│   └── README.md            # Guía de uso NodeRed
│
├── grafana/                 # Configuración Grafana
│   ├── dashboard.json       # Exportación del dashboard
│   ├── datasource.yaml      # Configuración de fuente de datos
│   ├── provisioning/        # Configuración automática
│   └── README.md            # Guía de uso Grafana
│
├── mosquitto/              # Broker MQTT
│   ├── mosquitto.conf      # Configuración del broker
│   ├── passwd              # Usuarios y contraseñas
│   ├── run_mosquitto.bat   # Script para iniciar Mosquitto
│   └── README.md           # Guía de configuración
│
├── config/                 # Configuraciones generales
│   ├── credentials.env     # Variables de entorno
│   └── README.md
│
├── docs/                   # Documentación
│   ├── setup_instructions.md
│   ├── user_manual.md
│   └── screenshots/
│
├── .gitignore             # Archivos ignorados
└── README.md             # Este archivo
```

## 🔧 Recursos Necesarios

### Software y Servicios
1. **NodeRed** - https://nodered.org/
2. **Grafana** - https://grafana.com/
3. **Mosquitto Broker** - https://mosquitto.org/
4. **Python 3.x** con librería `paho-mqtt`

### Instalación de Librerías Python
```bash
pip install paho-mqtt numpy
```

## 📊 Estructura de Datos JSON (dUMA)

El sistema genera un JSON con los siguientes datos ambientales:

```json
{
  "te": "float",     // Temperatura (°C) - np.random.normal(20,2,1)
  "hr": "float",     // Humedad del aire (%) - np.random.normal(70,2,1)
  "pa": "float",     // Presión atmosférica (hPa) - np.random.normal(900,10,1)
  "p01": "float",    // MP 1.0 ug/m3 - np.random.normal(20,2,1)
  "p25": "float",    // MP 2.5 ug/m3 - np.random.normal(30,2,1)
  "p10": "float",    // MP 10 ug/m3 - np.random.normal(30,2,1)
  "h03": "float",    // Histograma MP 0.3 um - np.random.normal(1000,10,1)
  "h05": "float",    // Histograma MP 0.5 um - np.random.normal(1000,10,1)
  "h01": "float",    // Histograma MP 1.0 um - np.random.normal(1000,10,1)
  "h25": "float",    // Histograma MP 2.5 um - np.random.normal(1000,10,1)
  "h50": "float",    // Histograma MP 5.0 um - np.random.normal(1000,10,1)
  "h10": "float"     // Histograma MP 10 um - np.random.normal(1000,10,1)
}
```

## 🚀 Inicio Rápido

### 1. Iniciar Mosquitto Broker
```bash
cd mosquitto
.\run_mosquitto.bat
```

### 2. Iniciar NodeRed
```bash
cd nodered
.\run_nodered.bat
```
Dashboard disponible en: `http://localhost:1880/ui`

### 3. Iniciar Grafana
- Iniciar servicio de Grafana
- Acceder a: `http://localhost:3000`

### 4. Ejecutar Scripts Python
```bash
cd python_scripts
python generador_datos.py        # Genera datos
python mqtt_publicador.py        # Publica vía MQTT
python http_post_nodered.py      # Envía a NodeRed
```

## 🚀 Flujo de Trabajo del Sistema

1. **Generación de Datos**: Script Python genera JSON con datos ambientales aleatorios
2. **Publicación HTTP POST**: Datos se envían a Dashboard en NodeRed vía HTTP POST
3. **Publicación HTTP POST**: Datos se envían a Dashboard en Grafana vía HTTP POST
4. **Publicación MQTT**: Datos se publican al tópico 'sensores' mediante Mosquitto Broker
5. **Suscripción MQTT**: Script suscriptor recibe datos y los envía al Dashboard de NodeRed
6. **Visualización**: Dashboards muestran datos en tiempo real con gráficos interactivos

## 📱 Dashboards

### NodeRed Dashboard
- IAQ Index con medidor visual
- Temperatura con gráfico temporal
- Humedad con gráfico temporal
- Presión atmosférica con gráfico temporal
- Indicadores de calidad del aire
- Registro de callback configurable

### Grafana Dashboard
- Visualización avanzada de series temporales
- Gráficos estadísticos de calidad del aire
- Histogramas de material particulado
- Alertas configurables

## 🔐 Seguridad

- Configurar Mosquitto Broker con **password** y **clave** seguras
- Credenciales para Publicadores y Suscriptores
- No incluir credenciales en el repositorio (usar variables de entorno)

## 👨‍💻 Desarrollo

Para comenzar a desarrollar:

1. Clona el repositorio
2. Instala las dependencias de Python
3. Configura Mosquitto Broker, NodeRed y Grafana
4. Lee la documentación en cada carpeta (`README.md`)
5. Comienza por el generador de datos en `scripts/generador_datos/`

## 📝 Notas

- Este es un proyecto académico para "Estoy Frito Ltda"
- Objetivo: Aprender tecnologías de visualización de datos en dashboards
- Los datos son simulados con distribuciones normales aleatorias

## 🤝 Contribuciones

Este es un proyecto académico. Consulta con el equipo antes de realizar cambios importantes.
