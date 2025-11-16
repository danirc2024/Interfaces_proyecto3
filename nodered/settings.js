module.exports = {
    // Puerto HTTP
    uiPort: process.env.PORT || 1880,
    
    // Configuración del dashboard UI
    ui: { path: "ui" },
    
    // Configuración del editor
    editorTheme: {
        page: {
            title: "Dashboard Ambiental",
            favicon: "/absolute/path/to/theme/icon",
            css: "/absolute/path/to/custom/css/file",
            scripts: [ "/absolute/path/to/custom/script/file" ]
        },
        header: {
            title: "Node-RED Dashboard Ambiental",
            image: "/absolute/path/to/header/image",
            url: "http://estoyfrito.cl"
        }
    },

    // Configuración de almacenamiento
    flowFile: 'flows.json',
    flowFilePretty: true,

    // Configuración de usuario
    userDir: './',
    
    // Configuración de administración
    adminAuth: null,
    
    // Habilitar el dashboard
    dashboard: {},

    // Configuración de logging
    logging: {
        console: {
            level: "info",
            metrics: false,
            audit: false
        }
    },

    // Configuración adicional
    exportGlobalContextKeys: false,
    externalModules: {}
};