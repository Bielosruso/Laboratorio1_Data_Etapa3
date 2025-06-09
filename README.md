 Laboratorio1_Data_Etapa3 Carga y Validación de DatosAdd commentMore actions

Este proyecto permite cargar automáticamente archivos CSV y Excel desde el directorio `files/`, validarlos y guardarlos en una base de datos MySQL utilizando SQLAlchemy.

 Características

Carga automática de todos los archivos `.csv` y `.xlsx` en la carpeta `files/`.
Validación de tipos de datos, campos obligatorios, eliminación de duplicados y valores nulos.
Persistencia de los datos en una base de datos MySQL, una tabla por archivo.
Mensajes de éxito o error al finalizar la carga de cada archivo.

 Requisitos

Python 3.8+
MySQL
Paquetes Python (revisar `requirements.txt`)

Instalación

1. Clonar el repositorio.
2. Crear y activa un entorno virtual:
    python -m venv venv
    .\venv\Scripts\activate
3. Instalar las dependencias:
    pip install -r requirements.txt
4. Configurar las variables de entorno en el archivo `.env`:
    DB_USER=tu_usuario
    DB_PASSWORD=tu_contraseña
    DB_HOST=localhost
    DB_PORT=3306
    DB_NAME=nombre_base

 Modo de Uso

Colocar los archivos `.csv` y `.xlsx` en la carpeta `files/`.
Ejecutar el programa principal:
    python main.pyAdd commentMore actions
El sistema debera validar y cargar los datos en la base de datos y mostrara un resumen al finalizar.