# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 20:42:35 2022

@author: Diana Magaña Nava
"""
#Funcion para el registro de las padawans
def registro():
    padawan={'nombre':' ','edad':1,'estado':' ','temas':' '}
    
    padawan['nombre'] = input("Ingresa el nombre: ")
    padawan['edad'] = input("Ingresa la edad: ")
    padawan['temas'] = input("Ingresa tu tema de interes: ")
    
    if (int(padawan['edad']) > 18):
        padawan['estado'] = 'Es mayor de edad'
    else :
        padawan['estado'] = 'Es menor de edad'
    return padawan
    
#Función para imprimir la lista padawans
def informe(padawans):
    for padawan in padawans:
        #print('\n')
        print('*'*40)
        for key in padawan:
            print(f'{key}: {padawan[key]}')
      
padawans = [] #lista que contiene los diccionarios
while(True):
    print('_'*50)
    print("1. Añadir una padawan ")
    print("2. Lista de participantes ")
    print("3. Salir")
    opcion = int(input("Elige una opción:  "))
    if opcion == 1:
        padawan = registro()
        padawans.append(padawan)
    elif opcion == 2:
        informe(padawans)
    elif opcion == 3:
        break
    else:
        print("Error, opción inválida")


    
        