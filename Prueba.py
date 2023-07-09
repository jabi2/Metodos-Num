# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
José Pablo Ortega Grajeda
04/07/2023

Prueba
"""
from pylab import *

#función adivina
def adivina(n):
    """ Genera un número aleatorio entre 1 y el parámetro n, para luego 
        solicitar al usuario el ingreso de números hasta que acierte con el 
        número generado. """
        
    rand = randint(1,n) #se genera el número aleatorio
    #print (rand)
    
    while True:
        numero = input("Adivine el numero entre 1 y " + str(n) + ": ") #se pide el ingreso del número
        #print (type(numero))
        
        if numero == str(rand): #si se acierta, se imprime el mensaje en pantalla
            print ("Felicidades, el numero era " + str(numero))
            break
    
#función primos
def primos(n):
    """ Devuelve la cantidad de números primos que hay hasta el número 'n', 
        incluyéndolo. Para este caso, el 1 no se considera como número primo. """
    
    totalPrimos = 0
    indicador = 1
    
    for i in range(2, n+1): #se revisa cada número desde 1 hasta n
        for j in range(2,i): #se obtiene l residuo del número divido entre cada número anterior
            if i % j == 0: #si el residuo es 0, no es primo por lo que el indicador se pone en 0
                indicador = 0
                break
        totalPrimos += indicador #se suma el indicador a la cuenta
        indicador = 1
    
    return totalPrimos
