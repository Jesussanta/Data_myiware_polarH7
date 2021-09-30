import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import seaborn as sns
from datetime import datetime
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

       #PrimaDar / johana / AmigaL / OrdoIsa     #David / Cuy / DaniLa / HCamila
gP=[12435,12915,14554,15543,12696,13790,15169,13542]
datos=[]


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
    #print(dat1f.describe())
    
sum_da=[]
for f in range (len(datos)):
    da=datos[f].mean()
    da=np.argsort(da)
    sum_da.append(da)
sums=pd.DataFrame(sum_da)
#print(sums.head(10))
dat=[]
for r in range(6):
    dat.append(sums[r][0]+sums[r][1]+sums[r][2]+sums[r][3]+sums[r][4]+sums[r][5]+sums[r][6]+sums[r][7])
'''''
dat[0]=18
dat[1]=17
dat[3]=dat[3]
dat[2]=dat[2]+4
dat[5]=dat[5]+4
dat[4]=dat[4]+1+2

print(dat)

'''
dat1=pd.DataFrame(dat)
sns.heatmap(dat1, center=0, cmap='icefire_r', annot=True, )
plt.show()
plt.plot(dat1)
plt.show()

