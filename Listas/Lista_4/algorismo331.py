""" Um marciano chegou a uma floresta e se escondeu atrás de uma
das 100 árvore quando viu um caçador. O caçador só tinha cinco balas em sua
espingarda. Cada vez que ele atirava, e não acertava, é claro, o marciano dizia:
estou mais à direita ou mais à esquerda. Se o caçador não conseguir acertar o
marciano, ele será levado para Marte. Implementar este jogo para dois jogadores,
onde um escolhe a árvore em que o marciano irá se esconder, e o outro tenta
acertar."""

import random

def jogar():
    """Função principal para o jogo de adivinhação do marciano."""

    # Definindo a árvore onde o marciano vai se esconder (entre 1 e 100)
    # O primeiro jogador insere um número entre 1 e 100 para a posição do marciano
    while True:
        try:
            posicao_marciano = int(input("Jogador 1, escolha a árvore (1-100) onde o marciano vai se esconder: "))
            if 1 <= posicao_marciano <= 100:
                break
            else:   
                print("A árvore deve estar entre 1 e 100.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    balas = 5
    arvores = list(range(1, 101))

    # O segundo jogador tenta adivinhar a posição do marciano
    while balas > 0:
        print(f"\nVocê tem {balas} balas.")
        while True:
            try:
                tiro = int(input("Jogador 2, atire em qual árvore (1-100): "))
                if 1 <= tiro <= 100:
                    break
                else:
                    print("A árvore deve estar entre 1 e 100.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        balas -= 1

        if tiro == posicao_marciano:
            print(f"Parabéns! Você acertou o marciano na árvore {tiro}.")
            print("Você salvou o planeta!")
            return
        elif tiro < posicao_marciano:
            print("O marciano diz: Estou mais à direita!")
        else:
            print("O marciano diz: Estou mais à esquerda!")

    print("\nVocê falhou em todos os tiros e o marciano escapou para Marte!")

# Inicia o jogo
if __name__ == "__main__":
    jogar()
    