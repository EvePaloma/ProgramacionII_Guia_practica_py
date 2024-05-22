'''
4. Elementos mayores que un valor: Escribe una función que tome una lista de números
y un valor n, y devuelva una nueva lista con los elementos mayores que n.
'''

def elementos_mayores_n(lista, n):

    return[elemento for elemento in lista if elemento > n]

num = [7,5,9,16]
n = 8
resultado = elementos_mayores_n(num, n)
print("Números mayores que n: ", resultado)