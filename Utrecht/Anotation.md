# Herramienta de anotación

## Motivo

El desarrollo de una herramienta específica de anotación es necesaria debido a que a diferencia de la segmentación de órganos de riesgo y/o tumores que hacemos para entrenar una red neuronal que identifica estructuras anatómicas, en este caso lo que queremos identificar sobre la imágen es un objeto del que tenemos información detallada de su morfología. Dentro de el conjunto de herramientas del planificador de tratamiento (TPS), existe una que nos permite posicionar los aplicadores pero al ser un software propietario extraer información para su posterior uso es complicado. Por este y otros motivos de limitaciones de dicha herramienta, nos decidimos a diseñar una nueva más a medida de nuestras necesidades.   

## Diferencias con con la segmentación habitual.

En un módulo de segmentación anatómica, un experto delimita la estructura corte a corte o se ayuda de herramientas de AI pre-entrenadas. Por el contrario, para la segmentación de un aplicador, colocamos el mismo sobre la secuencia de imágenes.     
