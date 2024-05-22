'''
2. Máximo y mínimo: Escribe una función que reciba una lista de números y devuelva el
valor máximo y el mínimo de la lista.
'''

def maximo_minimo(lista):
    maximo = max(lista)
    minimo = min(lista)

    return maximo, minimo

num = [50,35,89,34,200]
maximo, minimo = maximo_minimo(num)
print("El máximo es: ", maximo)
print("El mínimo es: ", minimo)
