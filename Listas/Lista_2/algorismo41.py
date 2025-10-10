""" Entrar com quatro números e imprimir a média ponderada ,
sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4. """

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))  
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

peso1 = 1
peso2 = 2
peso3 = 3           
peso4 = 4

soma_ponderada = (num1 * peso1) + (num2 * peso2) + (num3 * peso3) + (num4 * peso4)
soma_pesos = peso1 + peso2 + peso3 + peso4  
media_ponderada = soma_ponderada / soma_pesos
print("A média ponderada é: ", media_ponderada)