# Análisis de Ajedrez y Homicidios

## 📋 Descripción
Este proyecto explora la relación entre las estadísticas de partidas de ajedrez y datos de homicidios, analizando patrones y correlaciones inusuales. El análisis combina datos de partidas de ajedrez en línea con estadísticas de criminalidad para descubrir posibles conexiones sorprendentes.

## 🎯 Objetivos

- Analizar estadísticas de partidas de ajedrez en línea
- Explorar patrones en datos de homicidios
- Identificar correlaciones entre los dos conjuntos de datos
- Visualizar los hallazgos de manera efectiva

## 📊 Datos

### Datos de Ajedrez (`games.csv`)
- **id**: Identificador único de la partida
- **rated**: Si la partida fue calificada
- **created_at**: Fecha de creación de la partida
- **last_move_at**: Último movimiento
- **turns**: Número de turnos
- **victory_status**: Estado de la victoria
- **winner**: Color del ganador (blanco/negro)
- **white/black_rating**: Puntuación ELO de los jugadores
- **moves**: Secuencia de movimientos
- **opening_***: Información sobre la apertura

### Datos de Homicidios (`homicide.csv`)
- **record_id**: Identificador único
- **agency_name**: Nombre de la agencia
- **agency_type**: Tipo de agencia
- **state**: Estado
- **year**: Año del incidente
- **month**: Mes del incidente
- **incident**: Número de incidente
- **crime_type**: Tipo de crimen
- **victim_***: Información sobre la víctima
- **offender_***: Información sobre el agresor
- **relationship**: Relación entre víctima y agresor

## 🛠️ Herramientas Utilizadas

- **Python** para análisis de datos
- **Pandas** para manipulación de datos
- **Matplotlib** y **Seaborn** para visualizaciones
- **Jupyter Notebook** para análisis interactivo
- **Estadísticas** para análisis de correlación

## 📂 Estructura del Proyecto

```
chess_homicide_analysis/
├── games.csv
├── homicide.csv
├── analisis_ajedrez_homicidios.ipynb
└── README.md
```

## 📝 Hallazgos Clave

### Análisis de Partidas de Ajedrez
- Distribución de victorias por color de piezas
- Relación entre el rating ELO y la probabilidad de victoria
- Análisis de aperturas más comunes

### Análisis de Homicidios
- Tendencias temporales en la incidencia de homicidios
- Relación entre víctimas y agresores
- Patrones geográficos

### Correlaciones
- Posibles relaciones entre patrones de juego y estadísticas de criminalidad
- Análisis temporal comparativo

## 🚀 Cómo Ejecutar

1. Clona el repositorio
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Abre el notebook en Jupyter:
   ```bash
   jupyter notebook analisis_ajedrez_homicidios.ipynb
   ```

## 📝 Notas Adicionales

- Los datos de ajedrez provienen de partidas en línea
- Las estadísticas de homicidios cubren múltiples años
- Se han implementado técnicas de limpieza de datos para garantizar la calidad del análisis

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## ✉️ Contacto

Para más información o colaboraciones, no dudes en contactarme.
