'''
Diccionario inverso: Escribe una función que tome un diccionario y devuelva uno
nuevo que invierta las claves y los valores.
'''

def diccionario_inverso(diccionario):
    diccionario_invertido = {}

    for clave,valor in diccionario.items():
        diccionario_invertido[valor] = clave

    return diccionario_invertido

diccionario = {"Maria":25, "Esteban":28,"Pablo":26, "Carolina":27}
diccionario_invertido = diccionario_inverso(diccionario)
print(f"Su nuevo diccionario es: {diccionario_invertido}")    