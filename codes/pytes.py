import sys
import mysql.connector
from datetime import datetime
#INSERT INTO `Data`.`polar` (`Name`, `Time`, `Value`) VALUES ('Alejandro', '20:10:45', '60');
Name="m7"
cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="45237823", database="Data")

def saveData(Mi,Ma,time):
    cur = cnn.cursor()
    sql='''INSERT INTO `Data`.`myoware` (`Name`, `Time`, `Min`, `Max`) VALUES ('{}', '{}', '{}','{}')'''.format(Name,time,Mi,Ma)
    cur.execute(sql)
    n=cur.rowcount
    cnn.commit()    
    cur.close()
    pass
try:
    buff = '' #Se inicializa variables
    while True:
        buff += sys.stdin.read(1) #Se anexa la cadena recivida del sensor
        if buff.endswith('\n'): #Se ejecuta cada salto de linea
            now = datetime.now()
            now = now.strftime("%H:%M:%S")
            #print( buff[:-1])  #Se puede ver lo que llega al script
            po = buff.replace("\n", "")   #Se genera una separacion de cada parte del codigo por cada espacio
            if po[0] == 'hello':   #Se utiliza esta carracteristica para no dar valides ala primera linea, que es solo cadena de strings sin datos
                print("Data Myoware")       #Nos indica qeu se da inicio y ya llego la primera linea
            else:
                hr=po.split("-")
                print(hr)
                saveData(hr[0],hr[1],now)
                print(" Min:{} Max:{} Time: {}".format(hr[0],hr[1],now))  #Se escribe en cosola el valor de esta convercion 

            buff = '' #Se vacia variable
except KeyboardInterrupt: #Metodo de intorrupcion por teclado
   sys.stdout.flush()
   pass
