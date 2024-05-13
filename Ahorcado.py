import random

palabras = ["programacion", "desarrollador", "analista", "github",
            "ejecutar", "documentos", "usuario", "ahorcado"]

palabra = list(random.choice(palabras))

palabra_oculta = ['_']*len(palabra)
intentos = 6
letras = list("abcdefghijklmnñopqrstuvwxyz")
letras_descartadas = []

def mostrar_estado():
    print(f"Intentos restantes: {intentos}")
    print(f"Letras descartadas: {", ".join(letras_descartadas)}\n")
    print(f"Palabra: {" ".join(palabra_oculta)}\n")


#verificación de la letra valida
def letra_valida(letra):
    if len(letra) != 1:
        print("Has puesto mas de una letra, inténtalo de nuevo")
        return False
    elif letra not in letras:
        print("No has introducido una letra del abecedario")
        return False
    elif letra in palabra_oculta:
        print("La letra que introduciste ya la acertaste, inténtalo de nuevo")
        return False
    elif letra in letras_descartadas:
        print("Esa letra ya la habias dicho, inténtalo de nuevo")
        return False
    else:
        return True
    
def adivinar_letra(letra):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
            #palabra_oculta[i] = '_'
            
print("***BIENVENIDO AL JUEGO DEL AHORCADO***\n")
print(f"TIENES {intentos} INTENTOS. BUENA SUERTE!\n")
print(f"LA PALABRA TIENE {len(palabra_oculta)} LETRAS\n")

while intentos > 0 and '_' in palabra_oculta:
    mostrar_estado()
    print("-"*50)
    letra = input("INTRODUCE UNA LETRA: ").lower()

    while not letra_valida(letra):
        letra = input("INTRODUCE OTRA LETRA").lower()

    if letra in palabra:
        adivinar_letra(letra)
        print("-"*50)   
        print("¡HAS ACERTADO LA LETRA!\n")
    else:
        print("-"*50)
        print("HAS FALLADO")
        letras_descartadas.append(letra)
        intentos -=1
        

if "_" not in palabra_oculta:
    print("\n\n ***¡HAS GANADO!***")
else:
    print("***¡HAS PERDIDO!***") 
    print(f"La palabra era: {"".join(palabra)}")    

print()               

    