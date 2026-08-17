import random

def int_classico():
    print("Modo Clássico | Instruções: \n"
        "1. O objetivo é escolher uma célula do tabuleiro sem acertar as bombas.\n"
        "2. Se você acertar uma bomba, você perde o jogo.\n"
        "3. O jogo termina quando você acha uma bomba ou acertar as 23 casas sem bombas.\n"
        "4. O número de bombas adjacentes remete a quantidade de bombas que estão ao redor da célula escolhida.\n"
        "5. Boa sorte!")
    print()
    while True:
        escolha = int(input("Você deseja inicar o jogo[1] ou voltar ao menu[2]? "))
        if escolha == 1:
            print("Iniciando o Jogo...")
            jogar_classico()
            return
            
        elif escolha == 2:
            print("Voltando ao menu...")
            return
            
        else:
            print("Escolha invalida, Tente novamente")
            continue
    
def int_sobrevivencia():
    print("Modo Sobrevivência | Instruções: \n"
        "1. O jogo consiste em um tabuleiro 5x5 com números aleatórios de 0 a 9.\n"
        "2. O objetivo é escolher uma célula do tabuleiro sem acertar as bombas.\n"
        "3. Se você acertar uma bomba, você perde uma vida.\n"
        "4. Você começa com 3 vidas e pode ganhar vidas extras ao escolher certos números(MAX = 6).\n"
        "5. O jogo termina quando você perde todas as vidas.\n" \
        "6. Boa sorte!")
    print()
    while True:
        escolha = int(input("Você deseja inicar o jogo[1] ou voltar ao menu[2]? "))
        if escolha == 1:
            print("Iniciando o Jogo...")
            jogar_sobrevivencia()
            return
            
        elif escolha == 2:
            print("Voltando ao menu...")
            return
            
        else:
            print("Escolha invalida, Tente novamente")
            continue
    
def conta_minas_adjacentes(linha, coluna, bomba1, bomba2, tabuleiro):
    minas = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni = linha + di
            nj = coluna + dj
            if 0 <= ni < len(tabuleiro) and 0 <= nj < len(tabuleiro[0]):
                if (ni, nj) == bomba1 or (ni, nj) == bomba2:
                    minas += 1
    return minas
    
def bomba_classico():
    bomba1 = (random.randint(0, 4), random.randint(0, 4))
    bomba2 = (random.randint(0, 4), random.randint(0, 4))
    while bomba2 == bomba1:
        bomba2 = (random.randint(0, 4), random.randint(0, 4))
    return bomba1, bomba2
    
def mostrar_tabuleiro(tabuleiro):
    print("      0    1    2    3    4")

    for linha_num, linha in enumerate(tabuleiro):
        print(f"{linha_num} ", end="")

        for casa in linha:
            print(f"{casa:^5}", end="")
        print()
    
def jogar_classico():
    rodadas = 0
    tabuleiro = [
        ["*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*"]
    ]
    
    bomba1, bomba2 = bomba_classico()
    
    while rodadas < 23:
        mostrar_tabuleiro(tabuleiro)
        input_linha = input("Escolha uma linha (0-4): ")
        input_coluna = input("Escolha uma coluna (0-4): ")
        
        if not input_linha.isdigit() or not input_coluna.isdigit():
            print("Letras ou espaços vazios não são permitidos! Tente novamente.")
            continue

        linha = int(input_linha)
        coluna = int(input_coluna)
    
        if linha < 0 or linha > 4 or coluna < 0 or coluna > 4:
            print("Casa inválida ou Caractere invalido. Tente outra vez!")
            continue

        if tabuleiro[linha][coluna] != "*":
            print("Casa já aberta. Tente outra.")
            continue

        if (linha, coluna) != bomba1 and (linha, coluna) != bomba2:
            numero = (conta_minas_adjacentes(linha, coluna, bomba1, bomba2, tabuleiro))
            tabuleiro[linha][coluna] = numero
            print()
            print(f"Você escolheu a casa ({linha}, {coluna}).")
            print(f"Minas adjacentes: {numero}")
            rodadas += 1
            print("Rodadas Jogadas: ", rodadas)
            
        else:
            print("Você acertou uma bomba! Game Over.")
            break
    if rodadas == 23:
        print("Parabéns! Você venceu o jogo!")


def bomba_sobrevivencia():
    bomba3 = random.randint(0, 9)
    bomba4 = random.randint(0, 9)
    while bomba4 == bomba3:
        bomba3 = random.randint(0, 9)
        
    vidas_extras = random.randint(0, 9)
    return bomba3, bomba4, vidas_extras

def tab_sobrevivencia():
    matriz = [[random.randint(0, 9) for i in range(5)] for i in range(5)]
    return matriz

def jogar_sobrevivencia():
    vidas = 3
    vidas_max = 6
    rodadas = 0
    
    
    while True:
        matriz = tab_sobrevivencia()
        bomba3, bomba4, vidas_extras = bomba_sobrevivencia()
        print("   0  1  2  3  4")

        for linha_num, linha in enumerate(matriz):
            print(linha_num, linha)

        print()
        if vidas != 0:
            input_linha = input("Digite a linha(0-4): ")
            input_coluna = input("Digite a coluna(0-4): ")

            if not input_linha.isdigit() or not input_coluna.isdigit():
                print("Letras ou espaços vazios não são permitidos! Tente novamente.")
                continue

            linha = int(input_linha)
            coluna = int(input_coluna)

            if linha < 0 or linha > 4 or coluna < 0 or coluna > 4:
                print("Linha ou coluna inválida. Por favor, digite valores entre 0 e 4.")
                continue
            resultado = matriz[linha][coluna]
            print(f"O número que você escolheu foi: {resultado}")

            if resultado != bomba3 and resultado != bomba4 and resultado != vidas_extras:
                print("Você Sobreviveu!")
                rodadas += 1

            elif resultado == vidas_extras:
                if vidas < vidas_max:
                    vidas += 1
                    print("Você sobreviveu e ganhou uma vida extra!")
                else:
                    print("Você sobreviveu, mas já está com o número máximo de vidas!")
                rodadas += 1

            else:
                print("Você acertou uma bomba e perdeu uma vida!")
                vidas -= 1
                rodadas += 1

            print()
            print(f"O número com a primeira bomba era: {bomba3}")
            print(f"O número com a segunda bomba era: {bomba4}")
            print(f"O seu número atual de vidas é: {vidas}")
            print(f"O número com vidas extras era: {vidas_extras}")
            print()
        else:
            print()
            print("Fim de Jogo!!!")
            print(f"Você sobreviveu por {rodadas} rodadas!")
            break

def menu():
    while True:
        print(r"""  _____                                 __  __ _                 _
 / ____|                               |  \/  (_)               | |
| |     __ _ _ __ ___  _ __   ___      | \  / |_ _ __   __ _  __| | ___
| |    / _` | '_ ` _ \| '_ \ / _ \     | |\/| | | '_ \ / _` |/ _` |/ _ \
| |___| (_| | | | | | | |_) | (_) |    | |  | | | | | | (_| | (_| | (_) |
 \_____\__,_|_| |_| |_| .__/ \___/     |_|  |_|_|_| |_|\__,_|\__,_|\___/
                      | |
                      |_|                                                 """)
        escolha_do_modo = input("Escolha o modo de jogo: \n"
"(1) Clássico\n"
"(2) Sobrevivência\n"
"(3) Instruções do Modo Clássico\n"
"(4) Instruções do Modo Sobrevivência\n"
"(5) Sair\n"
"Sua escolha: \n"
"")
        if escolha_do_modo == "1":
            jogar_classico()
            
        elif escolha_do_modo == "2":
            jogar_sobrevivencia()

        elif escolha_do_modo == "3":
            int_classico()
            
        elif escolha_do_modo == "4":
            int_sobrevivencia()
            
        elif escolha_do_modo == "5":
            print("Encerrando o jogo...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    menu()
