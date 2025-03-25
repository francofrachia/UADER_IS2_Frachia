#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) < 2:
    input_range = input("Ingrese un rango de números (ej. 4-8): ")
else:
    input_range = sys.argv[1]

# Parseo el rango de números
try:
    start, end = map(int, input_range.split('-'))
    if start > end:
        print("El número inicial debe ser menor o igual al final.")
        sys.exit()
except ValueError:
    print("El formato del rango no es válido. Use el formato 'inicio-fin', como '4-8'.")
    sys.exit()

# Calcular los factoriales para cada número en el rango
for num in range(start, end + 1):
    print(f"Factorial {num}! es {factorial(num)}")

