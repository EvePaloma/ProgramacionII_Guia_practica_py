'''
Filtrar diccionario: Escribe una función que reciba un diccionario y una lista de claves,
y devuelva un nuevo diccionario solo con las claves especificadas.
'''

def filtrar_diccionario(diccionario,claves):
    #nuevo diccionario para guardar solo las claves
    nuevo_diccionario = {}

    #recorre cada clave en la lista de claves
    for clave in claves:
        if clave in diccionario:
            nuevo_diccionario[clave] = diccionario[clave]

    return nuevo_diccionario

diccionario = {'a':2,'b':4,'c':6}
claves_a_filtrar = ['a','c','z']
diccionario_filtrado = filtrar_diccionario(diccionario,claves_a_filtrar)
print(f"Las claves que filtró son: {diccionario_filtrado}")


