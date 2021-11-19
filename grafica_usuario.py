import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import seaborn as sns
from datetime import datetime
from seaborn import colors
cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="45237823", database="data")

def Da_Ti(N_1a,N_1b):
    cur = cnn.cursor()
    sql = "SELECT Time FROM Data.polar where N > {} AND N < {} ".format(N_1a,N_1b)
    cur.execute(sql)
    datos = cur.fetchall()
    cur.close()  
    return datos
def Da_po(N_1a,N_1b):
    cur = cnn.cursor()
    sql = "SELECT Value FROM Data.polar where N > {} AND N < {} ".format(N_1a,N_1b)
    cur.execute(sql)
    datos = cur.fetchall()
    cur.close()  
    return datos
def Da_myo(N_1a,N_1b):
    cur = cnn.cursor()
    sql = "SELECT Max FROM Data.myoware where N > {} AND N < {} ".format(N_1a,N_1b)
    cur.execute(sql)
    datos = cur.fetchall()
    cur.close()  
    return datos
def dataPo(a,b):
    das=Da_po(a,b)
    for n in range(29):
       das[n]=das[n][0]
    return das
def dataMy(a,b):
    das=Da_myo(a,b)
    for n in range(29):
       das[n]=das[n][0]
    return das
def dataTi(a,b):
    das=Da_Ti(a,b)
    for n in range(29):
       das[n]=das[n][0]
    return das

datos=[]
levels= []         
p=15543
for i in range(7):
    x=p+i*30
    levels.append(x)
dfp=[]
num=int(len(levels)-1)
for t in range(6):
    dfp.append(dataTi(levels[t],levels[t+1]))
datos.append(dfp)
dfp=[]
for t in range(6):
    dfp.append(dataPo(levels[t],levels[t+1]))

#dat1=pd.DataFrame(dfp)
#dat1f=dat1.transpose()
datos.append(dfp)
m=8353
levels= [] 
for i in range(7):
    x=m+i*30
    levels.append(x)
dfp=[]
num=int(len(levels)-1)
for t in range(6):
    dfp.append(dataMy(levels[t],levels[t+1]))

#datm=pd.DataFrame(dfp)
#datmf=datm.transpose()
datos.append(dfp)

E0,E1,E2,E3,E4,E5,E6 = [],[],[],[],[],[],[]
E0.append(datos[0][0])
E0.append(datos[1][0])
E0.append(datos[2][0])

E1.append(datos[0][1])
E1.append(datos[1][1])
E1.append(datos[2][1])

E2.append(datos[0][2])
E2.append(datos[1][2])
E2.append(datos[2][2])

E3.append(datos[0][3])
E3.append(datos[1][3])
E3.append(datos[2][3])

E4.append(datos[0][4])
E4.append(datos[1][4])
E4.append(datos[2][4])

E5.append(datos[0][5])
E5.append(datos[1][5])
E5.append(datos[2][5])



ig, axs = plt.subplots(2, 1)
plt.suptitle("Escenario 6",fontsize=25)
axs[0].plot(E5[0], E5[1],'r')
axs[0].set_ylabel('Pulso')
axs[0].grid(True)
axs[1].plot(E5[0], E5[2])
axs[0].set_xticks([])
axs[1].set_ylabel('Respuesta Muscular')
axs[1].grid(True)
axs[1].set_xlabel('Tiempo')
plt.xticks(rotation='vertical')
plt.show()
