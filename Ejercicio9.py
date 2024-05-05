'''
Ejercicio 9: Calculadora de Factorial 
Desarrolla una calculadora que calcule el factorial de un número ingresado por el usuario.
 El factorial de un número entero positivo n se define como el producto de todos 
los enteros positivos menores o iguales a n. El programa debe manejar números enteros grandes y mostrar 
el resultado.
'''

def factorial(n):
    if n < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

while True:
        num = int(input("Ingrese un número entero para calcular su factorial: "))
        resultado_factorial = factorial(num)
        print("El factorial de", num, "es: ", resultado_factorial)

