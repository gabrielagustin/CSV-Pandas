#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  31 06:42:18 2017

@author: gag

Script that reads multiple .SHP files with humidity and soil temperature measurements. 
A set of previously identified devices (ID) is read from each file. The average is calculated for
each device based on the ID and a new .SHP file is generated with this new information

"""

import shapefile

###----------------------------------------------------------------------------
### se listan las fechas de los archivos y los dispositivos que deseamos en c/u

#fecha = "2015-04-11"
#dispos = [55,82,121,123,125,133]

#fecha = "2015-05-26"
#dispos = [55,82,105,123,125,126,129,130,132,133,135]

#fecha = "2015-06-19"
#dispos = [55,82,105,121,125,126,129,132,133]

#fecha = "2015-07-24"
#dispos = [55,82,121,125,126,129,133,134,135,148]

#fecha = "2015-08-30"
#dispos = [55,82,121,125,126,129,133,134,135,148]

#fecha ="2015-09-23"
#dispos = [55,82,121,125,129,133,134,135,148]

#fecha ="2015-10-04"
#dispos = [55,121,123,129,133,131,134,148,151]

#fecha ="2015-11-21"
#dispos = [55,82,121,123,129,133,134,135,148]

#fecha ="2015-12-18"
#dispos = [55,82,121,123,125,129,133,134,135,148]

#fecha ="2016-01-08"
#dispos = [55,121,123,129,133,134,148,151]

#fecha ="2016-02-14"
#dispos = [82,121,129,133,134,135,148]

#fecha ="2016-03-20"
#dispos = [55,105,121,125,126,129,134,135,148,158]

#fecha ="2016-04-13"
#dispos = [55,121,123,125,126,133,134,148]

#fecha ="2015-04-03"
#dispos = [55,82,104,121,123,125,126,129,133]

#fecha ="2015-04-27"
#dispos = [55,82,121,123,125,126,129,132,133]

#fecha ="2015-05-15"
#dispos = [55,82,104,105,125,126,129,130,132,133,135]

#fecha ="2015-06-03"
#dispos = [132]

#fecha ="2015-06-30"
#dispos = [55,132,133]

#fecha ="2015-07-05"
#dispos = [121,132,134]

#fecha ="2015-07-16"
#dispos = [121,123,134]

#fecha ="2015-08-01"
#dispos = [55,82,121,123,125,126,129,133,134,135,148]

#fecha ="2015-08-20"
#dispos = [55,82,121,123,125,126,129,133,134,135,148]

#fecha ="2015-09-02"
#dispos = [55,121,123,126,129,133,134,148]

#fecha ="2015-09-10"
#dispos = [121,134]

#fecha ="2015-10-15"
#dispos = [55,82,121,123,125,129,133,134,148]

#fecha ="2015-10-28"
#dispos = [121,123,134]

#fecha ="2015-11-02"
#dispos = [55,82,104,121,125,133,134,135,148]

#fecha ="2015-11-13"
#dispos = [55,121,123,129,133,134,148]

#fecha ="2015-12-01"
#dispos = [121,123,134]

#fecha ="2015-12-28"
#dispos = [55,82,121,123,125,129,133,134,135,148]

#fecha ="2016-01-19"
#dispos = [55,82,121,123,125,129,133,134,148]

#fecha ="2016-01-27"
#dispos = [55,123,125,133]

#fecha ="2016-02-04"
#dispos = [55,82,121,123,125,129,133,134,135,148]

#fecha ="2016-02-25"
#dispos = [121,134]

#fecha ="2016-03-01"
#dispos = [55,82,121,125,129,133,134,135,148]

#fecha ="2016-03-12"
#dispos = [55,82,121,125,129,133,134,135,148]

#fecha ="2016-04-02"
#dispos = [55,105,121,123,125,126,129,133,134,148]

#fecha ="2016-04-24"
#dispos = [55,123,125,133,158]


#fecha ="2015-05-26"
#fecha ="2015-06-28"
#fecha ="2015-07-06"
#fecha ="2015-07-11"
#fecha ="2015-07-16"
#fecha ="2015-07-24"
#fecha ="2015-09-08"
#fecha ="2015-09-13"
#fecha ="2015-09-21"
#fecha ="2015-10-04"
#fecha ="2015-11-11"
#fecha ="2015-11-16"
#fecha ="2015-11-19"
#fecha ="2015-11-24"
#fecha ="2015-11-29"
#fecha ="2015-12-02"
#fecha ="2015-12-07"
#fecha ="2015-12-12"
fecha ="2016-02-04"
#fecha ="2016-02-14"
#fecha ="2016-02-25"
#fecha ="2016-03-01"
#fecha ="2016-04-03"
#fecha ="2016-04-08"
#fecha ="2016-04-11"
#fecha ="2016-04-16"

dispos = [122,124,128]

###----------------------------------------------------------------------------

path = "/home/ggarcia/Escritorio/data_inSitu/"

nameIn = path + fecha + "/Mediciones_Hydraprobe_diaria/" + fecha

inFile1 = nameIn +'.shp'
inFile2 = nameIn +'.dbf'


myshp = open(inFile1, "rb")
mydbf = open(inFile2, "rb")
sf = shapefile.Reader(shp=myshp, dbf=mydbf)

nameOut = path + fecha +"/mediciones_Hydraprobe_promedio/"
outFile = nameOut + fecha +'_Promedio.shp'


# Create a new shapefile in memory
w = shapefile.Writer(shapefile.POINT)
#w._shapes.extend(sf.shapes())
#w.null()
w.fields = list(sf.fields)

#p = list(sf.fields)
##print w.fields
#index1 = p.index(['RSOILMOIST', 'N', 19, 10])
#p[index1]= ['RSOILMOIST_MEAN', 'N', 19, 10]

#index2 = p.index(['RSOILTEMPC', 'N', 19, 10])
#p[index2]= ['RSOILTEMPC_MEAN', 'N', 19, 10]

#w.fields = p

#print w.fields

#w.records.extend(sf.records())
### se copia un unico registro para luego modificar
vv = sf.record(0)


fields = sf.fields[1:]
field_names = [field[0] for field in fields]
# construction of a dctionary field_name:value

### defino una lista de diccionarios
lrecords = []
lpoints = []
for r in sf.shapeRecords():
    #print r.shape.__geo_interface__
    lpoints.append(r.shape.points[0:2])
    lrecords.append(dict(zip(field_names, r.record)))
    #print (zip(field_names, r.record))



### crea una nueva lista solo con los dispositivos que necesitamos
lrecordsCopia = []
lpointsCopia = []
dispos2 = []
for i in range(0,len(lrecords)):
    valor = lrecords[i].get('ID_DISPOSI')
    if (valor not in dispos):
        #print valor
        if not (valor in dispos2):
            dispos2.append(valor)
        lrecordsCopia.append(lrecords[i])
        lpointsCopia.append(lpoints[i])

dispos = dispos2
for j in range(0,len(dispos)):
    SM_mean = 0
    SoilT_mean = 0
    SoilT = 0
    SM = 0
    count = 0
    item =[]
    for k in range(0,len(lrecordsCopia)-1):
        if (lrecordsCopia[k].get('ID_DISPOSI') == dispos[j]):
            item = lrecordsCopia[k]
            point = lpointsCopia[k]
            SM = SM + lrecordsCopia[k].get('RSOILMOIST')
            SoilT = SoilT + lrecordsCopia[k].get('RSOILTEMPC')
            count = count + 1
    #print item
    SM_mean = SM/(count)
    SoilT_mean = SoilT/(count)
    print dispos[j]
    print SM_mean
    print SoilT_mean

# len(field_names)
    #print type(vv)
    q =[]

    for i in range(0, len(field_names)):
        #print id
        id = field_names[i]
        valor = item.get(id)
        q.append(valor)
    index1 = field_names.index('RSOILMOIST')
    #valor1 =  round(SM_mean,4)
    #print q[index1]
    q.pop(index1)
    q.insert(index1, SM_mean)
    index2 = field_names.index('RSOILTEMPC')
    q.pop(index2)
    q.insert(index2, SoilT_mean)
    print point[0]
    w.point(point[0][0],point[0][1])
    #w.point(122, 37)
    w.records.append(q)
#theend= []
#w.records.append(theend)
w.save(outFile)


