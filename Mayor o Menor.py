# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 09:44:27 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""


def mayor_menor(x, y):
    if x > y:
        mayor = x
        menor = y
    else:
        menor = x
        mayor = y
    return mayor, menor


numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese otro número entero: "))

num_mayor, num_menor = mayor_menor(numero1, numero2)

print(f"El número mayor es {num_mayor} y el número menor es {num_menor}")
