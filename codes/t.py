import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
from datetime import datetime
Name="m1"
cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="45237823", database="Data")

def Da_po(N_1a,N_1b):
    cur = cnn.cursor()
    sql = "SELECT * FROM Data.polar WHERE Name = '{}' AND N > {} AND N < {} ".format(Name,N_1a,N_1b)
    
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
    sql= "SELECT * FROM Data.polar where Time = '{}';".format(num)
    cur.execute(sql)
    datos = cur.fetchone()
    cur.close()    
    return datos



N_1a=2546
N_1b=2576
datos=Da_po(N_1a,N_1b)
df_p1 = pd.DataFrame(data=datos)
df_p1.columns = ['ID','Name','Time','RPM']

N_1c=1448
N_1d=1482       

#N_1a=2192
#N_1b=2223
#N_1c=1276
#N_1d=1307

datos2=Da_my(N_1c,N_1d)
df_m1 = pd.DataFrame(data=datos2)
df_m1.columns = ['ID','Name','Time','Min','Max']

print(len(df_m1))
print(df_m1.describe())

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Piloto')

ax1.plot(df_m1["Time"],df_m1["Min"], 'o-')
ax1.plot(df_m1["Time"],df_m1["Max"], 'o-')
ax1.set_ylabel('Myoware')


ax2.plot(df_p1["Time"], df_p1["RPM"], '.-')
ax2.set_xlabel('time')
ax2.set_ylabel('Polar')
plt.xticks(rotation='vertical')

plt.show()