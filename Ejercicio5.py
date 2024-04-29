#Mejora el programa de conversión de temperatura que escribiste anteriormente 
#para que permita al usuario elegir entre convertir de grados Celsius a grados Fahrenheit o viceversa.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

continuar = True

while continuar:
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    print("3. Salir")
    opcion = int(input("Selecciona una opcion (1,2 o 3)"))
    
    
    if opcion == 1:
        celsius = float(input("Ingresa la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print("La temperatura en Fahrenheit es: ", fahrenheit)
        
    elif opcion == 2:
        fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print("La temperatura en Celsius es: ", celsius)    
    
    elif opcion == 3:
        print("Hasta luego!")
        continuar = False

    else:
        print("Opcion no valida. Por favor, selecciona 1,2 o 3")        