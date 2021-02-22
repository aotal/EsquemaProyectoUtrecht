# Identificación del aplicador sobre MRI: Segmentación del aplicador 

## Plataformas

Como recien llegados al mundo del deep learning, no tenemos todavía claro qué librería usar. Por lo que hemos visto las predominantes son [Tensorflow](https://www.tensorflow.org/) y [Pytorch](https://pytorch.org/). Por otra parte sabemos de la existencia de la plataforma de NVIDIA llamada [Clara](https://developer.nvidia.com/clara) que está pensada para uso médico y que puede integrar a las dos anteriores. 

## Candidatas

Revisando los modelos de segmentación mediante redes neuronales convolucionales (CNN), pensamos que las topologías de red adecuadas serían U-net{cite}`DBLP:journals/corr/RonnebergerFB15` o su equivalente en 3D V-net{cite}`7785132`

```{figure} https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/u-net-architecture.png
---
scale: 25%
align: center
---
Esquema de la topología de red U-net
```

En una búsqueda de internet rápida se ve que los dos modelos están implementados tanto en Tensorflow como en Pytorch.

## Hardware

Está claro que para la fase de entrenamiento un hardware potente que permita la paralelización del cálculo es la clave para reducir el tiempo de entrenamiento, pero de momento no lo hemos dimensionado. El uso de más de una GPU parece que no es opcional.

