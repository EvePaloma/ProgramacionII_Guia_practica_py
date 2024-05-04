#Ejercicio 7: Juego de Adivinar el Número 
#Desarrolla un juego en el que el programa selecciona aleatoriamente un número 
#entre 1 y 100 y el jugador debe adivinarlo. El programa debe proporcionar pistas 
#al jugador si el número ingresado es demasiado alto o demasiado bajo.
# El juego debe continuar hasta que el jugador adivine correctamente el número.

import random

def juego_adivinar_num():
    num = random.randint(1,100)

    print("Bienvenido al juego de ADIVINAR EL NÚMERO!")
    
    while True:

        intento = int(input("Adivinar el número del 1 al 100: "))

        if intento == num:
            print("Felicidades! Adivinaste el número.")
            jugar_de_nuevo = input("¿Quiere seguir jugando? (si/no): ")
            if jugar_de_nuevo.lower() != 'si':
                break

        elif intento < num:
            print("El numero es demasiado bajo. Intenta de nuevo.")
                
        else:
            print("El número es demasiado alto. Intenta de nuevo.")
            
        

juego_adivinar_num()                