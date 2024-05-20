'''
Ejercicio 4
Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te
devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido
hacer login incremente este valor, validar con otra función la cantidad de intentos posibles en
3 oportunidades.
'''

#Funcion para validar si se superaron los intentos permitidos
def validar_intentos(intentos):
    #Retorna True si los intentos son menores a 3
    return intentos < 3

#Funcion para verificar inicio de sesion
def login(nombre_usuario, contraseña, intentos):
    usuario_correcto = "usuario1"
    contraseña_correcta = "asdasd"
    #Si el nombre de usuario y la contraseña son correctas retorna True y los intentos sin cambios
    if nombre_usuario == usuario_correcto and contraseña == contraseña_correcta:
        return True, intentos
    #Si usuario y contraseña son incorrectas incrementa los intentos en 1 y muestra msj de error.
    else:
        intentos += 1
        print("Nombre de usuario o contraseña incorrectos. Inténtelo de nuevo.")
        #Devuelve False con los intentos actualizados
        return False, intentos

#Incializa en 0 el contador de intentos 
intentos = 0

#Este bucle se ejecuta mientras los intentos sean menores a 3
while validar_intentos(intentos):
    usuario = input("Ingrese el usuario: ")
    contraseña = input("Ingrese contraseña: ")
    #Se intenta iniciar sesion y actualiza los intentos
    login_exitoso, intentos = login(usuario,contraseña,intentos)
    #Si el inicio de sesion es exitoso imprime "Verdadero" y sale de bucle
    if login_exitoso:
        print("Verdadero")
        break
    else:
        #Si alcanza el maximo permitido de intentor imprime el msj y sale del bucle
        if intentos == 3:
            print("Se alcanzó el máximo de intentos permitidos.")        
            break
        else:
            #Si hay intentos disponibles, muestra el num de intentos
            print(f"Intento {intentos} de inicio de sesión")

