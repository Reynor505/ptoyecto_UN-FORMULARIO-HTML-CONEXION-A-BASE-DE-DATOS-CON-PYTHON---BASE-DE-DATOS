# 📰 Sistema de Registro de Fake News en Redes Sociales

## 📌 Descripción del proyecto

El proyecto consiste en desarrollar un sistema web para registrar, almacenar y visualizar noticias encontradas en diferentes redes sociales, con el propósito de facilitar su seguimiento y clasificación según su veracidad.

El sistema está desarrollado utilizando HTML para la interfaz, Python con Flask para gestionar las operaciones y SQL para almacenar la información en una base de datos.

## 🎯 Objetivo general

Desarrollar un sistema que permita registrar noticias de diferentes redes sociales, guardar sus datos en una base de datos y clasificarlas según su estado de verificación, contribuyendo a combatir la desinformación en Internet.

## ⚙️ Tecnologías utilizadas

- **HTML5:** Estructura de la interfaz web.
- **CSS3:** Diseño y presentación de la página.
- **Python:** Lenguaje utilizado para desarrollar la lógica del sistema.
- **Flask:** Framework encargado de conectar la página web con el servidor.
- **SQL:** Lenguaje utilizado para gestionar y almacenar los registros en la base de datos.
- **Jinja2:** Permite mostrar dinámicamente los datos enviados desde Python hacia HTML.

## 🖥️ Funcionalidades del sistema

### 1. Registro de noticias

El sistema cuenta con un formulario para ingresar la información de cada noticia:

- Título de la noticia.
- Red social donde fue publicada.
- Enlace de la publicación.
- Estado de verificación.
- Fecha de registro.

### 2. Selección de redes sociales

Permite identificar de qué plataforma proviene la publicación:

- Facebook.
- WhatsApp.
- TikTok.
- Instagram.
- X (Twitter).

### 3. Clasificación de noticias

Las noticias pueden registrarse con tres estados:

- **En revisión:** La noticia todavía está siendo analizada.
- **Falsa:** La información ha sido identificada como falsa.
- **Verdadera:** La información ha sido verificada.

### 4. Almacenamiento en SQL

Los datos ingresados mediante el formulario son enviados a Python (Flask), que se encarga de procesarlos y almacenarlos en la base de datos SQL.

Esto permite conservar los registros y consultarlos posteriormente.

### 5. Visualización de registros

El sistema muestra las noticias almacenadas en una tabla con los siguientes campos:

| Campo | Descripción |
|---|---|
| ID | Identificador de la noticia |
| Título | Nombre de la publicación |
| Red social | Plataforma de origen |
| Enlace | Dirección de la publicación |
| Estado | Clasificación de la noticia |
| Fecha | Fecha de registro |

## 📂 Estructura del proyecto

```text
FAKE-NEWS/
│
├── app.py              # Lógica del sistema con Flask
│
├── templates/
│   └── index.html      # Interfaz y formulario de registro
│
├── database.sql        # Base de datos y tablas SQL
│
└── README.md           # Documentación del proyecto
```

## 🔄 Funcionamiento del sistema

El funcionamiento se desarrolla mediante los siguientes pasos:

1. El usuario ingresa a la página web.
2. Completa el formulario con los datos de una noticia.
3. HTML envía la información a `app.py` mediante el método POST.
4. Flask recibe y procesa los datos.
5. Python se conecta con la base de datos SQL y almacena el registro.
6. El sistema consulta los registros almacenados.
7. Finalmente, las noticias aparecen en una tabla dentro de la página web.

