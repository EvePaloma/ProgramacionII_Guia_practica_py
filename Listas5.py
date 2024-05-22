'''
5. Eliminar duplicados: Crea una función que tome una lista y devuelva una nueva lista
sin elementos duplicados.
'''

def eliminar_duplicados(lista):

    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)

    return lista_sin_duplicados

lista_con_duplicados = [2,3,6,8,4,6,2,9,3]
resultado = eliminar_duplicados(lista_con_duplicados)
print(f"Lista sin duplicados:{resultado}")        