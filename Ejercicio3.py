#Escribe un programa en Python que solicite al usuario que ingrese 
#la base y la altura de un triángulo, y luego calcule y muestre el área del triángulo.

base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))

area = (base * altura) / 2

print("El area del triangulo es: ", area)