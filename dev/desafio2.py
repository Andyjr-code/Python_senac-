import os # importando uma biblioteca
print(""" 
╭━━━╮╱╱╱╭╮╭╮╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╭╯╰┫┃╱╱╱╱╱╱╱┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃┃
┃╰━╯┣╮╱┣╮╭┫╰━┳━━┳━╮┃╰━━┳━━┫╰━┳━━┳━━┫┃╭━━╮
┃╭━━┫┃╱┃┃┃┃╭╮┃╭╮┃╭╮╋━━╮┃╭━┫╭╮┃╭╮┃╭╮┃┃┃━━┫
┃┃╱╱┃╰━╯┃╰┫┃┃┃╰╯┃┃┃┃╰━╯┃╰━┫┃┃┃╰╯┃╰╯┃╰╋━━┃
╰╯╱╱╰━╮╭┻━┻╯╰┻━━┻╯╰┻━━━┻━━┻╯╰┻━━┻━━┻━┻━━╯
╱╱╱╱╭━╯┃
╱╱╱╱╰━━╯ """)

#variável  #input - ler do teclado string (texto)
nome_categoria = input("Digite o nome da categoria: ")
#print - mostrar na tela
print(nome_categoria)
print(type(nome_categoria)) #mostra o tipo (técnico)
os.system("pause") #pausa no sistemaa
os.system('cls') #limpamos a tela