'''
Concatenar listas: Escribe una función que reciba dos listas y devuelva una nueva lista
que sea la concatenación de ambas.
'''

def concatenar_listas(lista_1, lista_2):
    return lista_1 + lista_2

lista_1 = [1,2,3]
lista_2 = [4,5,6]
resultado = concatenar_listas(lista_1,lista_2)
print(f"Listas concatenadas:{resultado}")