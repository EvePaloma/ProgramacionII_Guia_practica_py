'''
Agrupar por longitud: Escribe una función que reciba una lista de palabras y devuelva
un diccionario donde las claves son las longitudes de las palabras y los valores son
listas de palabras con esa longitud.
'''

def agrupar_por_longitud(lista_palabras):
    diccionario = {}

    for palabra in lista_palabras:
        longitud = len(palabra)
        if longitud in diccionario:
            diccionario[longitud].append(palabra)
        else:
            diccionario[longitud] = [palabra]

    return diccionario

palabras = ['programacion','clave','valor','sumar','ejercicios'] 
resultado = agrupar_por_longitud(palabras)
print(f"Diccionario por longitud:{resultado}")          
    