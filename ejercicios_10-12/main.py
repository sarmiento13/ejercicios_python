#**Ejercicio Diez**
##Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre 
# por pantalla el número de veces que aparece la letra en la frase.

# Solicitar al usuario una frase y una letra
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

# Contar el número de veces que aparece la letra en la frase
contador = frase.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en la frase.")

#**Ejercicio Once**
##Escriba un programa que pregunte cuantos números se van a introducir, pida los esos números
# (que puedan ser decimales) y calcule su suma, mostrar por terminal la suma de los números introducidos.

# Solicitar al usuario cuántos números va a introducir
cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))

# Inicializar la variable para almacenar la suma de los números
suma = 0

# Pedir los números al usuario y calcular la suma
for i in range(cantidad_numeros):
    numero = float(input("Introduce un número: "))
    suma += numero

# Mostrar la suma de los números introducidos por terminal
print("La suma de los números introducidos es:", suma)

#**Ejercicio Doce**
##Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y
# escriba cuántos negativos ha introducido.

# Pedir al usuario cuántos números se van a introducir
num_numeros = int(input("¿Cuántos números vas a introducir? "))

# Inicializar contador de números negativos
contador_negativos = 0

# Pedir los números al usuario y contar los negativos
for i in range(num_numeros):
    numero = int(input(f"Introduce el número {i+1}: "))
    if numero < 0:
        contador_negativos += 1

# Mostrar la cantidad de números negativos introducidos
print(f"Has introducido {contador_negativos} números negativos.")