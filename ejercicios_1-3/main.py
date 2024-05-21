#**Ejercicio Uno**
##Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 puede entrar gratis, si tiene entre 4 y 18 debe pagar 5 soles, y 
# si es mayor de 18 deberá pagar 10 soles.

# Solicitar la edad del cliente al usuario
edad = int(input("Ingrese la edad del cliente: "))

# Calcular el precio de la entrada según la edad
if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10

# Mostrar el precio de la entrada por terminal
print("El precio de la entrada es:", precio, "soles")

#**Ejercicio Dos**
##Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces

# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Mostrar la palabra 10 veces por terminal
for _ in range(10):
    print(palabra)

#**Ejercicio Tres**
##Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
#los números impares desde 1 hasta ese número separados por comas.

# Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Mostrar los números desde 1 hasta el número dado
print("Números desde 1 hasta", numero, ":")
for i in range(1, numero + 1):
    print(i, end=" ")
 