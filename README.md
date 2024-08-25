# Pruebas Automatizadas Móviles

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

## Explicación de la estructura:

- config/: Contiene archivos de configuración separados para iOS y Android.
- ios_config.py: Configuraciones específicas para iOS.
- android_config.py: Configuraciones específicas para Android.
- tests/: Contiene todos tus casos de prueba.
- ios/: Pruebas específicas para iOS.
- android/: Pruebas específicas para Android.
- common/: Pruebas que se pueden ejecutar en ambas plataformas.
- pages/: Implementa el patrón Page Object Model.
- ios/ y android/: Contienen clases que representan pantallas específicas de cada plataforma.
- base_page.py: Clase base con métodos comunes para todas las páginas.
- utils/: Funciones y clases de utilidad.
- custom_wait.py: Funciones personalizadas de espera.
- test_data.py: Datos de prueba compartidos.
- reports/: Carpeta para almacenar los informes generados por las pruebas.
- apps/: Almacena los archivos IPA y APK de tu aplicación.
- requirements.txt: Lista todas las dependencias de Python necesarias.
- conftest.py: Configuraciones y fixtures de pytest.
- README.md: Documentación del proyecto.

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

## Configurar herramientas específicas de la plataforma
1. Para iOS:
   Instala Xcode desde la App Store

   Instala el comando xcrun ejecutando en la terminal:
   ```
   Copyxcode-select --install
   ```
2. Para Android:
   Descarga e instala Android Studio
   Configura las variables de entorno:

   ANDROID_HOME: ruta al SDK de Android
   JAVA_HOME: ruta a tu instalación de Java
   Añade $ANDROID_HOME/tools, $ANDROID_HOME/tools/bin, y $ANDROID_HOME/platform-tools a tu PATH

## Instalar drivers específicos de Appium
Para iOS:
```
Copyappium driver install xcuitest
```
Para Android:
```
Copyappium driver install uiautomator2
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