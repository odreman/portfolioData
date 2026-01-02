# Web Scraping: Extracción de Datos de Librería Online

[← Volver al Portafolio Python](../README.md) | [📓 Ver Notebook](./web-scraping-libreria-libros.ipynb)

## 📋 Descripción

Este proyecto implementa técnicas de web scraping para extraer información de una librería online. Se utilizan herramientas como BeautifulSoup y Selenium para recuperar datos estructurados de páginas web, demostrando diferentes enfoques y niveles de complejidad en la extracción de datos.

El sitio web utilizado es [Books to Scrape](http://books.toscrape.com/), una plataforma diseñada específicamente para practicar técnicas de scraping.

## 🎯 Objetivos

- Extraer información estructurada (títulos, precios, calificaciones) de páginas web
- Implementar scraping de una sola página y de múltiples páginas
- Comparar diferentes técnicas y herramientas de scraping
- Organizar los datos extraídos en estructuras de datos manejables (DataFrames)

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **BeautifulSoup4** - Parsing de HTML
- **Requests** - Peticiones HTTP
- **Pandas** - Manipulación y estructuración de datos
- **Selenium** - Automatización de navegador (opcional)

## 📁 Estructura del Proyecto

```
web-scraping-libreria-libros/
├── web-scraping-libreria-libros.ipynb  # Notebook principal
├── books_to_scrape.png                  # Captura del sitio web
└── README.md
```

## 🚀 Instalación

1. Clonar o descargar el repositorio
2. Instalar las dependencias:

```bash
pip install beautifulsoup4 requests pandas lxml
```

Para usar Selenium (opcional):

```bash
pip install selenium webdriver-manager
```

## 📖 Ejercicios Implementados

### Ejercicio 1: Extracción Básica
Recuperar los datos de título y precio de los 20 libros de la primera página.

**Tecnologías:** BeautifulSoup, Requests

### Ejercicio 2: Extracción Ampliada
Recuperar título, precio y calificación (rating) de los 20 libros de la primera página.

**Tecnologías:** BeautifulSoup, Requests

### Ejercicio 3: Scraping Multi-página
Recuperar título, precio y calificación para todos los libros del sitio web (múltiples páginas).

**Tecnologías:** BeautifulSoup, Requests, Selenium (opcional)

## 💡 Conceptos Aprendidos

- **Parsing HTML:** Uso de BeautifulSoup para navegar y extraer datos de estructuras HTML
- **Manejo de peticiones HTTP:** Uso de la librería Requests para obtener contenido web
- **Navegación entre páginas:** Implementación de bucles para recorrer múltiples páginas
- **Limpieza de datos:** Procesamiento y transformación de datos extraídos
- **Estructuración de datos:** Organización de datos en DataFrames de Pandas

## 📝 Uso

**📓 [Abrir Notebook](./web-scraping-libreria-libros.ipynb)**

1. Abrir el notebook `web-scraping-libreria-libros.ipynb` en Jupyter Notebook o JupyterLab
2. Ejecutar las celdas en orden
3. Cada ejercicio está documentado y puede ejecutarse de forma independiente

---

[← Volver al Portafolio Python](../README.md)

## ⚠️ Consideraciones Éticas

Este proyecto utiliza un sitio web diseñado específicamente para practicar scraping. Al realizar web scraping en sitios web reales, es importante:

- Respetar los términos de servicio del sitio web
- Revisar el archivo `robots.txt` del sitio
- Implementar delays entre peticiones para no sobrecargar el servidor
- Usar headers apropiados en las peticiones HTTP
- Considerar el uso de APIs oficiales cuando estén disponibles

## 📊 Resultados

El proyecto demuestra la capacidad de extraer y estructurar datos de páginas web, obteniendo información de cientos de libros organizada en un DataFrame de Pandas para su posterior análisis.

## 🔗 Referencias

- [Books to Scrape](http://books.toscrape.com/) - Sitio web utilizado para el proyecto
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://requests.readthedocs.io/)


