import random

tabuleiro = [["-" for _ in range(5)] for _ in range(5)]

linha_tesouro = random.randint(0, 4)
coluna_tesouro = random.randint(0, 4)

tentativas = 7

print("JOGO DE CAÇA AO TESOURO")
print("O tabuleiro tem 5 linhas e 5 colunas (0 a 4).")
print("Você tem 7 tentativas para encontrar o tesouro!\n")

def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

for i in range(tentativas):
    print(f"Tentativa {i + 1} de {tentativas}")

    while True:
        try:
            linha = int(input("Informe a linha (0 a 4): "))
            coluna = int(input("Informe a coluna (0 a 4): "))
            if 0 <= linha <= 4 and 0 <= coluna <= 4:
                break
            else:
                print("Valores devem estar entre 0 e 4. Tente novamente.")
        except ValueError:
            print("Digite apenas números inteiros!")

    if linha == linha_tesouro and coluna == coluna_tesouro:
        tabuleiro[linha][coluna] = "T"
        mostrar_tabuleiro()
        print("Parabéns! Você encontrou o tesouro!")
        break
    else:
        tabuleiro[linha][coluna] = "X"

        if linha < linha_tesouro:
            print("Dica: O tesouro está mais para BAIXO.")
        elif linha > linha_tesouro:
            print("Dica: O tesouro está mais para CIMA.")
        if coluna < coluna_tesouro:
            print("Dica: O tesouro está mais para a DIREITA.")
        elif coluna > coluna_tesouro:
            print("Dica: O tesouro está mais para a ESQUERDA.")

        mostrar_tabuleiro()

else:
    print("Suas tentativas acabaram!")
    print(f"O tesouro estava na posição ({linha_tesouro}, {coluna_tesouro}).")
    tabuleiro[linha_tesouro][coluna_tesouro] = "T"
    mostrar_tabuleiro()
