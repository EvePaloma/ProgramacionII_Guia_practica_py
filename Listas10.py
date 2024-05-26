'''
10.Encontrar índice: Escribe una función que reciba una lista y un valor, y devuelva el
índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.
'''

def encontrar_indice(lista, n):
    if n in lista:
        return lista.index(n)
    else:
        return -1
    
num = [10,20,30,40,50]
valor_a_buscar = 40
resultado = encontrar_indice(num,valor_a_buscar)
print(f"El índice de la primer aparición del valor {valor_a_buscar} es {resultado}")    