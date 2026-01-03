# Análisis de Atletas Olímpicos

## 📋 Descripción
Este proyecto analiza datos históricos de atletas olímpicos, explorando diferentes aspectos demográficos y de rendimiento. El conjunto de datos abarca múltiples ediciones de los Juegos Olímpicos, ofreciendo una visión completa del perfil de los atletas a lo largo del tiempo.

## 🎯 Objetivos

- Analizar la distribución de edades de los atletas olímpicos
- Explorar las diferencias de rendimiento entre géneros
- Identificar tendencias históricas en los Juegos Olímpicos
- Examinar la relación entre características físicas y rendimiento deportivo

## 📊 Datos

El conjunto de datos principal (`athlete_events.csv`) contiene información sobre:
- **ID**: Identificador único del atleta
- **Name**: Nombre completo del atleta
- **Sex**: Género (M/F)
- **Age**: Edad en años
- **Height**: Altura en centímetros
- **Weight**: Peso en kilogramos
- **Team**: Equipo/país
- **NOC**: Código de país del COI
- **Games**: Año y temporada de los Juegos
- **Year**: Año de los Juegos
- **Season**: Temporada (Verano/Invierno)
- **City**: Ciudad sede
- **Sport**: Deporte
- **Event**: Evento específico
- **Medal**: Tipo de medalla (Oro/Plata/Bronce/NA)

## 🛠️ Herramientas Utilizadas

- **Python** para análisis de datos
- **Pandas** para manipulación de datos
- **Matplotlib** y **Seaborn** para visualizaciones
- **Jupyter Notebook** para análisis interactivo
- **Estadísticas descriptivas** para análisis exploratorio

## 📂 Estructura del Proyecto

```
olympic_athletes_analysis/
├── athlete_events.csv
├── analisis_atletas_olimpicos.ipynb
└── README.md
```

## 📝 Hallazgos Clave

### Distribución de Edades
- Análisis de la distribución de edades de los atletas
- Identificación de la edad promedio y rangos más comunes
- Comparación entre diferentes ediciones de los Juegos

### Análisis por Género
- Proporción de atletas masculinos vs. femeninos a lo largo del tiempo
- Diferencias en rendimiento entre géneros
- Evolución de la participación femenina

### Características Físicas
- Relación entre altura, peso y rendimiento
- Diferencias por deporte y categoría
- Evolución de las características físicas a lo largo del tiempo

## 🚀 Cómo Ejecutar

1. Clona el repositorio
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Abre el notebook en Jupyter:
   ```bash
   jupyter notebook analisis_atletas_olimpicos.ipynb
   ```

## 📝 Notas Adicionales

- Los datos incluyen información desde los primeros Juegos Olímpicos modernos hasta la actualidad
- Se han implementado técnicas de limpieza de datos para manejar valores faltantes
- Las visualizaciones permiten identificar patrones interesantes en la evolución del deporte olímpico

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## ✉️ Contacto

Para más información o colaboraciones, no dudes en contactarme.
