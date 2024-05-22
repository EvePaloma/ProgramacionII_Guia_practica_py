'''
3. Promedio de una lista: Crea una función que calcule el promedio de los números en
una lista dada.
'''

def promedio(lista):
    promedio = sum(lista) / len(lista)

    return promedio

num = [10,20,30,40]
resultado = promedio(num)
print("El promedio es:", resultado)