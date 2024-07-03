# Proyecto ATM - Simulador de Cajero Automático

Este proyecto es un simulador de cajero automático (ATM) construido utilizando Django para el backend y HTML/CSS para el frontend. 
El objetivo del proyecto es proporcionar una interfaz gráfica de usuario que simula las funcionalidades básicas de un cajero automático, 
como la inserción de una tarjeta, la introducción de un PIN y la visualización del saldo.

## Contenido del Proyecto


### Descripción de Archivos y Directorios

- **atm/**: Contiene la aplicación principal del cajero automático.
  - **views.py**: Define las vistas para la interfaz del ATM.
  - **urls.py**: Define las rutas URL para la aplicación ATM.

- **myproject/**: Contiene la configuración del proyecto Django.
  - **settings.py**: Archivo de configuración principal de Django.
  - **urls.py**: Define las rutas URL para el proyecto principal.

- **statics/**: Contiene archivos estáticos como CSS.
  - **atm.css**: Estilos CSS personalizados para la interfaz del ATM.

- **templates/**: Contiene las plantillas HTML.
  - **atm_interface.html**: Plantilla principal para la interfaz del cajero automático.
  - **transaction_list.html**: Plantilla para mostrar la lista de transacciones (si se implementa).

- **db.sqlite3**: Base de datos SQLite utilizada por Django.

- **manage.py**: Herramienta de línea de comandos para interactuar con el proyecto Django.

- **venv/**: Entorno virtual para gestionar las dependencias del proyecto.

### Funcionalidades

- **Interfaz de Usuario del Cajero Automático**: Simula la interfaz de un cajero automático con un teclado numérico para introducir el PIN y un botón para insertar la tarjeta.
- **Validación del PIN**: Permite introducir un PIN y valida si es correcto.
- **Visualización del Saldo**: Muestra el saldo disponible en la cuenta.

### Cómo Ejecutar el Proyecto

1. Clonar el repositorio:

```sh
git clone https://github.com/javierfevidaho/bank-atm.git
cd bank-atm

### Estructura del Proyecto

myproject/
├── atm/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── migrations/
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── myproject/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── statics/
│ └── css/
│ └── atm.css
├── templates/
│ ├── atm_interface.html
│ └── transaction_list.html
├── db.sqlite3
├── manage.py
├── README.md
└── venv/
