""" Entrar com um número e imprimir o logaritmo desse número na
base 10. """

import math

# Solicita ao usuário que insira um número
numero_str = input("Por favor, insira um número: ")

# Converte a entrada para um número de ponto flutuante
numero = float(numero_str)

# Calcula o logaritmo na base 10
logaritmo_base_10 = math.log10(numero)

# Imprime o resultado
print(f"O logaritmo de {numero} na base 10 é: {logaritmo_base_10}")