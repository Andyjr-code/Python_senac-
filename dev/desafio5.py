import math

""" 
Cadastrar um produto e descobrir o valor total
"""  

# string [e] texto

produto = int(input("Digite o nome do produto: "))
qtde = int(input("Digite a quantidade do produto: "))
preco = float(int(input("Digite o preço do produto: ")))
total = qtde * preco
print('o valor total: ', total)
print(f'o produto {produto} tem o valor total de {total}')

# Estrutura Condicional
# Se o valor total for maior que 1000 entao de um desconto de 10
# > < == 
if total >= 1000:
    print("O valor total é maior ou igual a 1000") 

    math.pow(2,2)
    # 2 base
    # 2 expoente
    # 2²
    math.sqrt()