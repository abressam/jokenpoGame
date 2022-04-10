# Jokênpo Game

import os

# Informações iniciais do menu
print("Escolha o modo de jogo\nDigite o número correspondente ao modo\n")
print("Humano vs Humano [1]\n")
print("Humano vs Computador [2]\n")
print("Computador vs Computador [3]\n")

# Recebe a escolha do modo de jogo do usuário
user_choice = int(input("Digite o modo de jogo desejado: "))

# Se o dado fornecido pelo usuário não satisfaz a condição, ele deve digitar novamente
while user_choice < 1 or user_choice > 3:
    print("\nOops! Esse valor não é válido, tente novamente.")
    user_choice = int(input("Digite o modo de jogo desejado: "))

# O usuário selecionou o primeiro modo de jogo
if (user_choice == 1):
    os.system('cls')

    # Instruções de como jogar o modo Humano vs Humano
    print("Modo de Jogo - Humano vs Humano\n")
    print("""-> Instruções

Nesse modo de jogo é necessário dois jogadores humanos
e as partidas serão com base na regra “melhor de 3”, 
ou seja, o jogador que obtiver duas vitórias primeiro 
receberá 1 ponto no placar.
    """)
    print("Digite [1] para apostar “Tesoura”.\nDigite [2] para apostar “Papel”.\nDigite [3] para apostar “Pedra”.\n")
    print("Digite [0] para encerrar a partida.\n")

    is_playing = True

    round = 1
    max_round = round
    tie_occurs = 0

    first_player_win = 0
    second_player_win = 0

    max_first_win = first_player_win
    max_second_win = second_player_win

    first_player_points = 0
    second_player_points = 0

    while is_playing:

        # Imprime na tela a rodada atual
        print("Partida", round)
        print("-------------------------------------\n")

        # Recebe e guarda a opção de jogada inserido Jogador 1
        first_player = int(input("Jogador 1, infome sua jogada: "))

        # Confere se o valor inserido pelo Jogador 1 é valido, caso contrário joga novamente
        while first_player < 0 or first_player > 3:
            print("\nO Jogador 1 informou um número inválido. Por favor digite sua jogada novamente.")
            first_player = int(input("Jogador 1, infome sua jogada: "))

        # Recebe e guarda a opção de jogada inserido Jogador 2
        second_player = int(input("Jogador 2, informe sua jogada: "))
            
        # Confere se o valor inserido pelo Jogador 2 é valido, caso contrário joga novamente
        while second_player < 0 or second_player > 3:
            print("\nO Jogador 2 informou um número inválido. Por favor digite sua jogada novamente.")
            second_player = int(input("Jogador 2, informe sua jogada: "))

        # Confere se o Jogador 1 venceu
        if (first_player == 1 and second_player == 2 or first_player == 2 and second_player == 3 or first_player == 3 and second_player == 1):
            
            # Imprime na tela qual a situação que levou o Jogador 1 à vitória
            if (first_player == 1 and second_player == 2): print("\nResultado: “Tesoura” derrota “Papel”")
            elif (first_player == 2 and second_player == 3): print("\nResultado: “Papel” derrota “Pedra”")
            else: print("\nResultado: “Pedra” derrota “Tesoura”")

            print("\n-> O Jogador 1 venceu a " + str(round) + "º partida!\n")
            round += 1
            max_round = round
            first_player_win += 1

            max_first_win = first_player_win

            if (first_player_win == 2):
                first_player_points += 1
                round = 1
                print("Placar atual:\n")
                print("Jogador 1:", first_player_points, "pontos.")
                print("Jogador 2:", second_player_points, "pontos.\n")

        elif (second_player == 1 and first_player == 2 or second_player == 2 and first_player == 3 or second_player == 3 and first_player == 1):
            if (second_player == 1 and first_player == 2): print("\nResultado: “Tesoura” derrota “Papel”")
            elif (second_player == 2 and first_player == 3): print("\nResultado: “Papel” derrota “Pedra”")
            else: print("\nResultado: “Pedra” derrota “Tesoura”")

            print("\n-> O Jogador 2 venceu a " + str(round) + "º partida!\n")
            round += 1
            max_round = round
            second_player_win += 1

            max_second_win = second_player_win

            if (second_player_win == 2):
                second_player_points += 1
                round = 1
                first_player_win = 0
                second_player_win = 0
                print("Placar atual:\n")
                print("Jogador 1:", first_player_points, "pontos.")
                print("Jogador 2:", second_player_points, "pontos.\n")

        elif (first_player == 0 or second_player == 0):
            is_playing = False

            first_player_victory = ((max_first_win / (max_round)) * 100) if max_round != 0 else 0
            second_player_victory = ((max_second_win / (max_round)) * 100) if max_round != 0 else 0

            print("\nUm dos jogadores encerrou o jogo.\n ")

            print("----> Estatísticas do Jogo <----")
            print("\nPlacar final")
            print("\nJogador 1:", first_player_points, "pontos.")
            print("Jogador 2:", second_player_points, "pontos.\n")

            if (first_player_points > second_player_points): print("O Jogador 1 venceu o jogo!")
            elif (second_player_points > first_player_points): print("O Jogador 2 venceu o jogo!")
            else: print("O jogo terminou em empate")

            print("\nTotal de partidas realizadas: ", (max_round))
            print("Número de empates: ", tie_occurs)

            print("\nPorcentagem de vitória em relação as partidas")
            print("\nJogador 1: " + str(first_player_victory) + "% de vitória.")
            print("Jogador 2: " + str(second_player_victory) + "% de vitória.")

        else: # Em caso de empate
            print("\nEmpate! Joguem novamente.\n")
            round += 1
            max_round = round
            tie_occurs += 1
            first_player_win = first_player_win
            second_player_win = second_player_win

# O usuário selecionou o segundo modo de jogo
elif (user_choice == 2):
    os.system('cls')

    # Instruções de como jogar o modo Humano vs Computador
    print("Modo de Jogo - Humano vs Computador\n")
    print("""-> Instruções

Nesse modo de jogo o Jogador 1 é humano e o Jogador 2 é a inteligência artificial. 
As rodadas serão com base na regra “melhor de 3”, ou seja, o jogador que obtiver 
duas vitórias primeiro receberá 1 ponto no placar.
    """)
    print("Digite [1] para apostar “Tesoura”.\nDigite [2] para apostar “Papel”.\nDigite [3] para apostar “Pedra”.\n")
    print("Digite [0] para encerrar a partida.\n")




# O usuário selecionou o terceiro modo de jogo
elif (user_choice == 3):
    os.system('cls')
    print("Modo de Jogo - Computador vs Computador")
