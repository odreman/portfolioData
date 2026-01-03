# Clasificación de Imágenes con CNN

## 📋 Descripción

Serie de proyectos que progresan desde la construcción de una CNN básica hasta técnicas avanzadas de optimización para clasificación de imágenes (perros vs gatos). Cada notebook aborda diferentes aspectos de la construcción y optimización de redes neuronales convolucionales.

## 🎯 Objetivos

1. **CNN desde cero:** Construir una red convolucional básica
2. **Reducción de sobreentrenamiento:** Implementar data augmentation y dropout
3. **Transfer learning:** Utilizar modelos pre-entrenados
4. **Optimización avanzada:** Fine-tuning y técnicas avanzadas

## 📚 Notebooks

### 1. CNN desde cero (`01_cnn_template.ipynb`)
Construcción de una CNN básica para clasificación binaria de imágenes.

### 2. Reducción de sobreentrenamiento (`02_cnn_template.ipynb`)
Implementación de data augmentation y dropout para mejorar la generalización.

### 3. Transfer Learning (`03_cnn_template.ipynb`)
Uso de modelos pre-entrenados (VGG, ResNet, Inception V3, etc.) para mejorar el rendimiento. Incluye explicación detallada de la arquitectura Inception V3 y su aplicación a diferentes dominios.

### 4. Optimización avanzada (`04_cnn_template_.ipynb`)
Aplicación de Inception V3 a clasificación de flores, demostrando la versatilidad del transfer learning. Comparación de resultados con y sin Inception V3.

## 🔧 Tecnologías Utilizadas

- **TensorFlow/Keras:** Framework principal
- **CNN:** Redes neuronales convolucionales
- **Transfer Learning:** Modelos pre-entrenados (VGG, ResNet, etc.)
- **Data Augmentation:** Transformaciones de imágenes
- **OpenCV/PIL:** Procesamiento de imágenes

## 📊 Datasets

### Dogs vs Cats
- **Dataset:** 2,000 imágenes de perros y gatos
- **División:** Train/Validation
- **Preprocesamiento:** Redimensionamiento a 150x150, normalización
- **Uso:** Notebooks 1-3

### Clasificación de Flores
- **Dataset:** Base de datos de flores (múltiples clases)
- **División:** Train/Validation
- **Preprocesamiento:** Redimensionamiento, normalización
- **Uso:** Notebook 4 (comparación CNN propia vs Inception V3)

## 🏗️ Arquitecturas

- CNN personalizada (capas convolucionales, pooling, dense)
- Modelos pre-entrenados (VGG16, ResNet50, etc.)
- Fine-tuning de capas finales

## 📈 Técnicas Implementadas

### Data Augmentation

El proyecto implementa data augmentation exhaustivo para mejorar la generalización del modelo. Las transformaciones aplicadas incluyen:

- **rotation_range=40:** Rotación aleatoria de ±40 grados para reconocer objetos en diferentes orientaciones
- **width_shift_range=0.2:** Desplazamiento horizontal hasta 20% del ancho para simular cambios de posición lateral
- **height_shift_range=0.2:** Desplazamiento vertical hasta 20% de la altura para generalizar ante cambios de posición vertical
- **shear_range=0.2:** Transformación de cizalladura diagonal para robustez ante distorsiones
- **zoom_range=0.2:** Zoom aleatorio de ±20% para reconocer objetos a diferentes escalas
- **horizontal_flip=True:** Volteo horizontal aleatorio (imágenes en espejo)
- **fill_mode='nearest':** Relleno de espacios vacíos copiando el píxel más cercano

Estas transformaciones aseguran que el modelo nunca vea la misma imagen dos veces durante el entrenamiento, aumentando la variabilidad y fortaleciendo la capacidad de generalización.

### Dropout - Experimentación Sistemática

Se realizó una experimentación exhaustiva con diferentes valores de dropout para encontrar el equilibrio óptimo:

| Dropout | Train Accuracy | Val Accuracy | Train Loss | Val Loss | Diferencia Train-Val |
|---------|----------------|--------------|------------|----------|----------------------|
| **0.5** | 0.7480 | **0.7840** ⭐ | 0.5069 | **0.4771** | 0.0360 |
| 0.3 | 0.7590 | 0.7630 | 0.5085 | 0.4791 | 0.0040 |
| 0.7 | 0.7550 | 0.7610 | 0.5114 | 0.5101 | 0.0060 |
| 0.1 | 0.7455 | 0.7730 | 0.5144 | 0.4807 | 0.0275 |
| 0.9 | 0.7010 | 0.7520 | 0.5849 | 0.5257 | 0.0510 |

**Hallazgos:**
- **Dropout 0.5 fue seleccionado** como el valor óptimo, ofreciendo el mejor equilibrio entre evitar sobreajuste y mantener capacidad de aprendizaje
- Valores intermedios (0.3-0.7) ofrecen mejor equilibrio que extremos
- Dropout muy alto (0.9) limita demasiado el aprendizaje (underfitting)
- Dropout muy bajo (0.1) puede llevar a sobreajuste, aunque en este caso la diferencia fue pequeña

### Transfer Learning con Inception V3

El proyecto implementa transfer learning utilizando **Inception V3**, una arquitectura de red convolucional profunda.

**Características de Inception V3:**
- **Módulos Inception:** Utiliza múltiples tamaños de filtros (1x1, 3x3, 5x5) en el mismo bloque para capturar patrones a diferentes escalas
- **Técnicas de optimización:**
  - Convoluciones 1x1 para reducir dimensiones
  - Factorización de convoluciones (5x5 → dos 3x3)
  - Average Pooling y Batch Normalization
  - Auxiliary classifiers para mejorar flujo de gradientes
- **Entrenamiento:** Pre-entrenado en ImageNet (1+ millón de imágenes, 1000 clases) usando GPUs, data augmentation y SGD con regularización

**Aplicación a diferentes dominios:**
- Aunque entrenado en imágenes de 299x299, funciona con 150x150 gracias a que las convoluciones trabajan por zonas locales
- Se aplicó exitosamente a clasificación de flores, demostrando su versatilidad

**Resultados con Inception V3 (clasificación de flores):**
- **Sin Inception V3:** Accuracy de validación ~0.70 (70%) con mayor variabilidad e inestabilidad
- **Con Inception V3:** Accuracy de validación 0.74-0.76 (74-76%) con mayor estabilidad y menos overfitting
- **Conclusión:** Inception V3 proporciona un salto claro de rendimiento incluso con pocos datos, gracias a los pesos pre-entrenados y la arquitectura profunda

### Otras Técnicas

- Transfer learning con otros modelos (VGG16, ResNet50)
- Fine-tuning de capas finales
- Early stopping
- Callbacks de Keras

## 🚀 Ejecución

```bash
# Instalar dependencias
pip install tensorflow opencv-python pillow numpy matplotlib

# Ejecutar notebooks
jupyter notebook 01_cnn_template.ipynb
```

## 🎯 Resultados Clave

### Regularización (Notebook 2)
- **Mejor dropout:** 0.5 (val accuracy: 0.7840)
- Data augmentation reduce significativamente el sobreajuste
- Valores intermedios de dropout (0.3-0.7) ofrecen mejor equilibrio

### Transfer Learning (Notebooks 3-4)
- **Inception V3** mejora significativamente el rendimiento
- Aplicable a diferentes dominios (perros/gatos → flores)
- Funciona con diferentes tamaños de imagen (299x299 → 150x150)
- Mejora de ~70% a ~74-76% en clasificación de flores

## 📝 Notas

- Se recomienda usar GPU para entrenamiento (especialmente con Inception V3)
- Los datos se descargan automáticamente
- Los modelos pueden guardarse para reutilización
- Inception V3 requiere descarga de pesos pre-entrenados (automático con Keras)

