from audioop import mul
from tkinter.messagebox import RETRY


def mayor(x1, x2):
    if x1 > x2:
        return x1 
    else:
        return x2

def longitud(arr):
    i = 0
    for e in arr:
        i += 1
    return i

def es_palindromo(arr):
    l = longitud(arr) - 1
    i = 0
    while l != -1:
        if arr[l] != arr[i]:
            return False
            break
        else:
            l-=1
            i+=1
    return True

def multiplicar_caracter(n, char):
    return(int(n) * char)
