import pandas as pd
import numpy as np

datos_Original = pd.read_csv("Datoscompletos.csv", delimiter='#',header=0)
datos_uicn = pd.read_csv("uicn.csv", delimiter=';',header=0)
datos_familia = pd.read_csv("familia.csv", delimiter=',',header=0)

dOri=pd.DataFrame(datos_Original)
dUicn=pd.DataFrame(datos_uicn)
dFamilia=pd.DataFrame(datos_familia)

#metodo para sacar las columnas
def colum(dOri):
    list=[]
    for column, values in dOri.iteritems():
        list.append(column)

    return list

#columOri = colum(dOri)
#columUicn = colum(dUicn)
#columFamil = colum(dFamilia)
filasUic= len(dUicn)
filasOri=len(dOri)
filasfamili=len(dFamilia)
print filasUic
print filasOri
#print "fuera: ",dOri.loc[3,'UICN']
#print "fuera1: ",dUicn.loc[2,'uicn']
for value in range(filasUic):
    for value1 in range(filasOri):
        #print value1

        if dOri.loc[value1,'UICN'] == dUicn.loc[value,'uicn']:
            #print "valor: ", dOri.loc[value1,'UICN']
            dOri.loc[value1,'UICN']= dUicn.loc[value,'id']
            #print "modificado: ",dOri.loc[value1,'UICN']
print value
print value1

for value in range(filasfamili):
    for value1 in range(filasOri):
        #print value1

        if dOri.loc[value1,'Family'] == dFamilia.loc[value,'nombre']:
            #print "valor: ", dOri.loc[value1,'Family']
            dOri.loc[value1,'Family']= dFamilia.loc[value,'id']
            #print "modificado: ",dOri.loc[value1,'Family']

cus=dOri['Codigo especie']
cus1=dOri['Family']
cus2=dOri['Species']
cus3=dOri['Name']
cus4=dOri['Synonim']
cus5=dOri['UICN']
cus6=dOri['Endemismo']
cus7=dOri['Migracion']

#print cus
df=pd.DataFrame()
df.insert(0, 'Codigo Especie', cus)
df.insert(1, 'Familia',cus1)
df.insert(2,'especie',cus2)
df.insert(3, 'nombre',cus3)
df.insert(4, 'sinonimo',cus4)
df.insert(5, 'uicn',cus5)
df.insert(6, 'endemismo',cus6)
df.insert(7, 'migracion',cus7)



dfc= colum(df)
df['uicn'] = df['uicn'].replace(np.nan, 0)

for value in range(len(dfc)):

 #es para recorrer las filas que tiene
    df[dfc[value]] = df[dfc[value]].replace(np.nan, 444)
    for value1 in range(len(df)):

        if   df.loc[value1,dfc[value]] == '-' or df.loc[value1,dfc[value]] == 444:
            print "original",df.loc[value1,dfc[value]]
            df.loc[value1,dfc[value]]='null'
            print "modificado",df.loc[value1,dfc[value]]

df.to_csv('Especies2.csv',sep=',')
