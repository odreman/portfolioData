# Análisis de Cerveza y StackOverflow

## 📋 Descripción
Este proyecto combina dos conjuntos de datos aparentemente dispares: recetas de cerveza artesanal y preguntas de StackOverflow. El objetivo es descubrir patrones y correlaciones inesperadas entre estos dominios, aplicando técnicas de análisis de datos y visualización.

## 🎯 Objetivos

- Analizar estadísticas de recetas de cerveza artesanal
- Explorar patrones en preguntas de programación de StackOverflow
- Identificar correlaciones entre ambos conjuntos de datos
- Visualizar los hallazgos de manera efectiva

## 📊 Datos

### Recetas de Cerveza (`recipeData.csv`)
- **BeerID**: Identificador único de la receta
- **Name**: Nombre de la cerveza
- **URL**: Enlace a la receta
- **Style**: Estilo de cerveza
- **ABV**: Porcentaje de alcohol por volumen
- **IBU**: Unidades Internacionales de Amargor
- **Color**: Color de la cerveza
- **BrewMethod**: Método de elaboración
- **SugarScale**: Escala de azúcar utilizada
- **BrewMethod**: Método de elaboración
- **PitchRate**: Tasa de levadura
- **PrimaryTemp**: Temperatura de fermentación primaria

### Preguntas de StackOverflow (`stackoverflow.csv`)
- **Id**: Identificador único de la pregunta
- **CreationDate**: Fecha de creación
- **Score**: Puntuación de la pregunta
- **ViewCount**: Número de visualizaciones
- **Tags**: Etiquetas de la pregunta
- **AnswerCount**: Número de respuestas
- **CommentCount**: Número de comentarios
- **FavoriteCount**: Número de favoritos
- **Body**: Contenido de la pregunta

## 🛠️ Herramientas Utilizadas

- **Python** para análisis de datos
- **Pandas** para manipulación de datos
- **Matplotlib** y **Seaborn** para visualizaciones
- **Jupyter Notebook** para análisis interactivo
- **Análisis estadístico** para descubrir correlaciones

## 📂 Estructura del Proyecto

```
beer_stackoverflow_analysis/
├── recipeData.csv
├── stackoverflow.csv
├── analisis_cerveza_stackoverflow.ipynb
└── README.md
```

## 📝 Hallazgos Clave

### Análisis de Cerveza
- Distribución de estilos de cerveza más populares
- Relación entre ABV, IBU y color
- Tendencias en métodos de elaboración

### Análisis de StackOverflow
- Lenguajes de programación más preguntados
- Correlación entre vistas, respuestas y puntuación
- Evolución temporal de las preguntas

### Correlaciones Cruzadas
- Posibles relaciones entre preferencias de cerveza y tecnologías
- Análisis de tendencias temporales comparativas

## 🚀 Cómo Ejecutar

1. Clona el repositorio
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Abre el notebook en Jupyter:
   ```bash
   jupyter notebook analisis_cerveza_stackoverflow.ipynb
   ```

## 📝 Notas Adicionales

- Los datos de cerveza incluyen miles de recetas caseras
- Las preguntas de StackOverflow cubren múltiples tecnologías
- Se han implementado técnicas de limpieza de datos para garantizar la calidad del análisis

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## ✉️ Contacto

Para más información o colaboraciones, no dudes en contactarme.
