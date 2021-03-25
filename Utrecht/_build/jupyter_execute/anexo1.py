import pandas as pd

# Anexo 1: Creación y exportación Dicom

## Introducción

Como proyecto paralelo a la reconstrucción completamente automática y utilizando la herramienta de [anotación](capitulo:anotation) que hemos desarrollado, podemos utilizar el resultado que proporciona la herramienta para hacer un uso clínico del mismo, es decir, incorporar la reconstrucción realizada al flujo de trabajo. Para ello vamos a investigar la estrura de los ficheros dicom de imágenes y ejemplos de exportación del plan para generar uno que pueda ser importado en Oncentra con la reconstrucción ya hecha.

## Tags comunes entre imágenes y plan: 

Hay 23 tags comunes entre un fichero de secuencia de imágenes y uno tipo RTPlan. De ellos, 14 poseen el mismo valor y por lo tanto el mismo viene definido de la MRI. La lista es:

<ul><li>AccessionNumber</li><li>FrameOfReferenceUID</li><li>PatientBirthDate</li><li>PatientID</li><li>PatientName</li><li>PatientSex</li><li>PositionReferenceIndicator</li><li>ReferringPhysicianName</li><li>SpecificCharacterSet</li><li>StudyDate</li><li>StudyDescription</li><li>StudyID</li><li>StudyInstanceUID</li><li>StudyTime</li></ul>

### Tags de diferente valor

Los 9 que nos quedan son:

<ul><li>Manufacturer</li><li>ManufacturerModelName</li><li>Modality</li><li>SOPClassUID</li><li>SOPInstanceUID</li><li>SeriesInstanceUID</li><li>SeriesNumber</li><li>SoftwareVersions</li><li>StationName</li></ul>

campos=pd.read_csv('data/camposnocomunes.csv')
campos.set_index('tag')

Hay una serie de ellos que no nos van a suponer ningún problema. No obstante detengámonos en cada uno de ellos

#### Manufacter y ManufacturerModelName

Podemos poner en ambos el nombre que queramos por ejemplo **IRIMED** y **UtrechtTool**

#### Modality

Esta debe ser obligatoriamente **RTPlan**

#### SeriesNumber

En esta pondremos **1**

#### SoftwareVersion y StationName

De momento pondremos **1.0** para la primera y **3DSlicer** para la segunda.

Ahora entramos en los campos no tan evidentes

#### SOPClassUID

Por lo que vemos en los diferentes planes, este valor es común. Así que lo mantendremos en nuestro RTPlan fabricado: **1.2.840.10008.5.1.4.1.1.481.5**

