# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class usuario:
    
    def __init__(self, user, passw):
        self.user = user
        self.__passw = passw
        
user1 = usuario('CamF','prog_avz1234')

passw_ingreso ='prog_avz1234'

if user1._usuario__passw ==passw_ingreso:
    print('Acceso Concedido')
else:
    print ('Vuelve a interntarlo')
    
