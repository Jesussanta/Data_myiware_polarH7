#Guarda encuestas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

def insertat (No,D1,D2,D3,UC1,UC2,UC3,UC4,UC5,UC6,UC7):
    cnn = mysql.connector.connect(host="localhost", user="root",passwd="45237823", database="eval")
    cur = cnn.cursor()
    sql='''INSERT INTO `feria` (`No`, `D1`, `D2`, `D3`, `UC1`, `UC2`, `UC3`, `UC4`, `UC5`, `UC6`, `UC7`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');'''.format(No,D1,D2,D3,UC1,UC2,UC3,UC4,UC5,UC6,UC7)
    cur.execute(sql)
    n=cur.rowcount
    cnn.commit()    
    cur.close()
    return n   
for i in range(15):
    No=input("Nombre: ")
    D1=input("Diagnostico(1): ")
    D2=input("Diagnostico(2): ")
    D3=input("Diagnostico(3): ")
    UC1=input("Usailidas y calidad (1): ")
    UC2=input("Usailidas y calidad (2): ")
    UC3=input("Usailidas y calidad (3): ")
    UC4=input("Usailidas y calidad (4): ")
    UC5=input("Usailidas y calidad (5): ")
    UC6=input("Usailidas y calidad (6): ")
    UC7=input("Usailidas y calidad (7): ")

    data=[No,D1,D2,D3,UC1,UC2,UC3,UC4,UC5,UC6,UC7]
    print("Rectifique:")
    print(data)
    a = input("Subir datos?")
    if(a == "s"):
        insertat(No,D1,D2,D3,UC1,UC2,UC3,UC4,UC5,UC6,UC7)
        print("Valores guardados.")
    else:
        print("Adios!!!")
        exit()
