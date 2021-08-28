import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
from datetime import datetime
Name="Karla"
cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="45237823", database="Data")
#SELECT * FROM Data.polar where Name = 'Karla' and N > 160;
cur = cnn.cursor()
sql = "SELECT * FROM Data.polar WHERE Name = 'Karla'"
cur.execute(sql)
datos = cur.fetchall()
cur.close()  
print(len(datos))
df = pd.DataFrame(data=datos)
print(df)
print(df[3])

cur = cnn.cursor()
sql = "SELECT * FROM Data.myoware WHERE Name = 'Karla'"
cur.execute(sql)
datos2 = cur.fetchall()
cur.close()  
df2 = pd.DataFrame(data=datos2)

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Piloto')

ax1.plot(df2[2],df2[3], 'o-')
ax1.plot(df2[2],df2[4], 'o-')
ax1.set_ylabel('Myoware')

ax2.plot(df[2], df[3], '.-')
ax2.set_xlabel('time')
ax2.set_ylabel('Polar')

plt.show()




