""" Entrar com um número e informar se ele é divisível por 3 e por 7 """
num = float(input("Digite um número: "))

if num % 3 == 0 and num % 7 == 0:
    print(f"{num} é divisível por 3 e por 7.")
else:
    print(f"{num} não é divisível por 3 e por 7.")