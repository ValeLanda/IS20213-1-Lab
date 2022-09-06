'''
Problemas en python 3
Alumno: Rodrigo Arevalo Gaytan
Fecha: 05-09-2022
'''

# Funcion que regresa el mayor entre dos numeros
def mayor(a,b):
	return a if a>b else b

# Funcion que regresa la longitud de una lista o una cadena
def longitud(ls):
	count=0
	for i in ls:
		count+=1
	return count

# Funcion que nos dice si una palabra es un palindromo
def es_palindromo(p):
	base = ""
	for x in p:
		base = x + base
	return(p==base)

# Funcion que toma un entero n y un caracter x y devuelve
# el caracter multiplicado por n.
def generar_caracteres(n,x):
	if (longitud(x) > 1):
		print("Solo se aceptan caracteres (cadenas de longitud 1)")
	else:
		base = ""
		for i in range(n):
			base = base + x
		return(base)