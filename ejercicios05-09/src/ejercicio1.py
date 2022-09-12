
# Ejercicios 
# 1. Realiza una función que tome como parámetro dos números enteros y devuelva el mayor de ellos.
def mayor_es(x,y):
	if x > y:
		return x
	else: 
		return y;

# 2. Definir una función que calcule la longitud de una lista o cadena dada
def leng(cadena):
	longitud = 0
	for x in cadena:
		longitud +=1
	return longitud
# 3. Definir una función es_palindromo() que reconoce palabras palíndromas y regresa
# True en caso de ser así, en otro caso, devuelve False.
def es_palindromo(cadena):
	palindromo = ''
	for x in cadena:
		palindromo = palindromo + x
	if palindromo == cadena:
		return True
	return False
# 4. Definir una función que tome un entero n y un carácter y devuelve el carácter multiplicado por n.
# Por ejemplo generar_caracteres(5, “x”) devuelve —> “xxxxx”
def genera_caracters(number, character):
	return (number * character)

if __name__ == '__main__':
	print (mayor_es(20,21))
	print (leng('teamofergb'))
	print (es_palindromo('eevee'))
	print (genera_caracters(31,'x'))