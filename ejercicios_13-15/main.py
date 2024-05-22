#**Ejercicio Trece**
##Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos `SAL` no se apaga.
#
##Esta calculadora funciona de la siguiente manera:
#
##- Recogemos los datos A y B
##- Si operación es 1 calcula la raíz cuadrada de la suma de A y B
##- Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
##- Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5

# Función para calcular la raíz cuadrada de la suma de A y B
def calcular_raiz_cuadrada_suma(A, B):
    return (A + B) ** 0.5

# Función para calcular A / B
def calcular_division(A, B):
    return A / B if B != 0 else "Error: No se puede dividir por cero."

# Función para calcular (A * B) / 2.5
def calcular_formula(A, B):
    return (A * B) / 2.5

# Encender la calculadora
while True:
    # Solicitar al usuario los datos A, B y la operación
    A = float(input("Ingresa el valor de A: "))
    B = float(input("Ingresa el valor de B: "))
    operacion = int(input("Selecciona la operación (1: Raíz cuadrada de la suma, 2: División, 3: Fórmula): "))

    # Realizar la operación correspondiente
    if operacion == 1:
        resultado = calcular_raiz_cuadrada_suma(A, B)
    elif operacion == 2:
        resultado = calcular_division(A, B)
    elif operacion == 3:
        resultado = calcular_formula(A, B)
    else:
        resultado = "Operación no válida."

    # Mostrar el resultado de la operación
    print("El resultado de la operación es:", resultado)

    # Verificar si se debe apagar la calculadora
    if input("¿Deseas continuar (SAL para salir)? ") == "SAL":
        break


#**Ejercicio Catorce**
##Tenemos la pantalla del móvil bloqueada. Partiendo de un `PIN_SECRETO`, intentaremos desbloquear 
# la pantalla. Tenemos hasta 3 intentos. Simula el proceso con Python. En caso de acceder, lanza al 
# usuario `login correcto`. Sino, `llamando ala policía`.

pin_secreto:str="2005"
intentos_restantes:int=3
while intentos_restantes >0 :
    pin_usuario:str=input("ingrese un PIN: ")
    if pin_usuario == pin_secreto:
        print("login correcto")
        break
    else:
        intentos_restantes -= 1
        if intentos_restantes >0:
            print(f"te quedan {intentos_restantes} intentos restantes")
        else:
            print("has agotado tus intentos.  Llamando a la policia")

#**Ejercicio Quince**
##Crea un algoritmo para la sucesión de Fibonacci. La sucesión de Fibonacci es la siguiente serie:
#
##`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89`
#
##Pista: Empezando por 0 y 1, el siguiente número es la suma de los dos números últimos.

a, b = 0, 1
print(a)
contador = 1
n = 10
while contador < n:
    a, b = b, a + b
    print(a)
    contador += 1
