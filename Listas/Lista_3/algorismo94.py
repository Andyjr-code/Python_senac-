""" Entrar com um número e imprimir uma das mensagens: é múltiplo
de 3 ou não é múltiplo de 3. """

num = int(input("Digite um número inteiro: "))

if num % 3 == 0:
  print("É múltiplo de 3.")
else:
  print("Não é múltiplo de 3.")