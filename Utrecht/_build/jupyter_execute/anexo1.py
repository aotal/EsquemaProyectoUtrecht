import pandas as pd
from myst_nb import glue

import uuid
from datetime import datetime

# Anexo 1: Creación y exportación Dicom

## Introducción

Como proyecto paralelo a la reconstrucción completamente automática y utilizando la herramienta de [anotación](capitulo:anotation) que hemos desarrollado, podemos utilizar el resultado que proporciona la herramienta para hacer un uso clínico del mismo, es decir, incorporar la reconstrucción realizada al flujo de trabajo. Para ello vamos a investigar la estrura de los ficheros dicom de imágenes y ejemplos de exportación del plan para generar uno que pueda ser importado en Oncentra con la reconstrucción ya hecha.

## Tags comunes entre imágenes y plan: 

Hay 23 tags comunes entre un fichero de secuencia de imágenes y uno tipo RTPlan. De ellos, 14 poseen el mismo valor y por lo tanto el mismo viene definido de la MRI. La lista es:

<ul><li>AccessionNumber</li><li>FrameOfReferenceUID</li><li>PatientBirthDate</li><li>PatientID</li><li>PatientName</li><li>PatientSex</li><li>PositionReferenceIndicator</li><li>ReferringPhysicianName</li><li>SpecificCharacterSet</li><li>StudyDate</li><li>StudyDescription</li><li>StudyID</li><li>StudyInstanceUID</li><li>StudyTime</li></ul>

### Tags de diferente valor

Los 9 que nos quedan se muestran en la tabla siguiente con valores ejemplo de tres planes diferentes y de un archivo de imagen:

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

Por lo que vemos en los diferentes planes, este valor es común. EL valor **1.2.840.10008.5.1.4.1.1.481.5** corresponde a un _Radiation Therapy Plan Storage_.

#### SOPInstanceUID y SeriesInstanceUID

En el caso de estos dos valores las cosas no están tan claras. Parece que poseeen el mismo prefijo que sus equivalentes en el fichero de imagen. La segunda parte corresponde a un número aleatorio de entre 39 y 40 cifras separado en grupos de 10 por puntos. Así pues los generamos con el siguiente código:

prefix='1.3.6.1.4.1.2452.6.'
def UIDgenerator(prefix):
    while True:
        uid=str(uuid.uuid4().int)
        if (len(uid)>=39):
             return prefix+uid[0:10]+'.'+uid[10:20]+'.'+uid[20:30]+'.'+uid[30:]
UIDgenerator(prefix)

## Tags no comunes

### Tags no sequence

<ul><li>ApprovalStatus</li><li>BrachyTreatmentTechnique</li><li>BrachyTreatmentType</li><li>InstanceCreationDate</li><li>InstanceCreationTime</li><li>InstitutionalDepartmentName</li><li>OperatorsName</li><li>RTPlanDate</li><li>RTPlanGeometry</li><li>RTPlanLabel</li><li>RTPlanName</li><li>RTPlanTime</li><li>TimezoneOffsetFromUTC</li></ul>

#### ApprovalStatus

El valor será **UNAPPROVED**

#### BrachyTreatmentTechnique

Pondremos valor **INTERSTITIAL**

#### BrachyTreatmentType
El valor es **HDR**

#### InstanceCreationDate y InstanceCreationTime
Fecha del día de la creación del plan en formato AAAAMMDD y la hora HHMMSS

Hoy=datetime.today()
print(Hoy.strftime("%Y%m%d"),Hoy.strftime("%H%M%S"))

#### OperatorsName

Cuanquiera. **Plan** por ejemplo.

#### RTPlanDate

La misma que **InstanceCreationTime**

#### RTPlanGeometry
El valor es **PATIENT**

#### RTPlanLabel y RTPlanName
Por ejemplo **IRIMED** en ambos

#### RTPlanTime
El mismo valor que InstanceCreationTime

#### TimezoneOffsetFromUTC
Habrá que verificar el horario en ese momento. No creemos que sea importante ya que no influye en la reconstrucción