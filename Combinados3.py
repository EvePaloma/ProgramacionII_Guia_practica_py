'''
Diccionario de listas: Escribe una función que tome un diccionario donde los valores
son listas y devuelva una lista que contenga todos los elementos de las listas del
diccionario.
'''
def diccionario_listas(diccionario):
    elementos_combinados = []

    for lista in diccionario.values():
        for elemento in lista:
            elementos_combinados.append(elemento)

    return elementos_combinados

diccionario = {"lista_1":[10,20,30],"lista_2":["a","b","c"]}
elementos_combinados = diccionario_listas(diccionario)
print(f"Los elementos de las listas son:{elementos_combinados}")        