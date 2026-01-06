# Generación de Imágenes con DCGAN

Este proyecto implementa Deep Convolutional Generative Adversarial Networks (DCGAN) para generar imágenes sintéticas. Se incluyen experimentos con los datasets MNIST y CIFAR-10, demostrando cómo las GANs pueden aprender a crear imágenes realistas a partir de ruido aleatorio.

## 📋 Objetivos

- Implementar una arquitectura DCGAN completa
- Entrenar modelos generativos en datasets de imágenes
- Generar imágenes sintéticas de dígitos manuscritos (MNIST)
- Generar imágenes sintéticas de objetos naturales (CIFAR-10)
- Visualizar la evolución del generador durante el entrenamiento

## 📝 Descripción

Las Generative Adversarial Networks (GANs) son una de las ideas más interesantes en el campo del deep learning. Se entrenan dos modelos de forma simultánea convirtiéndolos en adversarios: un generador (el artista) aprende a crear imágenes que parezcan reales, mientras un discriminador (el crítico de arte) aprende a distinguir imágenes reales de copias.

Durante el entrenamiento, el generador va mejorando progresivamente en crear imágenes que parecen reales, mientras que el discriminador se hace mejor en distinguirlas. El proceso alcanza un equilibrio cuando el discriminador ya no puede distinguir las imágenes generadas de las reales.

Este proyecto demuestra este proceso en dos datasets diferentes:
- **MNIST**: Dígitos manuscritos (28x28 píxeles en escala de grises)
- **CIFAR-10**: Objetos naturales (32x32 píxeles en color)

## 🛠️ Tecnologías Utilizadas

- **TensorFlow**: Framework de deep learning
- **Keras**: API de alto nivel para construcción de modelos
- **NumPy**: Operaciones numéricas
- **Matplotlib**: Visualización de resultados
- **ImageIO**: Generación de GIFs animados

## 📊 Temas Cubiertos

- Arquitectura DCGAN (Generador y Discriminador)
- Entrenamiento adversarial
- Normalización por lotes (Batch Normalization)
- Optimizadores Adam
- Generación de imágenes a partir de ruido aleatorio
- Visualización de la evolución del entrenamiento
- Guardado y carga de checkpoints

## 📁 Estructura del Proyecto

```
generacion_imagenes_dcgan/
├── dcgan_mnist.ipynb          # Implementación DCGAN para MNIST
├── dcgan_cifar10.ipynb        # Implementación DCGAN para CIFAR-10
├── images/                     # GIFs y visualizaciones
│   ├── dcgan.gif
│   ├── dcgan_cifar.gif
│   └── dcgan fashion.gif
├── training_checkpoints/      # Checkpoints del entrenamiento
└── image_at_epoch_*.png       # Imágenes generadas por época
```

## 📓 Notebooks

- **[DCGAN para MNIST](./dcgan_mnist.ipynb)** - Implementación completa de DCGAN para generar dígitos manuscritos del dataset MNIST
- **[DCGAN para CIFAR-10](./dcgan_cifar10.ipynb)** - Adaptación de DCGAN para generar imágenes de objetos naturales del dataset CIFAR-10

## 🚀 Ejecución

### Requisitos

```bash
pip install tensorflow matplotlib numpy imageio
```

### Uso

1. Abrir el notebook deseado:
   - `dcgan_mnist.ipynb` para dígitos manuscritos
   - `dcgan_cifar10.ipynb` para objetos naturales

2. Ejecutar todas las celdas en orden

3. El entrenamiento generará:
   - Imágenes de muestra durante el entrenamiento
   - GIFs animados mostrando la evolución
   - Checkpoints para reanudar el entrenamiento

## 📈 Resultados

Los modelos entrenados generan imágenes sintéticas que mejoran progresivamente durante el entrenamiento. Las visualizaciones muestran cómo las imágenes comienzan siendo ruido aleatorio y gradualmente adquieren la forma de los objetos objetivo.

## 📝 Notas

- El entrenamiento puede tomar varias horas dependiendo del hardware
- Se recomienda usar GPU para acelerar el proceso
- Los checkpoints permiten reanudar el entrenamiento desde donde se dejó

