""" Entrar com um ângulo em graus e imprimir: seno, co-seno,
tangente, secante, co-secante e co-tangente deste ângulo. Use o módulo math. """

import math

# Solicita o ângulo em graus ao usuário
try:
    angulo_graus = float(input("Digite um ângulo em graus: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
else:
    # Converte o ângulo de graus para radianos
    angulo_radianos = math.radians(angulo_graus)

    # Calcula e imprime as funções trigonométricas principais
    seno = math.sin(angulo_radianos)
    cosseno = math.cos(angulo_radianos)
    tangente = math.tan(angulo_radianos)

    print(f"\nSeno: {seno:.4f}")
    print(f"Co-seno: {cosseno:.4f}")

    # Calcula e imprime as funções trigonométricas recíprocas
    # Lida com casos em que o denominador é zero (cosseno ou seno = 0)
    if abs(cosseno) < 1e-9: # Se o cosseno for muito próximo de zero
        secante = "Indefinido"
        tangente = "Indefinido"
    else:
        secante = f"{1 / cosseno:.4f}"
        tangente = f"{tangente:.4f}"

    if abs(seno) < 1e-9: # Se o seno for muito próximo de zero
        cossecante = "Indefinido"
        cotangente = "Indefinido"
    else:
        cossecante = f"{1 / seno:.4f}"
        cotangente = f"{1 / tangente:.4f}"

    print(f"Tangente: {tangente}")
    print(f"Secante: {secante}")
    print(f"Co-secante: {cossecante}")
    print(f"Co-tangente: {cotangente}")
