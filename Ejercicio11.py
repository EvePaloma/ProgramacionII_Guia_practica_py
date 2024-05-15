'''
Ejercicio 11: Adivinador de números
Crea un juego que le pida al usuario que piense un número entre 1 y 100. 
Luego, el programa debe intentar adivinar ese número utilizando la estrategia de búsqueda binaria. 
En cada intento, el programa debe preguntar al usuario si el número a adivinar es mayor, 
menor o igual al número propuesto por el programa. 
El juego debe terminar cuando el programa adivine el número correcto.

'''

def adivinar_num():
    print("Piensa en un número del 1 al 100...")
    input("Estas listo/a?\nPreciona enter para empezar.")
    
    limite_inferior = 1
    limite_superior = 100
    num_encontrado = False

    while not num_encontrado:
        num_propuesto = (limite_inferior + limite_superior) // 2
        print(f"Es tu número {num_propuesto}?")
        respuesta = input("Por favor ingresa 'menor', 'mayor' o 'igual': ").lower()

        if respuesta == "igual":
            print(f"¡Adivine tu número! Es {num_propuesto}")
            num_encontrado = True
        elif respuesta == "menor":
            limite_superior = num_propuesto -1
        elif respuesta == "mayor":
            limite_inferior = num_propuesto + 1
        else:
            print("Por favor ingresa una respuesta válida (menor, mayor o igual)")

adivinar_num()                     