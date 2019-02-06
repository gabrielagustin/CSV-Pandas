# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:58:49 2019

@author: gag

Script que lee todos los ficheros (MESES) dentro de un fichero inicial(AÑO).
Cada fichero posee archivos .CSV (cada archivo se corresponde con una pasada de satelite
por horas) para todos los días para cada mes del año.
Genera un objeto pandas que posee todos los archivos .CSV y los 
organiza por fecha. 

"""


import os
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


directory = "/.../"
arr = os.listdir(directory)
big_frame = pd.DataFrame()
# for i in range(0, len(arr)):
for i in range(0, 1):
    print("Mes - Año: " +str(arr[i]))
    csvFiles = os.listdir(directory+str(arr[i]))
    print("Cantidad de archivos .CSV: "+str(len(csvFiles)))
    for j in range(0,len(csvFiles)):
    # for j in range(0,1):
        name = csvFiles[j]
        date = str(name[20:-15])
        print("Fecha archivo .CSV: " + date)
        df = pd.read_csv(directory+str(arr[i])+"/"+str(csvFiles[j]),sep=',', decimal=",")
        df['Date'] = str(date)
        big_frame = big_frame.append(df, ignore_index=True)

# print(big_frame['Date'])

result = big_frame.sort_values(by=['Date'])
result = result.reset_index(drop=True)
result.to_csv("../DataSet.csv", decimal = ",")
print("Archivo año completo creado con exito!")


          
