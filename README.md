# LECTOSTR - Analizador de Texto

LECTOSTR es una aplicación de escritorio desarrollada con Python y Flet que permite analizar archivos de texto y obtener estadísticas sobre su contenido.

## Características

- **Interfaz gráfica amigable**: Diseño moderno y fácil de usar
- **Análisis completo de texto**: Calcula múltiples métricas de un archivo de texto
- **Manejo de errores**: Sistema de diálogos para informar sobre el estado del proceso
- **Soporte para archivos de texto**: Procesamiento de archivos .txt con codificación UTF-8

## Funcionalidades

La aplicación analiza archivos de texto y calcula:

1. Cantidad total de caracteres en el texto
2. Cantidad de símbolos (todo lo que no sea letra o número)
3. Cantidad de vocales (a, e, i, o, u, tanto mayúsculas como minúsculas)
4. Cantidad de consonantes
5. El carácter que más se repite en el texto

## Requisitos

- Python 3.6 o superior
- Flet
- Bibliotecas: collections, re, os, sys

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tEsveBavi/lectostr.git
cd lectostr
```

2. Instala las dependencias necesarias:
```bash
pip install flet
```

3. Ejecuta la aplicación:
```bash
python main.py
```

## Estructura de Directorios

```
lectostr/
├── main.py           # Archivo principal de la aplicación
├── assets/           # Recursos gráficos 
│   ├── btn_exit.png
│   ├── btn_okver.png
│   ├── btn_uploadinfo.png
│   ├── btn_uploadotherfile.png
│   ├── error_msg.png
│   ├── relsuthere.png
│   └── sucess_msg.png
└── README.md         # Este archivo
```

## Uso

1. Ejecuta la aplicación
2. Haz clic en el botón "Subir archivo .txt"
3. Selecciona un archivo de texto (.txt)
4. Visualiza los resultados del análisis

## Detalles técnicos

- **Interfaz**: Construida con Flet, una biblioteca de Python para crear aplicaciones GUI modernas
- **Procesamiento de texto**: Utiliza expresiones regulares para analizar el contenido
- **Gestión de errores**: Manejo de excepciones para casos como archivos no válidos o errores de lectura

## Sobre el Proyecto

Este proyecto fue desarrollado como parte de la asignatura Proceso Personal para el Desarrollo de Software (PSP0) en el Instituto Tecnológico Superior del Sur del Estado de Yucatán.

## Autora

- Esvetlana Batun Villacis

---

Proyecto creado en 2025 para la materia de Proceso Personal para el Desarrollo de Software.
