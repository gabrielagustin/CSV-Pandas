#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 05:57:59 2018

@author: gag
"""

# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statistics
from scipy import stats



if __name__== "__main__":

    path = "/.../"
    nameFile = "file.csv"
    file = path+nameFile

    df = pd.read_csv(file, sep=',', decimal=",")

    #### se agrupa por: Fecha y Coordenadas y se calcula la media de las variables. Es decir, se calcula la
    #### media para cada dia de cada punto o lo que es lo mismo, se promedia las pasadas del satelite en el día.

    group_data = df.groupby(['Date','Coordinates_KML'], sort=False)['Brightness Temperature (10.7GHz,H)', 
    'Brightness Temperature (10.7GHz,V)', 'Brightness Temperature (18.7GHz,H)', 'Brightness Temperature (18.7GHz,V)',
    'Brightness Temperature (36.5GHz,H)', 'Brightness Temperature (36.5GHz,V)', 'Brightness Temperature (6.9GHz,H)',
    'Brightness Temperature (6.9GHz,V)', 'Brightness Temperature (7.3GHz,H)', 'Brightness Temperature (7.3GHz,V)'].mean()

    df = group_data

    #### Luego, se vuelve a agrupar por punto (coordinates) para todas las fechas, para una banda en particular
    #### y se calcula la media y el STD
    df6_9GHz = df.groupby(['Coordinates_KML'], sort=False)['Brightness Temperature (6.9GHz,H)', 
            'Brightness Temperature (6.9GHz,V)'].agg({'mean', 'std'})
    df6_9GHz = df6_9GHz.reset_index(drop=False)


    name = 'AMSR2 GW1AM2 L1B - November Last week Flight Line November'
    # name = 'AMSR2 GW1AM2 L1B - December First week Flight Line December'
    clrs = sns.color_palette("husl", 5)

    fig1, ax1 = plt.subplots()
    ix = df6_9GHz['Brightness Temperature (6.9GHz,H)'].index.values
    mm = df6_9GHz['Brightness Temperature (6.9GHz,H)']['mean']
    std = df6_9GHz['Brightness Temperature (6.9GHz,H)']['std']
    ax1.plot(ix, mm, label='BT (6.9GHz,H)')
    ax1.fill_between(ix, mm-std, mm+std ,alpha=0.3, facecolor=clrs[0])
    plt.title(name)
    ax1.set_xlabel("Point")
    ax1.set_ylabel("Brightness_Temperature[K]")
    ax1.legend(loc='lower right')

    plt.show()
 