""" Entrar com um número e imprimir a raiz quadrada do número caso
ele seja positivo e o quadrado do número caso ele seja negativo. """

import math

num_str = input("Digite um número: ")

try:
    numero = float(num_str)

    if numero >= 0:
        
        resultado = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é: {resultado:.2f}")
    else:
        
        resultado = numero ** 2
        print(f"O quadrado de {numero} é: {resultado:.2f}")

except ValueError:
    
    print("Entrada inválida. Por favor, digite um número.")
