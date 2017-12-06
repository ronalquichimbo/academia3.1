import pandas  as pd
import numpy as np

datos= pd.read_csv("db-aves-lista.csv", delimiter= '#',header=0)
#order= pd.read_csv("db-aves-list.csv",header=0,usecols=['ID'])
#ver la informacion de cada atributo
#print  "---------------Objetos que tiene el csv---------------\n",(datos.info())
# ver los 5  datos
#columna=datos1.dtypes
print  "---------------Objetos que tiene el csv---------------\n",(len(datos))




# ver los datos de las columnas
#print  "----------------------Columnas-----------------\n",(datos.iloc[:,1])

#print  "------------------------order-------------------------\n",(datos['Order/Clade'])
df=pd.DataFrame(datos)


#df['Year of collection'] = df['Year of collection'].replace(np.nan, 0)
#df.loc[0,'ID']=2
#print "---------------------datos---------------------\n", df.loc[22243,'ID']
#print "---------------------Codigo---------------------\n", df.loc[22243,'Codigo especie']
#print "---------------------Especie---------------------\n", df.loc[22243,'Species']

list=[]
for column, values in df.iteritems():
    list.append(column)
    #print column
    #print "original: ",df.loc[i,column]
    #if df.loc[i,column]=='':
    #    print "original: ",df.loc[i,column]
    #    df.loc[i,column]='null'
    #    print "cambiada: ", df.loc[i,column]


#aqui grabo la longuitud que tiene nuestas columnas
columna= len(list)
#aqui grabo la longuitud de nuestas filas
filas= len(df)
print "filas",filas
##este  for es para recorrer las columnas que tiene

for value in range(columna):
## es para recorrer las filas que tiene
    df[list[value]] = df[list[value]].replace(np.nan, 0)
    for value1 in range(filas):

        if   df.loc[value1,list[value]] == '-' or df.loc[value1,list[value]] == 0:
            print "original",df.loc[value1,list[value]]
            df.loc[value1,list[value]]='null'
            print "modificado",df.loc[value1,list[value]]

print df.loc[6718,'Year of collection']
print len(df)
df.to_csv('Datoscompletos.csv',sep='#')
    #print "value", values
    #print "valu",list(values)
