'''
Ejercicio 2
Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
máximo y el mínimo, utilizando la función anterior.
'''

def calcular_max_min(lista):
    maximo = lista[0]
    minimo = lista[0]

    for num in lista:
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num

    return maximo, minimo

usuario = input("Ingrese los números separados por espacios: ")
numeros = [float(num) for num in usuario.split()]
maximo, minimo = calcular_max_min(numeros)
print(f"El maximo es: {maximo}\nEl mínimo es: {minimo}")
