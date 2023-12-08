# 1. Cree un programa que imprima los números enteros entre 0 y 100 en orden ascendente y descendente.

print ('------ascendente-------')

for i in range(101):
    print(i+1)
    
    
print ('------ascendente-------')

for i in range (100,-1,-1):
    print (i)

print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 2. Cree un programa que imprima la tabla de multiplicar del 3, del 0 al 50

for i in range ( 51):
    print (f"{3} x {i} = {i*3} ")

print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 3. Cree un programa que calcule el promedio de tres notas para n estudiantes.

estudiante = int(input ("ingese el numero de estudiantes"))

for i in range (estudiante):
    
    nombre = input ("ingrese nombre: ")
    n1 = int(input("ingrese la primera nota : "))
    n2 = int(input("ingrese la segunda nota: "))
    n3 = int(input("ingrese la tercera nota: "))
    promedio = (n1 + n2 + n3 )/ 3
    
    print ("nombre del estudiante: ", nombre)
    print ("el promedio es: ", promedio) 


print ("--------------------------------------------------------------------------------------------------------------------------------------------")



# 4. Cree un programa que dado un número entero n, calcule su factorial(n!).


def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

try:
    n = int(input("Ingrese un número entero para calcular su factorial: "))
    
    if n >= 0:
        resultado = calcular_factorial(n)
        print(f"El factorial de {n} es: {resultado}")
    else:
        print("Por favor, ingrese un número entero no negativo.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")


