# coding=utf-8

"""
Ejercicios Laboratorio

Diana Berenice Hernández Alonso.
317183425
"""

"""
1. Función que tiene como parámetro dos números enteros y 
   devuelve el mayor de ellos.
"""

def mayor (a, b):
	if (a > b):
		return a
	else:
		return b

"""
2. Función que calcula la longitud de una lista o cadena 
   dada.
"""

def longitud (l):
	lon = 0
	for i in l:
		lon += 1
	return lon

"""
3. Función que devuelve True si son palabras palíndromas y 
   False en otro caso. 
"""

def palindromo(p):
	cadena = ""
	for i in p:
		cadena = i + cadena
	return (p == cadena)

"""
4. Función que toma un entero n y un carácter y devuelve 
   el carácter multiplicado por n. 
"""

def multiplica(n, char):
	if (longitud (char) != 1):
		print("La cadena debe tener solo un caracter")
	else:
		return (char * n)

#Ejemplos

print("\nMayor entre 3 y 8:")
print(mayor(3, 8))

print("\nLongitud de la lista [1, 2, 4, 7]:")
print(longitud ([1, 2, 4, 7]))

print("\nEs palindromo oso?")
print(palindromo("oso"))

print("\nEs palindromo hola?")
print(palindromo("hola"))

print("\nMultiplica 5 veces b:")
print(multiplica(5, "b"))

"""
Comentario:

Tuve que poner este comando: 

# coding=utf-8

al principio del archivo por que sin el me salia este error:

SyntaxError: Non-ASCII character '\xc3' in file Ejercicios.py 
on line 7, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

al tratar de correr el archivo.
"""