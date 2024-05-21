#**Ejercicio Siete**
##Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
#el número de veces que aparece la letra en la frase.

# Solicitar al usuario una frase y una letra
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

# Contar el número de veces que aparece la letra en la frase
contador = frase.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en la frase.")

#**Ejercicio Ocho**
##Escribir un programa que pida al usuario una palabra y luego muestre por pantalla la primera letra la 
#letra que se encuentra en medio y la ultima letra separadas por comas(,).

# Solicitar al usuario ingresar una palabra
palabra = input("Ingresa una palabra: ")

# Obtener la longitud de la palabra
longitud = len(palabra)

# Inicializar una variable para almacenar las letras del medio
letras_medio = ""

# Determinar las letras del medio
inicio = longitud // 2 - 1 if longitud % 2 == 0 else longitud // 2
fin = inicio + 2 if longitud % 2 == 0 else inicio + 1

# Construir las letras del medio separadas por comas
for i in range(inicio, fin):
    letras_medio += palabra[i] + ("," if i != fin - 1 else "")

# Mostrar las letras separadas por comas
print("Las letras son:", palabra[0] + "," + letras_medio + "," + palabra[-1])

#**Ejercicio Nueve**
##Escriba un programa que pregunte cuántos números se van a introducir, luego pida esos números, y muestre 
#un mensaje cada vez que un número no sea mayor que el anterior.

cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))

if cantidad_numeros > 0:
    numero_anterior = int(input("Introduce el primer número: "))
    for i in range(1, cantidad_numeros):
        numero_actual = int(input("Introduce el siguiente número: "))
        if numero_actual <= numero_anterior:
            print("El número introducido no es mayor que el anterior.")
        numero_anterior = numero_actual
else:
    print("No se han introducido números.")