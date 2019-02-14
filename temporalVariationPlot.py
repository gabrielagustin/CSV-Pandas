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

    data = pd.read_csv(file, sep=',', decimal=",")


    data['SM_CONAE'] = data['SM_CONAE']*100
    data['SM_SMAP'] = data['SM_SMAP']*100
    data['Ts_SMAP'] = data['Ts_SMAP']-273.15
    data['sigma0_hh_'] = 10*np.log10(data['sigma0_hh_'])
    data['sigma0_vv_'] = 10*np.log10(data['sigma0_vv_'])

    data.GPM = data.GPM * 0.1

    del data['wkt_geom']
    del data['ID_DISPOSI']


    data = data.fillna('')


    fig, ax = plt.subplots()
    data.plot(ax=ax, xticks=data.index, rot=45)
    tick_idx = plt.xticks()[0]
    year_labels = data.Date[tick_idx].values
    ax.xaxis.set_ticklabels(year_labels)

    plt.show()
 