# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Javier Andrés Bocanegra Fuentes
04/07/2023

Hoja de trabajo 1
"""

"""
Escribir una función en Python que devuelva la suma de todos los divisores de un número, sin
incluirlo. Usando la función anterior, escribir una función que imprima los primeros números
tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros números perfectos)
"""

def divi(n):
    """ Devuelve la suma de los divisores de el numero 'n' """
    
    divisores = []
    perff = False
    selebrasao = ''

    
    for i in range(1, n): 

        if n % i == 0: 
            divisores.append(i)

    
    return sum(divisores)

def perfs(n):
    """ Devuelve los numeros perfectos hasta ese el numero 'n' """
    
    prfs = []
    
    for i in range(1, n):
        if divi(i) == i:
            prfs.append(i)
        
    return prfs
            