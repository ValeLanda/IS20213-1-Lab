def obtener_mayor(a,b):
    if (a<b):
        return b
    else:
        return a

def longitud(l):
    return len(l)

def es_palindromo(l):
    for i in range(len(l)//2):
        if l[i] != l[len(l)-1-i]:
            return False
    return True

def generar_caracteres(n,x):
    return x*5
