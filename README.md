Exercício de Programação – Jogo de Caça ao
Tesouro
Objetivo
Desenvolver um programa em Python que simule um jogo de caça ao tesouro utilizando matrizes
(listas bidimensionais). O objetivo é praticar conceitos de listas, loops, entrada de dados e
condicionais, implementando um jogo funcional que interaja com o usuário pelo terminal.
Descrição do Problema

Você deverá criar um programa que:
1. Crie um tabuleiro representado por uma matriz 5x5.
2. Posicione um tesouro em uma posição aleatória do tabuleiro.
3. Permita que o jogador faça 7 tentativas para encontrar o tesouro.
4. Para cada tentativa, o jogador deve informar:
o Linha (0 a 4)
o Coluna (0 a 4)
5. Caso o jogador acerte a posição do tesouro:
o Marque a posição no tabuleiro com "T".
o Exiba uma mensagem de vitória e finalize o jogo.
6. Caso o jogador erre:
o Marque a posição escolhida com "X".
o Informe uma dica indicando se o tesouro está mais para cima, baixo, esquerda ou
direita.
7. Ao final das tentativas, caso o tesouro não seja encontrado, exiba a posição correta.
8. Exiba o tabuleiro atualizado após cada tentativa.


Regras e Restrições
• Use listas bidimensionais para representar o tabuleiro.
• O programa deve rodar no terminal; não utilize bibliotecas gráficas.
• As posições do tabuleiro são numeradas de 0 a 4 para linhas e colunas.
• Não permita que o jogador insira valores fora do tabuleiro.
• Evite qualquer comportamento que quebre a execução do programa (como entradas
inválidas)
