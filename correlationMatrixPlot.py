#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 05:57:59 2018

@author: gag
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statistics
from scipy import stats
import selection



def corrfunc(x, y, **kws):
  #r = r2_score(x, y)
  r, p = stats.pearsonr(x, y)
  p_stars = ''
  #if p <= 0.05:
    #p_stars = '*'
  #if p <= 0.01:
    #p_stars = '**'
  #if p <= 0.001:
    #p_stars = '***'
  ax = plt.gca()
  ax.annotate('r = {:.2f} '.format(r) + p_stars,
              xy=(0.2, 0.5), xycoords=ax.transAxes, size=15)

def annotate_colname(x, **kws):
  ax = plt.gca()
  ax.annotate(x.name, xy=(0.05, 0.9), xycoords=ax.transAxes,
              fontweight='bold', size=12)

def cor_matrix(df):
  g = sns.PairGrid(df, diag_sharey=False)
  # Use normal regplot as `lowess=True` doesn't provide CIs.
  #g.map_upper(sns.regplot, scatter_kws={'s':10})
  g.map_lower(sns.regplot, scatter_kws={'s':5})
  g.map_diag(sns.distplot, bins=20)
  #g.map_offdiag(plt.scatter);
  #g.map_diag(plt.hist)
  #g.map_diag(sns.kdeplot)
  #g.map_diag(annotate_colname)
  #g.map_lower(sns.kdeplot, cmap='Blues_d')
  #g.map_lower(corrfunc)
  g.map_upper(corrfunc)
  # Remove axis labels, as they're in the diagonals.
  #for ax in g.axes.flatten():
    #ax.set_ylabel('')
    #ax.set_xlabel('')
#  g.fig.tight_layout()
  g.axes[0,0].set_ylim(0,50)

  return g


if __name__== "__main__":
  path = "/.../"
  nameFile = "extract_table_2.csv"
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
  #del data['sigma0_hh_']
  #del data['GPM']
  data = data.fillna('')

  data = data.dropna()

  g = cor_matrix(data)
  plt.show()
