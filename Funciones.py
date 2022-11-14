#Karem Ramos Calpulalpan - 314068583

def menu():
    """Genera las opciones que hay dentro de este menú."""
    opciones = {
        '1': ('Compara dos números enteros y regresa el mayor.', numeroMayor),
        '2': ('Calcula la longitud de una lista.', longitudLista),
        '3': ('Te dice si una cadena es un palindromo.', es_Palindromo),
        '4': ('Dado un número n y un carácter x, muestra n veces el carácter x.', generarCaracteres),
        '5': ('Salir', salir)
    }
    generar_menu(opciones, '5')

def mostrar_menu(opciones):
    """Muestra el menú."""
    print('Selecciona la función que quieres probar, por favor:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    """Lee la opción que le pasa el usuario."""
    while (valor := input('Opción: ')) not in opciones:
        print('Escribe un número, vuelve a intentarlo.')
    return valor

def ejecutar_opcion(opcion, opciones):
    """Manda a llamar la opción que eligio el usuario del menú."""
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    """Muestra el menú, según la opción"""
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def numeroMayor():
    """Compara dos números enteros y regresa el mayor."""
    print("\n****** Compara dos números enteros y regresa el mayor. ******\n")
    numero_1 = int(input("Escribe el primer número entero positivo: "))
    numero_2 = int(input("Escribe el segundo número entero positivo: "))
    if numero_1 < numero_2:
        print("El número mayor es: ", numero_2)
    else:
        print("El número mayor es: ", numero_1)

def longitudLista():
    """Muestra la longitud de una lista."""
    print("\n****** Muestra la longitud de una lista. ******\n")
    nombres = ['Karem', 'Juan', 'María', 'Carlos', 'José']
    print("La lista es: ", nombres)
    print("La longitud de la lista es: ", len(nombres))

def es_Palindromo():
    """Te dice si una oración es un palindromo."""
    print("\n****** Te muestra False si una oración NO es un palindromo y True si \n una oración sí es un palindromo. ******\n")
    cadena = input("Escribe una oración: ")
    cadena = cadena.lower().replace(' ', '')
    print(cadena == cadena[::-1])

def generarCaracteres():
    """Dado un un número y un carácter genera n veces, el x carácter"""
    print("\n****** Dado un número n y un carácter x, genera n veces el carácter x. ******\n")
    numero = int(input("Escribe un número entero positivo, por favor: "))
    caracter = input("Escribe un carácter, por favor:")
    print(numero*caracter)

def salir():
    """Muestra una cadena de despedida."""
    print("\n¡Adiós!")

if __name__ == '__main__':
    menu()
