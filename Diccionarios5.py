'''
Diccionario de cuadrados: Escribe una función que reciba un número n y devuelva un
diccionario con los números de 1 a n como claves y sus cuadrados como valores.
'''

def diccionario_de_cuadrados(n):
    diccionario = {}

    for i in range(1,n +1):
        diccionario[i] = i**2

    return diccionario

n = 10
resultado = diccionario_de_cuadrados(n)
print(f"Los números son: {resultado}")    