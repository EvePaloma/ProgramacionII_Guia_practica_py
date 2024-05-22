'''
6. Contar elementos: Escribe una función que reciba una lista y un valor, y devuelva
cuántas veces aparece ese valor en la lista.
'''

def contar_elementos(lista, n):
    return lista.count(n)

num = [10,9,5,2,6,8,9,2]
n = 9
resultado = contar_elementos(num, n)
print(f"El valor aparece {resultado} veces.")

