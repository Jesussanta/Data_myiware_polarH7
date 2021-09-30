import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import seaborn as sns
from datetime import datetime

from seaborn import colors
Name="m1"
cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="45237823", database="data")

def Da_po(N_1a,N_1b):
    cur = cnn.cursor()
    sql = "SELECT Value FROM Data.polar where N > {} AND N < {} ".format(N_1a,N_1b)
    cur.execute(sql)
    datos = cur.fetchall()
    cur.close()  
    return datos
def Da_my(N_1a,N_1b):
    cur = cnn.cursor()
    sql = "SELECT * FROM Data.myoware WHERE Name = '{}' AND N > {} AND N < {} ".format(Name,N_1a,N_1b)
    cur.execute(sql)
    datos = cur.fetchall()
    cur.close()  
    return datos
def get_n(num):
    cur = cnn.cursor()
    sql= "SELECT N FROM Data.polar where Time = '{}';".format(str(num))
    cur.execute(sql)
    datos = cur.fetchall()
    cur.close()  
    return datos
def dataPo(a,b):
    das=Da_po(a,b)
    for n in range(29):
       das[n]=das[n][0]
    return das

gP=[2484,4491,9876,12831,5492,5802,8862,2839]        #PrimaDar / johana / AmigaL / OrdoIsa     #David / Cuy / DaniLa / HCamila
#gB=[12435,12915,14554,15543,12696,13542,13790,15169]
datos=[]
datos2=[]

for r in range(len(gP)):
    levels= []          #Mujeres 1
    z=gP[r]
    for i in range(7):
        x=z+i*30
        levels.append(x)
    dfp=[]
    num=int(len(levels)-1)
    for t in range(6):
        dfp.append(dataPo(levels[t],levels[t+1]))
    dat1=pd.DataFrame(dfp)
    dat1f=dat1.transpose()
    datos.append(dat1f)
    #dat1.describe()
sum_da=[]
for f in range (len(datos)):
    da=datos[f].mean()
    da=np.argsort(da)
    sum_da.append(da)
sums=pd.DataFrame(sum_da)
print(sums.head(10))
dat=[]
for r in range(6):
  dat.append(sums[r][0]+sums[r][1]+sums[r][2]+sums[r][3]+sums[r][4]+sums[r][5]+sums[r][6]+sums[r][7])
dat1=pd.DataFrame(dat)

#ax = plt.axes()
#sns.heatmap(dat1, center=0, cmap='PuBu', annot=True, )
#jet
#plt.title('Heatmap of Flighr Dataset', fontsize = 20)
#plt.show()
#plt.plot(dat1)
#plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Grupo P', fontsize = 20)#PuBu
sns.heatmap(dat1, center=0, cmap='PuBu', annot=True, )
ax1.plot(dat1)
plt.show()

dble=[]
dble2=[]
for f in range (len(datos)-4):
    dble.append(datos[f].mean())

for f in range (len(datos)-4):
    dble2.append(datos[f+4].mean())

db1=pd.DataFrame(dble)
db2=pd.DataFrame(dble2)
print(db1.transpose())
print(db2.transpose())
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Grupo P \n Mujer / Hombre ', fontsize = 20)
ax1.plot(db1.transpose())
ax2.plot(db2.transpose())
plt.show()

fig, ((b1,b2),(b3,b4),(b5,b6)) = plt.subplots(3, 2)
fig.suptitle('Ambientes \nMujer 2', fontsize = 20)
b1.plot(datos[1][0],color='b')
b2.plot(datos[1][1],color='g')
b3.plot(datos[1][2],color='r')
b4.plot(datos[1][3],color='c')
b5.plot(datos[1][4],color='m')
b6.plot(datos[1][5],color='k')
plt.show()



