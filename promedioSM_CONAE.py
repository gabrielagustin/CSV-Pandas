#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 06:42:18 2018

@author: gag

Script que lee multiples archivos .CSV con mediciones de humedad y temperatura de suelo
y realiza el promedio en base al identificador del dispositivo. Luego, genera nuevos 
archivos .CSV con los promedios de las variables. 

"""

import pandas as pd
from os import listdir
import os
import numpy as np

dir = "gag"


pathIN = "/home/"+dir+"/Escritorio/mediciones_sensoresHPII_160415-050715_MB/"
pathOUT = "/home/"+dir+"/Escritorio/mediciones_sensoresHPII_160415-050715_MB/SM_CONAE_Prom/"

for cosa in listdir(pathIN):
    if os.path.splitext(cosa)[-1] == '.csv':
        print(cosa)
        nom = cosa[:-4] + '_Prom.csv'
        file = pathIN + cosa
        data = pd.read_csv(file, sep=',', decimal=",")
#        print(data)
#        result = data.sort(['ID_DISPOSI,N,19,0'])
#        print(data)
        
#        Latitud = np.unique(result['LATITUD,N,32,10'].values)
#        Longitud = np.unique(result['LONGITUD,N,32,10'].values)
        data_mean_SM = (data['RSOILMOIST,N,32,10'].groupby(data['ID_DISPOSI,N,19,0']).mean())
#        print(data_mean_SM)
        data_mean_Ts = (data['RSOILTEMPC,N,32,10'].groupby(data['ID_DISPOSI,N,19,0']).mean())
#        print(data_mean_Ts)
        Latitud = (data['LATITUD,N,32,10'].groupby(data['ID_DISPOSI,N,19,0']).mean())
        Longitud= (data['LONGITUD,N,32,10'].groupby(data['ID_DISPOSI,N,19,0']).mean())
#        Latitud = (data['LATITUD,N,32,10'].groupby(data['ID_DISPOSI,N,19,0']).axis=0)
#        Latitud = (groupby(data['ID_DISPOSI,N,19,0']).['LATITUD,N,32,10'])
#        print(Latitud)

        #
        df = pd.DataFrame({'Latitud':Latitud,'Longitud':Longitud,'Ts':np.array(data_mean_Ts),'SM':data_mean_SM})
#        print(df)
        df.to_csv(pathOUT + nom, decimal = ",")
        print("Archivo creado con exito!" + str(nom))