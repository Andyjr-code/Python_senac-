""" Construir um algoritmo que leia dois valores numéricos inteiros e
efetue a adição; caso o resultado seja maior que 10, apresentá-lo. """

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
soma = num1 + num2

if soma > 10:
    print("A soma é: ", soma)
else:
    print("A soma é menor ou igual a 10")