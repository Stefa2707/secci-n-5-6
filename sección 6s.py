# 1. Cree un programa que muestre los números naturales de 1 a n.
n = float(input (" ingrese un numero limite: "))

contador = 0
while (contador <= n):
    print(contador)
    contador += 1 

print ("--------------------------------------------------------------------------------------------------------------------------------------------")



# 2. Cree un programa que calcula la suma de los primeros n números naturales.


n = float(input("Ingrese un número límite: "))

contador = 0
suma = 0

while contador <= n:
    suma += contador
    contador += 1

print(f"La suma de los primeros {int(n)} números naturales es: {suma}")


print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 3. Cree un programa que muestre la tabla de multiplicar del 10, del 1 al 50

for i in range ( 51):
    print (f"{5} x {i} = {i*5} ")


print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 4. Cree un programa que muestre los números impares entre 1 y n

n = int(input("Ingrese un número para mostrar los impares hasta ese límite: "))

print(f"Números impares hasta {n}:")
for i in range(1, n + 1, 2):
    print(i)


print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 5. Cree un programa que pregunte al usuario si desea salir, si o no “S/N”, si el usuario teclea la letra S el programa se detendrá, de lo contrario continuará ejecutándose.


bandera = input ("ingrese s/n: ")
while (bandera != "s"):
    bandera = input ("ingrese s/n: ")
print ("gracias por usar nuestro programa: ")

print ("--------------------------------------------------------------------------------------------------------------------------------------------")



# 6. Cree un programa que calcule el promedio de 10 números


suma = 0

for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    suma += numero

promedio = suma / 10
print(f"El promedio de los 10 números ingresados es: {promedio}")

print ("--------------------------------------------------------------------------------------------------------------------------------------------")



# 7. Cree un programa que muestre el promedio de n números, dejándose de solicitar números cuando se introduzca el cero


suma = 0
contador = 0


while True:
    numero = float(input("Ingrese un número (0 para terminar): "))
    
    if numero == 0:
        break
    
    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"El promedio de los números ingresados es: {promedio}")
else:
    print("No se ingresaron números para calcular el promedio.")

print ("--------------------------------------------------------------------------------------------------------------------------------------------")



# 8. Cree un programa que calcule la suma de los cuadrados de los números entre 1 y n

n = int(input("Ingrese un número para calcular la suma de los cuadrados hasta ese límite: "))

suma_cuadrados = sum(i**2 for i in range(1, n + 1))

print(f"La suma de los cuadrados hasta {n} es: {suma_cuadrados}")