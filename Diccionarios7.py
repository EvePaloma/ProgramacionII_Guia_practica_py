'''
Sumar valores: Escribe una función que reciba un diccionario con valores numéricos y
devuelva la suma de todos los valores.
'''

def suma_de_valores(diccionario):
    return sum(diccionario.values())

diccionario = {'a':10,'b':20,'c':30}
resultado = suma_de_valores(diccionario)
print(f"La suma de los valores es: {resultado}")