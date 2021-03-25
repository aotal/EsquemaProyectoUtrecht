import pydicom as dc

import pandas as pd

plansimple=dc.read_file('Ficheros/PlanSimple.dcm')
plancomplejo=dc.read_file('Ficheros/PlanComplejo.dcm')
plancomplejo2=dc.read_file('Ficheros/PlanComplejo2.dcm')

imagen=dc.read_file('Ficheros/MR1.3.6.1.4.1.2452.6.1019122476.1241727211.1770477973.3491608041.dcm')
estructura=dc.read_file('Ficheros/EstructuraSimple.dcm')



plansimple.ReferencedStructureSetSequence[0]

planlist=plansimple.dir()
planlist2=plancomplejo.dir()
imagenlist=imagen.dir()

len(common)

len(samevalues)

common=[]
noncommon=[]
for x in planlist:
    if x in imagenlist:
        common.append(x)
    else:
        noncommon.append(x)

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

make_markdown_table(differentvalue)

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

