# Proyecto de Pruebas Automatizadas con Appium

Este proyecto contiene pruebas automatizadas para aplicaciones móviles iOS y Android utilizando Appium.

## Estructura del Proyecto

```
appium-test-project/
│
├── config/
│   ├── ios_config.py
│   └── android_config.py
│
├── tests/
│   ├── ios/
│   ├── android/
│   └── common/
│
├── pages/
│   ├── ios/
│   ├── android/
│   └── base_page.py
│
├── utils/
│   ├── custom_wait.py
│   └── test_data.py
│
├── reports/
├── apps/
├── requirements.txt
├── conftest.py
└── README.md
```

## Requisitos Previos

- Python 3.7+
- Node.js y npm
- Appium Server
- Xcode (para pruebas en iOS)
- Android Studio y SDK (para pruebas en Android)

## Configuración del Entorno

1. Instala las dependencias de Python:
   ```
   pip install -r requirements.txt
   ```

2. Instala Appium:
   ```
   npm install -g appium
   ```

3. Configura las variables de entorno:
   - ANDROID_HOME: ruta al SDK de Android
   - JAVA_HOME: ruta a tu instalación de Java

## Configuración de las Pruebas

1. Coloca tus archivos .ipa (iOS) y .apk (Android) en la carpeta `apps/`.
2. Actualiza las rutas y capacidades deseadas en `config/ios_config.py` y `config/android_config.py`.

## Ejecución de las Pruebas

Para ejecutar todas las pruebas:
```
pytest
```

Para ejecutar pruebas específicas de iOS:
```
pytest tests/ios
```

Para ejecutar pruebas específicas de Android:
```
pytest tests/android
```

## Generación de Reportes

Los reportes se generarán automáticamente en la carpeta `reports/` después de cada ejecución de pruebas.

## Contribución

1. Haz un fork del proyecto
2. Crea una nueva rama (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Contacto

Juan Pablo Melinao González - j.melinao@live.cl

Enlace del proyecto: [https://github.com/neobones/pruebas.Automatizadas.moviles](https://github.com/neobones/pruebas.Automatizadas.moviles)

## Agradecimientos

- [Appium](https://appium.io/)
- [Selenium](https://www.selenium.dev/)
- [pytest](https://docs.pytest.org/)