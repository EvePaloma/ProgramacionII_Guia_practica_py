'''
Merge de diccionarios: Crea una función que tome dos diccionarios y devuelva uno
nuevo que combine ambos (en caso de conflicto, usa los valores del segundo
diccionario).
'''

def merge_de_diccionarios(diccionario_1,diccionario_2):
    diccionarios_combinados = {}

    for clave,valor in diccionario_1.items():
        diccionarios_combinados[clave] = valor

    for clave,valor in diccionario_2.items():
        diccionarios_combinados[clave] = valor

    return diccionarios_combinados

diccionario_1 = {'a':2,'b':3,'c':6}
diccionario_2 = {'b':4,'d':8,'e':10}
diccionarios_combinados = merge_de_diccionarios(diccionario_1,diccionario_2)
print(f"Diccionario combinado: {diccionarios_combinados}")         

