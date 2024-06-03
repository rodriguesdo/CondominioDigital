import os
import random

def tela():
    os.system("cls" if os.name == "nt" else "clear")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("    ----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("    ----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + str(jogadas))

def jogador_joga():
    global jogadas
    while True:
        try:
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if velha[linha][coluna] == " ":
                velha[linha][coluna] = "X"
                jogadas += 1
                break
            else:
                print("Posição já ocupada!")
        except (IndexError, ValueError):
            print("Entrada inválida! Tente novamente.")

def cpu_joga():
    global jogadas
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if velha[linha][coluna] == " ":
            velha[linha][coluna] = "O"
            jogadas += 1
            break

def check_vit():
    # Checar linhas
    for i in range(3):
        if velha[i][0] == velha[i][1] == velha[i][2] and velha[i][0] != " ":
            return velha[i][0]
    # Checar colunas
    for i in range(3):
        if velha[0][i] == velha[1][i] == velha[2][i] and velha[0][i] != " ":
            return velha[0][i]
    # Checar diagonais
    if velha[0][0] == velha[1][1] == velha[2][2] and velha[0][0] != " ":
        return velha[0][0]
    if velha[0][2] == velha[1][1] == velha[2][0] and velha[0][2] != " ":
        return velha[0][2]
    return "n"

jogarNovamente = "s"
while jogarNovamente == "s":
    velha = [[" " for _ in range(3)] for _ in range(3)]
    jogadas = 0
    quemJoga = 2
    maxJogadas = 9
    vit = "n"

    while True:
        tela()
        if quemJoga == 2:
            jogador_joga()
            quemJoga = 1
        else:
            cpu_joga()
            quemJoga = 2

        vit = check_vit()
        if vit != "n" or jogadas >= maxJogadas:
            break

    tela()
    if vit == "n":
        print("Deu velha!")
    else:
        print(f"Vitória do {vit}!")

    jogarNovamente = input("Jogar novamente? (s/n): ").lower()
