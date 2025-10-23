""" Entrar com 8 números e , para cada número, imprimir o logaritmo
desse número na base 10. """

import math

numeros = []

for i in range(8):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

print("\nLogaritmos na base 10:")
for numero in numeros:
    logaritmo = math.log10(numero)
    print(f"O logaritmo de {numero} na base 10 é: {logaritmo}")