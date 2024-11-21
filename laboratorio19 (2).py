#Parte 1: Condicionales
#- Escribir un programa que solicite al usuario un número por teclado y determine si es par o
#impar. Mostrar un mensaje adecuado en cada caso.
#- Escribir un programa que pida ingresar por teclado un número positivo de uno, dos o tres
#dígitos (1..999) mostrar un mensaje indicando si el número tiene uno, dos o tres dígitos.
n = int(input("Ingrese un numero"))
if n % 2 == 0:
    print("El numero es Par")
else:
    print("El numero es impar.")
if n <= 9:
    print("El numero tiene 1 digito")
elif n > 9 and n<=99:
    print("El numero tiene dos digitos")
else:
    print("el numero tiene 3 digitos")
#Parte 2: Bucles con Listas
#- Bucle while: En una empresa trabajan n empleados cuyos sueldos oscilan entre $1000000 y
#$5000000, realizar un programa que lea los sueldos que cobra cada empleado e informe
#cuántos empleados cobran entre $1000000 y $3000000 y cuántos cobran más de $3000000.
#Además el programa deberá informar el total que gasta la empresa en sueldos al personal.
n=int(input("Cuantos empleados tiene la empresa:"))
x=1
conta1=0
conta2=0
gastos=0
while x<=n:
    x = x + 1
    sueldo=float(input("Ingrese el sueldo del empleado:"))
 # continuar con el condicional
    if sueldo > 1000000 and sueldo < 3000000:
        conta1 = conta1 + 1
    else:
        conta2 = conta2 + 1
    gastos = gastos + sueldo
print("Los empleados que ganan entre $1000000 y $3000000 son",conta1)
print("Los empleados que ganan mas de $3000000 son",conta2)
print("En sueldos al personal la empresa gasta $",gastos)
#- Bucle For: Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos
#en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto
#cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
cant1=0
cant2=0
cant3=0
cant4=0
n=int(input("Cantidad de puntos:"))
for f in range(n):
    x=int(input("Ingrese coordenada x:"))
    y=int(input("Ingrese coordenada y:"))
    if x>0 and y>0:
        cant1 = cant1 + 1
    elif x<0 and y>0:
        cant2 = cant2 + 1
    elif x<0 and y<0:
        cant3 = cant3 + 1
    else:
        cant4 = cant4 + 1
print(f"En el primer cuadrante hay {cant1} puntos")
print(f"En el segundo cuadrante hay {cant2} puntos")
print(f"En el tercer cuadrante hay {cant3} puntos")
print(f"En el cuarto cuadrante hay {cant4} puntos")

#Parte 3: Diccionarios
# - Crear un diccionario que almacene los nombres de tres estudiantes y sus respectivas
#calificaciones. Escribir un programa que imprima el nombre del estudiante con la calificación
#más alta.
calificaciones = {
  "Juan": 5.0,
 "Ana": 4.2,
 "Luis": 4.5   
}
nombre_max = max(calificaciones, key=calificaciones.get)
print(f"El estudiante con la calificación más alta es {nombre_max} con una calificación
de {calificaciones[nombre_max]}.")

#Parte 4: Combinación de Estructuras
# - Escribir un programa que permita al usuario ingresar el nombre de un estudiante y su
#calificación. Si el estudiante ya existe en el diccionario, actualizar la calificación; si no existe,
#agregarlo al diccionario. Finalmente, mostrar todos los estudiantes y sus calificaciones.
estudiantes = {
 "Juan": 5.0,
 "Ana": 4.2,
 "Luis": 4.5
}
n = int(input("Cuantos estudiantes va a modificar:"))
for i in range (n):
    nombre = input("Ingresa el nombre del estudiante: ")
    nota = float(input("Ingresa la calificacion del estudiante: "))
    estudiantes[nombre] = nota
    print(f"La calificacion del estudiante {nombre} es {estudiantes[nombre]}")
print(estudiantes)
