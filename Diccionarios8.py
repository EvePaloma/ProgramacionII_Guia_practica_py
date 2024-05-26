'''
Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y
devuelva un diccionario con la frecuencia de cada palabra.
'''

def diccionario_de_frecuencias(palabras):
    frecuencias = {}

    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1    

    return frecuencias

palabras = ['programacion','clave','valor','ejercicios','valor','sumar','ejercicios']
resultado = diccionario_de_frecuencias(palabras)
print(f"La frecuencia de cada palabra es de:{resultado}")