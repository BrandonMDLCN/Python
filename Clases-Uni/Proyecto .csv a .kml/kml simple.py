# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:34:23 2021

@author: BrandonDLC
"""

from simplekml import Kml
kml = Kml(name='KmlUsage')
kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)]) #Punto simple
kml.save("KmlClass.kml")  # guardar
print(kml.kml())  # Imprimir
