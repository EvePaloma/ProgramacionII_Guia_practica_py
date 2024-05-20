'''
Ejercicio 5
Crear una función recursiva que permita calcular el factorial de un número. Realiza un
programa principal donde se lea un número validado como entero, el cual es ingresado por
el usuario y se muestre el resultado del factorial.
'''

def calcular_factorial(n):
    if n < 0:
        return "No se puede calcular el factorial de un numero negativo."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado = resultado * i
        return resultado
        
while True:
    num = int(input("Ingrese un número entero para calcular su factorial: "))
    resultado_factorial = calcular_factorial(num)
    print(f"El factorial de {num} es: {resultado_factorial}")      