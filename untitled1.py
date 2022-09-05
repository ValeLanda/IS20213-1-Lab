# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 15:29:42 2022

@author: O.Ledesma
"""

def mayor(a, b):
    if a > b:
        return a
    else:
        return b
    
def longitud(lista):
    longitud = 0
    for x in lista:
        longitud = longitud + 1
    return longitud

def es_palindromo(palabra):
    return palabra == palabra[::-1]
        

def caracteres(caracter, n):
    return caracter*n