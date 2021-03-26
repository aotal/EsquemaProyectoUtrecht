import pandas as pd
from myst_nb import glue
import pydicom as dc

import uuid
from datetime import datetime
import pytz

estructura=dc.read_file('Ficheros/EstructuraSimple.dcm')
plansimple=dc.read_file('Ficheros/PlanSimple.dcm')
plancomplejo2=dc.read_file('Ficheros/PlanComplejo2.dcm')

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
La función que nos da el valor del tag se muestra a continuación

def DiferenciaUTC(X='Europe/Madrid'):
    delta=pytz.timezone(X).utcoffset(datetime.today())
    delta=delta.days*24+delta.seconds//3600
    return "{:=+03d}00".format(delta)

DiferenciaUTC()

DiferenciaUTC('US/Pacific')

### Tags sequence

La lista de tags de secuencia son los siguientes

<ul><li>FractionGroupSequence</li><li>ReferencedStructureSetSequence</li><li>SourceSequence</li><li>TreatmentMachineSequence</li><li>ApplicationSetupSequence</li></ul>

Salvo que se diga lo contrario siempre nos referiremos a la posición 0 de la secuencia

#### FractionGroupSequence
Dejaremos el siguiente tag por defecto

print(plansimple.data_element('FractionGroupSequence').value[0])

#### ReferencedStructureSetSequence
El aspecto del tag es el siguiente:

print(plansimple.data_element('ReferencedStructureSetSequence').value[0])

Simplemente debemos localizar en el fichero de estructuras los campos SOPClassUID y SOPInstanceUID e incorporar esos valores a los sub tags. 

#### SourceSequence
Esta secuencia tiene el siguiente aspecto:

print(plansimple.data_element('SourceSequence').value[0])

Ignoraremos los private tag data. Para los campos **ReferenceAirKermaRate**,**SourceStrength ReferenceDate** y **SourceStrengthReferenceTime** tenemos dos opciones: O ponemos valores genéricos de fuente, lo más cómodo, o ponemos los valores de la funete que vayamos a utilizar. Lo demás se puede dejar como en el ejemplo 

#### ApplicationSetupSequence
En el ejemplo siguiente los dos primeros tags pueden quedar tal cual.

```
(300a, 0232) Application Setup Type              CS: 'GYNECOLOGY'
(300a, 0234) Application Setup Number            IS: "0"
(300a, 0250) Total Reference Air Kerma           DS: "3315.31795903434"
```

El tercero lo podemos calcular como el cociente entre el campo **ReferenceAirKermaRate** y el tiempo total de radiación expresado en horas que será la suma de los tiempos totales de cada fuente, en nuestro caso 1, y de cada uno de los canales.

Para el ejemplo que nos ocupa el plan se llama plancomplejo2 y los valores que buscamos son:

ReferenceAirKermaRate=plancomplejo2.data_element('SourceSequence').value[0].ReferenceAirKermaRate
Secuencia=plancomplejo2.data_element('ApplicationSetupSequence').value[0]
TiempoTotal=(Secuencia.ChannelSequence[0].ChannelTotalTime+Secuencia.ChannelSequence[1].ChannelTotalTime+Secuencia.ChannelSequence[2].ChannelTotalTime)/3600
TotalReferenceAirKerma=ReferenceAirKermaRate*TiempoTotal
print(TotalReferenceAirKerma)

Que como vemos coincide con lo que había en la cabecera. Con respecto al tiempo total, podemos elegir el tiempo que queramos por posición. Este cálculo lo hacemos para que simplemente sea consistente el fichero.
Por otra parte veamos ahora el aspecto de cada uno de los ChannelSequence

Secuencia.ChannelSequence[0]

Ignoramos como siempre los campos privados. Del tiempo total ya hemos hablado así que lo saltaremos. El **SourceApplicatorLength** lo podemos obtener a posteriori midiendo la distancia entre cada uno de los puntos de parada. Al **FinalCumulativeTimeWeight** le pasa lo mismo que al tiempo, mientras sea consistente no pasa nada. Vamos ahora al **BrachyControlPointSequence**.
Siempre tendrá un número par de elementos, veamos un ejemplo:

Secuencia.ChannelSequence[0].BrachyControlPointSequence[6]

Secuencia.ChannelSequence[0].BrachyControlPointSequence[7]

Los elementos van numerados de manera correlativa por un índice. La posición relativa es un múltiplo del paso de fuente, en este caso 2.5. El **ControlPoint3DPosition** nos vendrá del programa de reconstrucción descrito en el capítulo sobre [anotación](capitulo:anotation). El **CumulativeTimeWeight** al igual que el tiempo lo definiremos consistente con lo que elijamos para cada canal