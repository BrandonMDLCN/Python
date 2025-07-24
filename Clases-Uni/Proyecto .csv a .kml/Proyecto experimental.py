# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 22:44:39 2021

@author: BrandonDLC
"""

import simplekml
import pandas

df = pandas.read_csv("D:\\Descargas\\Coordenates.csv")

kml = simplekml.Kml()

for lon, lat in zip(df["Longitude"], df["Latitude"]):
    kml.newpoint(coords = [(lon,lat)])
    
kml.save("D:\\Descargas\\Points.kml")