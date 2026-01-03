# Redes Neuronales DNN

## 📋 Descripción

Dos proyectos que demuestran el uso de redes neuronales densas (DNN) para resolver problemas de clasificación. El primero resuelve el problema clásico XOR (no linealmente separable) y el segundo clasifica imágenes de ropa del dataset Fashion MNIST.

## 🎯 Objetivos

1. **Problema XOR:** Demostrar que las redes neuronales multicapa pueden resolver problemas no linealmente separables (ser más listos que los SVMs)
2. **Fashion MNIST:** Clasificar imágenes de prendas de ropa en 10 categorías diferentes

### Objetivos de Aprendizaje

- Conocer y aplicar redes neuronales profundas en problemas supervisados de machine learning
- Familiarizarse con TensorFlow y Keras como frameworks para desarrollar redes neuronales
- Comprender la normalización en Deep Learning
- Comprender la tasa de aprendizaje (learning rate) en Deep Learning
- Aprender a construir un problema y un modelo desde cero

## 📚 Notebooks

### 1. Problema XOR (`S5_DL_practice1_XOR.ipynb`)
Implementación de una DNN para resolver el problema XOR, demostrando la capacidad de las redes multicapa para aprender funciones no lineales.

**Características:**
- Arquitectura: 2-2-1 (2 entradas, 2 neuronas ocultas, 1 salida)
- Función de activación: Sigmoid en capa oculta
- Optimizador: SGD con learning rate 0.1
- Entrenamiento: 1000 épocas

**Resultados:**
- La red aprende correctamente la función XOR
- Predicciones obtenidas:
  - [0,0] → 0.3034 (esperado: 0)
  - [0,1] → 0.5404 (esperado: 1)
  - [1,0] → 0.5362 (esperado: 1)
  - [1,1] → 0.6198 (esperado: 0)

**Análisis de Pesos:**
- La capa oculta transforma el espacio 2D de entrada en un nuevo espacio 2D
- La función sigmoid "dobla" el espacio para separar los puntos del XOR
- La capa de salida combina las activaciones de la capa oculta para formar las regiones de decisión
- El XOR funciona porque la capa oculta crea dos líneas de decisión que, al combinarse, forman las regiones necesarias para separar los puntos (0,0),(1,1) de los puntos (0,1),(1,0)

### 2. Fashion MNIST (`S5_DL_practice1_FasMNIST.ipynb`)
Clasificación de imágenes de ropa en 10 categorías usando una DNN optimizada.

**Características:**
- 10 clases: Camisetas, pantalones, zapatos, etc.
- Arquitectura: Múltiples capas densas
- Optimización de hiperparámetros y técnicas de normalización

**Técnicas Implementadas:**

1. **Normalización de Datos (TODOs 1-3):**
   - Escalado a rango [0,1]: Dividir por 255.0
   - Centrado a media 0: Restar la media
   - Estandarización N(0,1): Normalizar a media 0 y varianza 1

2. **Análisis de Normalización (TODO 4):**
   - Comparación de 3 tipos de normalización
   - **Mejor resultado:** Estandarización N(0,1) con 88.71% de precisión
   - La normalización mejora significativamente la convergencia y estabilidad

3. **Optimización de Learning Rate (TODO 5):**
   - Experimentación con learning rates: [0.1, 0.001, 0.0001]
   - **Mejor resultado:** 0.001 con 88.25% de precisión
   - Learning rate alto (0.1) impide el aprendizaje
   - Learning rate bajo (0.0001) ralentiza innecesariamente

4. **Callbacks (TODOs 6-7):**
   - Implementación de ReduceLROnPlateau
   - **Mejora significativa:** De 88.25% a 90.14% de precisión
   - Ajuste automático del learning rate cuando la pérdida se estanca

## 🔧 Tecnologías Utilizadas

- **TensorFlow/Keras:** Framework principal
- **DNN:** Redes neuronales densas (fully connected)
- **NumPy:** Procesamiento numérico
- **Matplotlib:** Visualización

## 📊 Datasets

### XOR
- 4 ejemplos de entrenamiento
- Entrada binaria (2D)
- Salida binaria

### Fashion MNIST
- 70,000 imágenes (28x28 píxeles)
- 10 clases de prendas de ropa
- División: 60,000 train / 10,000 test

## 🏗️ Arquitecturas

### XOR
```
Input (2) → Hidden (2) → Output (1)
```

### Fashion MNIST
```
Input (784) → Hidden Layers → Output (10)
```

## 📈 Características Principales

### Fashion MNIST

- **Normalización exhaustiva:** Comparación de 3 tipos (rango [0,1], media 0, N(0,1))
- **Optimización de learning rate:** Experimentación sistemática con diferentes valores
- **Callbacks avanzados:** ReduceLROnPlateau para ajuste automático del learning rate
- **Análisis de curvas de aprendizaje:** Evaluación detallada de convergencia y estabilidad

### Problema XOR

- **Resolución de problemas no linealmente separables:** Demostración práctica de la necesidad de capas ocultas
- **Análisis de pesos entrenados:** Comprensión de cómo la red transforma el espacio de entrada
- **Visualización de la transformación:** Explicación de cómo las capas ocultas crean regiones de decisión

## 🎯 Resultados Clave

### Fashion MNIST

| Técnica | Configuración | Test Accuracy |
|---------|---------------|---------------|
| **ReduceLROnPlateau** | Callback con patience=2, factor=0.5 | **0.9014** ⭐ |
| Learning Rate óptimo | 0.001 (fijo) | 0.8825 |
| Normalización óptima | Estandarización N(0,1) | 0.8871 |
| Normalización básica | Rango [0,1] | 0.8732 |
| Centrado | Media 0 | 0.8768 |

**Hallazgos:**
- La estandarización N(0,1) obtiene el mejor resultado entre las normalizaciones (88.71%)
- El learning rate de 0.001 ofrece el mejor equilibrio entre velocidad y precisión
- ReduceLROnPlateau mejora significativamente el resultado final (90.14%)
- Las normalizaciones mejoran la convergencia y estabilidad del entrenamiento

### Problema XOR

- **Éxito en resolución:** La red aprende correctamente la función XOR
- **Arquitectura mínima:** Solo 2 neuronas ocultas son suficientes
- **Comprensión de pesos:** Análisis detallado de cómo la red transforma el espacio de entrada

## 🚀 Ejecución

```bash
# Instalar dependencias
pip install tensorflow numpy matplotlib

# Ejecutar notebooks
cd notebooks
jupyter notebook S5_DL_practice1_XOR.ipynb
jupyter notebook S5_DL_practice1_FasMNIST.ipynb
```

## 📝 Notas

### Problema XOR
- Es un ejemplo clásico que demuestra la necesidad de capas ocultas
- Un perceptrón simple no puede resolver XOR (problema no linealmente separable)
- Las redes multicapa pueden aprender funciones no lineales mediante transformaciones del espacio

### Fashion MNIST
- Más complejo que MNIST tradicional (dígitos)
- Requiere técnicas de normalización para obtener buenos resultados
- Los callbacks son fundamentales para optimizar el entrenamiento
- La normalización N(0,1) es crucial para la convergencia estable

### Técnicas Aprendidas
- Normalización de datos: Escalado, centrado y estandarización
- Optimización de learning rate: Balance entre velocidad y estabilidad
- Callbacks: Ajuste automático de hiperparámetros durante el entrenamiento
- Análisis de arquitecturas: Comprensión de cómo las capas transforman los datos

