""" Entrar com 10 números e imprimir a metade de cada número """

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    metade = numero / 2
    print(f"A metade de {numero} é {metade}")