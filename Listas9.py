'''
Producto de elementos: Escribe una función que tome una lista de números y
devuelva el producto de todos los elementos.
'''

def producto_de_elemento(lista):
    producto = 1

    for elemento in lista:
        producto = elemento * producto
    return producto

num = [1,2,3,4,5]
resultado = producto_de_elemento(num)
print(f"El producto del elemento es:{resultado}")

