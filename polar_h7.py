import sys
import mysql.connector
from datetime import datetime
#INSERT INTO `Data`.`polar` (`Name`, `Time`, `Value`) VALUES ('Alejandro', '20:10:45', '60');
Name="Karla"
cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="45237823", database="Data")

def saveData(data,time):
    print("Data")
    cur = cnn.cursor()
    sql='''INSERT INTO `Data`.`polar` (`Name`, `Time`, `Value`) VALUES ('{}', '{}', '{}')'''.format(Name,time,data)
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
            po = buff.split(" ")    #Se genera una separacion de cada parte del codigo por cada espacio
            if po[0] == 'Characteristic':   #Se utiliza esta carracteristica para no dar valides ala primera linea, que es solo cadena de strings sin datos
                print("Data Polar h7")       #Nos indica qeu se da inicio y ya llego la primera linea
            else:
                hr=int(po[6],16)
                            #Se extrae el valor de la frecuencia cardiaca de la cadena string y se genera la conversion de hex a dec
                saveData(hr,now)
                print("  {} PRbpm  Time: {}".format(hr,now))  #Se escribe en cosola el valor de esta convercion 

            buff = '' #Se vacia variable
except KeyboardInterrupt: #Metodo de intorrupcion por teclado
   sys.stdout.flush()
   pass

