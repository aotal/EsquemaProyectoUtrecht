Planteamiento del problema
=======================

## Datos de entrada y objetos de salida

La entrada del problema  es una MRI y la información sobre la configuración del aplicador Utrecht, es decir, para la parte intracavitaria tipo de ovoides izquierdo y derecho (OV) y sonda intrauterina (IU) y para la parte intersticial agujas implantadas y profundidad de inserción de cada una. La salida es la transformación afín (TA) del cambio de base de la MRI y el aplicador por una parte y el ángulo formado por los ovoides, normalmente muy pequeño, así como de la IU respecto del aplicador. Para la parte intersticial, apoyándose en a información de la parte intracavitaria, la trayectoria de cada una de las agujas y la determinación de la punta.

```{figure} https://www.uv.es/radiofisica/images/Utrecht.png
---
scale: 100%
align: center
---
Modelo 3D del aplicador Utrecht con parte intersticial
```

## Bloques de trabajo

No pensamos que se pueda obtener de manera directa las TAs que buscamos. Por lo tanto la estructura de trabajo que a priori contemplamos es la siguiente:

  - **Preparación de datos**: Anotación para el entrenamiento de la red neuronal.
  - **Segmentación del aplicador**
  - **Posicionamiento del aplicador**: Con los datos de la segmentación y por métodos de registro rígido de estructuras tridimensionales obtener las transformaciones buscadas.
