""" Entrar com 10 números e imprimir o quadrado de cada número """

numeros = []

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

for numero in numeros:
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é {quadrado}")