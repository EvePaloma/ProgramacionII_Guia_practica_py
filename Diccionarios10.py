'''
10.Valores únicos: Escribe una función que reciba un diccionario y devuelva una lista de
valores únicos en el diccionario.
'''

def valores_unicos(diccionario):
    valores_unicos = []

    for valor in diccionario.values():
        if valor not in valores_unicos:
            valores_unicos.append(valor)

    return valores_unicos

diccionario = {'a':10,'b':20,'c':30,'d':20,'e':35,'f':20,'g':10}
resultado = valores_unicos(diccionario)
print(f"La lista de valores únicos en el diccionario es:{resultado}")        