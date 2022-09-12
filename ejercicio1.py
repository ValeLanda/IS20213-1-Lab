"""
    Ingeniería de Software 
    Semestre 2023-1
    Fausto David Hernández Jasso
    Ejercicio 1
"""


"""
    Dados dos números enteros decidimos cuál es el mayor.
"""
def mayor(num1: int, num2: int) -> int:
    if (num1 > num2):
        return num1
    else:
        return num2


"""
    Dada una cadena o una lista, devolvemos su longitud.
"""
def longitud(param):
    len = 0
    for i in param:
        len += 1
    return len
    

"""
    Sea s una cadena determinamos sí s es palíndromo.
"""
def es_palindromo(string: str) -> bool:
    l = longitud(string)
    for i in range(l):
        if (string[i] != string[l - i - 1]):
            return False
    return True


"""
    Sea n un número entero positivo y chr un carácter, 
    devolvemos una cadena con n concatenaciones de chr.
"""
def generar_caracteres(n: int, chr: str) -> str:
    if (longitud(chr) != 1):
        raise Exception("Los carácteres deben de tener longitud 1")
    else:
        str_generated = ""
        for i in range(n):
            str_generated += chr
        return str_generated


"""
    Algunos ejemplos de uso de las funciones.
"""
if __name__ == "__main__":
    print(mayor(5,6))
    l = [x*x for x in range(16)]
    str = "thisisastring"
    print(longitud(l))
    print(longitud(str))
    palindromo = "aaabbaaa"
    no_palindromo = "anita"
    print(es_palindromo(palindromo))
    print(es_palindromo(no_palindromo))
    print(generar_caracteres(5, "x"))
    print(generar_caracteres(10, "f"))