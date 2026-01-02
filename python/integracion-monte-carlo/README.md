# Integración Numérica con el Método de Monte Carlo

[← Volver al Portafolio Python](../README.md) | [📓 Ver Notebook](./integracion-monte-carlo.ipynb)

## 📋 Descripción

Este proyecto implementa el método de Monte Carlo para calcular la integral definida de una función f(x) en un intervalo [a, b], comparando un enfoque iterativo con uno vectorizado para evaluar su eficiencia y precisión.

La integración numérica es una herramienta clave en ciencia e ingeniería, especialmente cuando las soluciones analíticas no son factibles. Este proyecto demuestra la implementación práctica del método de Monte Carlo y la importancia de la vectorización en Python para mejorar el rendimiento computacional.

## 🎯 Objetivo

Implementar un algoritmo de integración numérica utilizando el método de Monte Carlo en dos versiones:
- **Versión iterativa:** Implementación usando bucles de Python
- **Versión vectorizada:** Implementación usando operaciones vectorizadas de NumPy

El propósito es comparar ambas implementaciones en términos de precisión y eficiencia, validando los resultados con la función `scipy.integrate.quad`.

## 📐 Método de Monte Carlo

El método consiste en generar puntos aleatorios dentro de un rectángulo que contiene el área bajo la curva de la función. La integral se aproxima calculando la proporción de puntos que caen debajo de la curva.

### Fórmula

$$
I \approx \frac{N_{\text{debajo}}}{N_{\text{total}}} \times (b - a) \times M
$$

Donde:
- $N_{debajo}$ es el número de puntos que caen por debajo de la curva
- $N_{total}$ es el número total de puntos generados
- $(b - a)$ es el ancho del intervalo de integración
- $M$ es el valor máximo de la función en el intervalo

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **NumPy** - Operaciones numéricas y vectorización
- **Matplotlib** - Visualización de resultados
- **SciPy** - Validación con `scipy.integrate.quad` y optimización

## 📁 Estructura del Proyecto

```
integracion-monte-carlo/
├── integracion-monte-carlo.ipynb  # Notebook principal
└── README.md
```

## 🚀 Instalación

1. Clonar o descargar el repositorio
2. Instalar las dependencias:

```bash
pip install numpy matplotlib scipy
```

## 📖 Implementación

### Versión Iterativa

Implementación usando bucles de Python para generar puntos aleatorios y evaluar la función punto por punto.

**Características:**
- Fácil de entender
- Más lenta para grandes cantidades de puntos
- Uso de bucles explícitos

### Versión Vectorizada

Implementación usando operaciones vectorizadas de NumPy para generar y evaluar todos los puntos simultáneamente.

**Características:**
- Optimización del máximo usando `scipy.optimize.minimize_scalar`
- Generación vectorizada de puntos aleatorios
- Evaluación vectorizada de la función
- Significativamente más rápida

## 📊 Análisis de Rendimiento

El proyecto incluye un análisis comparativo de rendimiento que muestra:

- **Tiempos de ejecución:** Comparación de tiempos para diferentes números de puntos
- **Precisión:** Comparación de resultados con el valor real calculado por SciPy
- **Escalabilidad:** Comportamiento de ambas versiones al aumentar el número de puntos

### Resultados Esperados

- La versión vectorizada es significativamente más eficiente, especialmente con grandes cantidades de puntos
- Ambas versiones ofrecen aproximaciones razonables al valor real
- La vectorización demuestra su superioridad en computación científica con Python

## 📈 Visualización

El proyecto incluye visualizaciones que muestran:

- Los puntos aleatorios generados (verdes: debajo de la curva, rojos: encima)
- La función objetivo
- Comparación gráfica de rendimiento entre ambas versiones

## 📝 Uso

**📓 [Abrir Notebook](./integracion-monte-carlo.ipynb)**

1. Abrir el notebook `integracion-monte-carlo.ipynb` en Jupyter Notebook o JupyterLab
2. Ejecutar las celdas en orden
3. Observar los resultados de precisión y rendimiento

---

[← Volver al Portafolio Python](../README.md)

## 🔬 Función de Prueba

El proyecto utiliza la función de prueba:

$$f(x) = e^{-x^2}$$

Integrada en el intervalo $[-2, 2]$, que corresponde a una campana de Gauss.

## 💡 Conceptos Aprendidos

- **Método de Monte Carlo:** Técnica de integración numérica basada en muestreo aleatorio
- **Vectorización:** Uso de operaciones vectorizadas de NumPy para mejorar el rendimiento
- **Optimización:** Uso de técnicas de optimización para encontrar el máximo de funciones
- **Benchmarking:** Comparación de rendimiento entre diferentes implementaciones
- **Validación:** Comparación de resultados con métodos analíticos conocidos

## 📄 Licencia

Este proyecto es de carácter educativo.

## 🔗 Referencias

- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Documentation](https://docs.scipy.org/)
- [Monte Carlo Methods](https://en.wikipedia.org/wiki/Monte_Carlo_method)


