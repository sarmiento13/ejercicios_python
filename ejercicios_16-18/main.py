#**Ejercicio Dieciséis**
##Desarrolla un programa en Python que permita gestionar una lista de tareas pendientes. El programa
# debe cumplir con los siguientes requisitos:
#
##- Debe permitir agregar nuevas tareas a la lista.
##- Debe permitir marcar tareas como completadas, lo que las eliminará de la lista de tareas pendientes.
##- Debe mostrar la lista actual de tareas pendientes.
##- Debe proporcionar un menú interactivo que permita al usuario seleccionar entre las opciones anteriores 
# y salir del programa.
##El menú debe presentar las siguientes opciones:
#
##- Agregar tarea
##- Marcar tarea como completada
##- Mostrar tareas
##- Salir

# Lista de tareas pendientes
tareas = []

# Menú interactivo
while True:
    print("\nMenú de opciones:")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        tareas.append(input("Ingrese la nueva tarea: "))
        print("Tarea agregada exitosamente.")
    elif opcion == "2":
        if tareas:
            print("Tareas pendientes:")
            for i, tarea in enumerate(tareas):
                print(f"{i + 1}. {tarea}")
            num_tarea = int(input("Ingrese el número de la tarea completada: "))
            if 1 <= num_tarea <= len(tareas):
                tarea_completada = tareas.pop(num_tarea - 1)
                print(f"Tarea '{tarea_completada}' marcada como completada.")
            else:
                print("Número de tarea inválido.")
        else:
            print("No hay tareas pendientes.")
    elif opcion == "3":
        if tareas:
            print("Tareas pendientes:")
            for i, tarea in enumerate(tareas):
                print(f"{i + 1}. {tarea}")
        else:
            print("No hay tareas pendientes.")
    elif opcion == "4":
        print("¡Gracias por utilizar la lista de tareas pendientes!")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

#**Ejercicio Diecisiete**
##Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir
# al usuario realizar las siguientes operaciones:
#
##- Verificar el saldo de su cuenta.
##- Depositar dinero en su cuenta.
##- Retirar dinero de su cuenta.
##- Salir del programa.
##El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:
#
##- Verificar saldo
##- Depositar dinero
##- Retirar dinero
##- Salir

# Saldo inicial del cajero automático
saldo = 1000

# Menú interactivo del cajero automático
while True:
    print("\nMenú de opciones:")
    print("1. Verificar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Su saldo actual es: ${saldo}")
    elif opcion == "2":
        monto_deposito = float(input("Ingrese la cantidad a depositar: $"))
        saldo += monto_deposito
        print(f"Se han depositado ${monto_deposito}. Saldo actual: ${saldo}")
    elif opcion == "3":
        monto_retiro = float(input("Ingrese la cantidad a retirar: $"))
        if monto_retiro <= saldo:
            saldo -= monto_retiro
            print(f"Ha retirado ${monto_retiro}. Saldo actual: ${saldo}")
        else:
            print("Saldo insuficiente.")
    elif opcion == "4":
        print("¡Gracias por utilizar el cajero automático!")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

#**Ejercicio Dieciocho**
##Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a 
# solicitar hasta que las dos contraseñas coincidan.

# Solicitar y validar la contraseña
while True:
    contraseña1 = input("Ingrese la contraseña: ")
    contraseña2 = input("Confirme la contraseña: ")

    if contraseña1 == contraseña2:
        print("Contraseña confirmada. ¡Contraseñas coinciden!")
        break
    else:
        print("Las contraseñas no coinciden. Inténtelo de nuevo.")