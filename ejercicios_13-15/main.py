#**Ejercicio Trece**
##Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos `SAL` no se apaga.
#
##Esta calculadora funciona de la siguiente manera:
#
##- Recogemos los datos A y B
##- Si operación es 1 calcula la raíz cuadrada de la suma de A y B
##- Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
##- Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5




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
