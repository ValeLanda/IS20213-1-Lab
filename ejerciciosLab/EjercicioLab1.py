#Resuelve los problemas 
""""1. Realiza una función que tome como parametro dos 
números enteros y devuelva el mayor de ellos"""

def mayor(num1, num2):
    if num1 > num2: 
    	return num1
    else:
    	return num2
    	
"""2. Definir una función que calcule la longirud de una 
lista o cadena dada"""
def longitud(cadena):
    longitud= 0
    #Recorremos la cadena y por cada posicion sumamos 1 al contador
    for i in cadena: 
        longitud += 1
    return longitud
"""3. Definir una función es_palindromo() que reconoce palabras
palindromas y regresa true en caso de ser asi, en otro caso False"""
def es_palindromo(pala):
    palin = ""
    #Recorremos la string y vamos guardandola en la nueva variable 
    for i in pala:
        palin = i + palin
    if (pala == palin):
        return True
    else: 
        return False

"""4. Definir una función que tome un entero n y un caracter y 
devuelve el caracter multiplicado por n"""
def generar_caracteres(num, carac):
	return num*carac
	

if __name__ == "__main__":
    print("el número mayor es:", mayor(10,35))
    print(longitud("stay"))
    print(es_palindromo("oso"))
    print(es_palindromo("atencion"))
    print(generar_caracteres(5, "u"))
