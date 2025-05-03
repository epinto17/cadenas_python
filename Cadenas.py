def logica_programa(opcion):
    if (opcion == 1):
        print ("Programa que multiplica el Nombre")
        nombre = str(input("Ingresa tu nombre: "))
        cantidad = int(input("Ingresa un numero para multiplicar el nombre: "))

        for i in range(cantidad):
            print (f"{i+1}: {nombre}")

    elif (opcion == 2):
        print ("Programa que imprime el nombre en tres estilos.")
        nombre = str(input("Ingresa tu nombre completo: "))

        print ("En minúsculas: ", nombre.lower())
        print ("En mayúsculas: ", nombre.upper())
        print ("Inicial maýuscula: ", nombre.title())

    elif (opcion == 3):
        print ("Programa que cuenta las letras del nombre")
        nombre = str(input("Escriba su nombre: "))

        print (f"{nombre.upper()} tiene {len(nombre)} letras.")

    elif (opcion == 4):
        print ("Programa que formatea el numero de telefono")
        print ("Formato del número: +502-12345678-XX")
        numero_telefono = str(input("Ingrese su número de teléfono: "))

        print ("El numero de telefono sin formato es: ",numero_telefono[5:13])

    elif (opcion == 5):
        print ("Programa que invierte un texto")
        frase = str(input("Ingresa una frase: "))

        print ("Frase invertida: ",frase[::-1])

    elif (opcion == 6):
        print ("Programa que cambia una vocal a mayúscula")
        frase = str(input("Ingresa una frase: "))
        vocal = str(input("Ingresa una vocal: ")).lower()

        print ("Con vocal mayúscula: ", frase.replace(vocal, vocal.upper()))

    elif (opcion == 7):
        print ("Programa que cambia de dominio al correo")
        correo = str(input("Ingrese su correo electrónico: "))
        usuario = correo[:correo.find("@")]

        print (f"Dominio UPANA: {usuario}@upana.edu.gt")
        
    elif (opcion == 8):
        print ("Programa que separa decimales")
        precio = str(input("Ingrese el precio del producto: "))
        quetzales = precio[:precio.find(".")]
        centavos = precio[precio.find(".")+1:]

        print (f"El producto tiene un costo de Q. {quetzales} y {centavos} centavos.")

    elif (opcion == 9):
        print ("Programa que muestra la fecha de cumpleaños por separado")
        print ("Formato de fecha: dd/mm/aaaa")
        fecha = str(input("Ingrese su fecha de nacimiento: "))

        separador = fecha.split("/")
        dia = separador[0]
        mes = separador[1]
        anio = separador[2]

        print (f"Día: {dia} \nMes: {mes} \nAño: {anio}")

    elif (opcion == 10):
        print ("Programa que separa lista de compra")
        print ("Productos separados por coma: tomate, zanahoria, etc")
        lista_compra = str(input("Ingrese la lista de compra: "))

        productos = lista_compra.split(", ")

        for i, producto in enumerate(productos, start=1):
            print (f"{i}: {producto}")

    else:
        print ("La opción ingresada no es válida.")
    
    global continuar
    seguir = str(input("¿Desea probar otro programa? Si / No: ")).lower()

    if (seguir == "si"):
        continuar = True
    elif (seguir == "no"):
        continuar = False
    else:
        print ("Opcion no válida...")

def menu():
    print ("Ejercicios con Cadenas")
    print ("""
        1. Ejercicio 1
        2. Ejercicio 2
        3. Ejercicio 3
        4. Ejercicio 4
        5. Ejercicio 5
        6. Ejercicio 6
        7. Ejercicio 7
        8. Ejercicio 8
        9. Ejercicio 9
        10. Ejercicio 10
    """)

    opcion = int(input("Seleccione un programa: "))
    logica_programa(opcion)

continuar = True
while (continuar):
    menu()