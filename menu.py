#Corrección
#Importamos la libreria hashlib necesaria para el funcionamiento del menú.

import hashlib

#Definimos la función encargada de pedir el número para el menú.
def pedirNumeroEntero():
    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input("Introduce una opcion del 1 al 5: "))
            correcto = True
        #La función except se utiliza cuando el usario no introduce un numero entero, mostrando un mensaje de error para
        # evitar que el programa se cierre al cometer un error.
        except ValueError:
            print('Error!! introduce un numero entero')

    return num

#Definimos una función que se ejecutará cuando elijamos la opción 2 de nuestro menú, con ayuda de la librería
# hashlib esta función sirve para codificar un fichero y crear un resumen MD5 y mostrarlo en hexadecimal.
def md5sum(filename):
    f = open(filename, mode='r')
    d = hashlib.md5()
    for buf in f.read(128):
        d.update(buf.encode())
    return d.hexdigest()


#Definimos una función que se ejecutará cuando elijamos la opción 4 de nuestro menú, con ayuda de la librería
# hashlib esta función sirve para codificar un fichero y crear un resumen SHA1 y mostrarlo en hexadecimal.
def sha1sum(filename):
    f = open(filename, mode='r')
    d = hashlib.sha1()
    for buf in f.read(128):
        d.update(buf.encode())
    return d.hexdigest()

#Definimos el menú al mostrar, el cuál se mostrará hasta que le indiquemos el número 5, el cuál significa salir
# del menú.
salir = False
opcion = 0

while not salir:

    print("1. Resumen MD5 de una cadena")
    print("2. Resumen MD5 de un fichero")
    print("3. Resumen SHA1 de una cadena")
    print("4. Resumen SHA1 de un fichero")
    print("5. Salir")

    print("Elige una opcion")

    opcion = pedirNumeroEntero()


#La opción numero 1 utiliza la librería hashlib para crearnos un resumen MD5 y mostrarlo en hexadecimal
# de una cadena de caracteres que le indiquemos.
    if opcion == 1:
        cadena1 = str(input("Introduce la cadena de caracteres para hacer el resumen MD5: "))
        print(hashlib.md5(cadena1.encode('utf-8')).hexdigest())

#La opción numero 2 utiliza la función que hemos definido anteriormente como md5sum(filename) para crear un resumen
# md5 de un fichero que le indiquemos.
    elif opcion == 2:
        fichero1 = str(input("Introduce el fichero para hacer el resumen MD5: "))
        print(md5sum(fichero1))

#La opción numero 3 utiliza la librería hashlib para crearnos un resumen SHA1 y mostrarlo en hexadecimal de una
# cadena de caracteres que le indiquemos.
    elif opcion == 3:
        cadena2 = str(input("Introduce la cadena de la que se hara el resumen en SHA1: "))
        print(hashlib.sha1(cadena2.encode('utf-8')).hexdigest())

#La opción 4 del menú utiliza la función sha1sum(filename) que hemos definido anteriormente para crear un resumen
# sha1 de un fichero que le indiquemos.
    elif opcion == 4:
        fichero2 = str(input("Introduce la ruta del fichero del que se hara el resumen en SHA1: "))
        print(sha1sum(fichero2))

#La opción 5 cerrará el menú y acabará con su ejecución en bucle, ya que anteriormente hemos definido que
# el menú se estará ejecutando en bucle hasta que seleccionemos esta opción.
    elif opcion == 5:
        salir = True
    else:
        print("Introduce una opcion del 1 al 5: ")

print("Fin")
