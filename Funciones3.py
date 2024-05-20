'''
Ejercicio 3
Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha
función en un programa principal que lea el radio de una circunferencia y muestre su área y
perímetro.
'''
import math

#Funcion para calcular area y perimetro de una circunsferencia que recibe como dato el radio de la circunsferencia
def calcular_area_perimetro_circunferencia(radio):
    #Formula para calcular area "pi * radio al cuadrado"
    area = math.pi * radio ** 2
    #Formula para calcular perimetro "2 * pi * radio"
    perimetro = 2 * math.pi * radio

    return area, perimetro


try: 
    #Se le solicita al usuario que ingrese el radio y lo convierte a num flotante
    radio = float(input("Ingrese el radio de la circunsferencia: "))
    #Llama a la funcion para calcular el area y el perimetro con el radio proporcionado
    area, perimetro = calcular_area_perimetro_circunferencia(radio)
    #Imprime el area y el perimetro con dos decimales
    print(f"El area de la circunsferencia es: {area:.2f}\nEl perimetro de la circunferencia es: {perimetro:.2f}")
    #Si el usuario ingresa un valor no numerico muestra un msj de error
except ValueError:
    print("Por favor, ingrese un valor numérico para el radio.")    


