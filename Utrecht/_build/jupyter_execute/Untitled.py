import pydicom as dc

import pandas as pd
from datetime import datetime
import numpy as np

plansimple=dc.read_file('Ficheros/PlanSimple.dcm')
plancomplejo=dc.read_file('Ficheros/PlanComplejo.dcm')
plancomplejo2=dc.read_file('Ficheros/PlanComplejo2.dcm')

imagen=dc.read_file('Ficheros/MR1.3.6.1.4.1.2452.6.1019122476.1241727211.1770477973.3491608041.dcm')
estructura=dc.read_file('Ficheros/EstructuraSimple.dcm')

len(plansimple.data_element('SOPInstanceUID').value)

len(plancomplejo.data_element('SOPInstanceUID').value)

len(plancomplejo2.data_element('SOPInstanceUID').value)

len(plansimple.data_element('SeriesInstanceUID').value)

len(plancomplejo.data_element('SeriesInstanceUID').value)

len(plancomplejo2.data_element('SeriesInstanceUID').value)

datetime.strptime('2020-03-22', '%y-%m-%d')

datetime.strptime()

datetimeobject = datetime.strptime('20200302120000','%Y%m%d%H%M%S')

datetimeobject

%H%M%S

plansimple.ReferencedStructureSetSequence[0]

planlist=plansimple.dir()
planlist2=plancomplejo.dir()
imagenlist=imagen.dir()

common=[]
noncommon=[]
for x in planlist:
    if x in imagenlist:
        common.append(x)
    else:
        noncommon.append(x)

noncommon

def make_markdown_table(array):

    """ Input: Python list with rows of table as lists
               First element as header. 
        Output: String to put into a .md file 
        
    Ex Input: 
        [["Name", "Age", "Height"],
         ["Jake", 20, 5'10],
         ["Mary", 21, 5'7]] 
    """
    markdown="<ul>"
    for e in array:
        markdown += '<li>' + str(e)+'</li>'
        #markdown +=" <br> "
    markdown+='</ul>'
    return markdown

make_markdown_table(noncommon)

samevalues=[]
differentvalue=[]
for x in common:
    if (plansimple.data_element(x).value==imagen.data_element(x).value):
        samevalues.append(x)
    else:
        differentvalue.append(x)

samevalues

differentvalue

A=pd.DataFrame([[x,plansimple.data_element(x).value,plancomplejo.data_element(x).value,plancomplejo2.data_element(x).value,imagen.data_element(x).value] for x in differentvalue],columns=['tag','Plan1','Plan2','Plan3','Imagen'])

A.columns.tolist()

A.set_index('tag')

A.to_csv('camposnocomunes.csv',columns=A.columns.tolist(),index=False)

plan.data_element('AccessionNumber').value

plan.AccessionNumber



imagen.dir()

plansimple.data_element('InstanceCreationDate').value

plansimple.data_element('SOPInstanceUID').value

print(plansimple.data_element('FractionGroupSequence').value[0])

plancomplejo2.RTPlanDate

plancomplejo2.RTPlanTime

plancomplejo2.SourceSequence[0].SourceStrengthReferenceDate

plancomplejo2.SourceSequence[0].SourceStrengthReferenceTime

datetimeobject = datetime.strptime('20200302120000','%Y%m%d%H%M%S')

fecha=lambda x,y:datetime.strptime(x+y,'%Y%m%d%H%M%S')

fechacal=fecha(plancomplejo2.SourceSequence[0].SourceStrengthReferenceDate,plancomplejo2.SourceSequence[0].SourceStrengthReferenceTime)
fechatrat=fecha(plancomplejo2.RTPlanDate,plancomplejo2.RTPlanTime)

delta=fechatrat-fechacal

plancomplejo2.data_element('SourceSequence').value[0].ReferenceAirKermaRate

Secuencia.TotalReferenceAirKerma

np.exp(-np.log(2)*delta.seconds/3600/24/73.81)*5009

AS=plancomplejo2.ReferencedStructureSetSequence

#Secuencia=plancomplejo2.data_element('ApplicationSetupSequence').value[0].ChannelSequence
Secuencia=plancomplejo2.data_element('ApplicationSetupSequence').value[0]

X=Secuencia.ChannelSequence[0].ChannelTotalTime+Secuencia.ChannelSequence[1].ChannelTotalTime+Secuencia.ChannelSequence[2].ChannelTotalTime

plancomplejo2.data_element('SourceSequence').value[0].ReferenceAirKermaRate/3600*X

plancomplejo2.data_element('ApplicationSetupSequence').value[0]

Secuencia.TotalReferenceAirKerma

Secuencia[0].FinalCumulativeTimeWeight+Secuencia[1].FinalCumulativeTimeWeight+Secuencia[2].FinalCumulativeTimeWeight

X=Secuencia[0].ChannelTotalTime+Secuencia[2].ChannelTotalTime+Secuencia[2].ChannelTotalTime

X/3600

26306.824376534/X

Secuencia[0]

plancomplejo2

