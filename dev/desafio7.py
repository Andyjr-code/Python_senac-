import os

print("Menu Financeiro")

print("1 - Cadastrar")
print("2 - Listar")
print("3 - Atualizar")
print("4 - Excluir")

opcao = int(input("Digite a opção: "))
if opcao == 1:
    print("Cadastrar")
elif opcao == 2:
    print("Listar")
elif opcao == 3:
    print("Atualizar")
elif opcao == 4:
    print("Excluir")
else: 
    print("Opção inválida!")

os.system("pause")
os.system('cls')

