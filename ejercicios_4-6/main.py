#**Ejercicio Cuatro**
##Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# Mostrar la tabla de multiplicar del 1 al 10
for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()
 

#**Ejercicio Cinco**
##Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
# una a una las letras de la palabra introducida empezando por la última.

# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Mostrar las letras de la palabra introducida empezando por la última
for letra in reversed(palabra):
    print(letra)

#**Ejercicio Seis**
##Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo.

# Solicitar al usuario un número entero
numero = int(input("Ingrese un número entero: "))

# Mostrar un triángulo rectángulo con números en el patrón dado
for i in range(1, numero + 1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()