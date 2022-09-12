import math  

def mayor(uno, dos):
    if(uno > dos):
        res = uno
    else:
        res = dos
    return res

def longitud(liscad):
    i = 0
    for x in liscad:
        i += 1
    return i
    
def es_palindromo(pal):
    caduno = []
    caddos = []

    x = len(pal)-1
    while x >= math.floor(len(pal)/2):
        caddos += pal[x]
        x -= 1
    
    i = 0
    while i <= math.floor(len(pal)/2):
        caduno += pal[i]
        i += 1

    return  caduno == caddos

def duplica(veces,caracter):
    x = 1
    nuevocar = caracter
    while x < veces:
        nuevocar = nuevocar + caracter
        x+=1
    return nuevocar


if __name__ == "__main__":
    print(mayor(2,3))
    lista = [1,2,3,4,5,6,7,8,9,10]
    cadena = "reconocer"
    cadenados = "prueba"
    cadenatres = "sometemos"
    print(longitud(lista))
    print(longitud(cadena))
    print(es_palindromo(cadena))
    print(es_palindromo(cadenados))
    print(es_palindromo(cadenatres))
    print(duplica(5,"x"))
    print(duplica(10,"y"))
    
    