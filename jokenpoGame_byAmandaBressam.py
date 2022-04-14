# Jokênpo Game

import os
from random import randint

# Informações iniciais do menu
print("Escolha o modo de jogo\nDigite o número correspondente ao modo\n")
print("Humano vs Humano [1]\n")
print("Humano vs Computador [2]\n")
print("Computador vs Computador [3]\n")

# Recebe a escolha do modo de jogo pelo usuário
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
    print("Digite [1] para apostar “Pedra”.\nDigite [2] para apostar “Papel”.\nDigite [3] para apostar “Tesoura”.\n")

    is_playing = 1

    round = 1
    tie_occurs = 0

    first_player_win = 0
    second_player_win = 0

    while is_playing == 1:

        # Imprime na tela a rodada atual
        print("\nPartida", round)
        print("-------------------------------------\n")

        # Recebe e guarda a opção de jogada inserido Jogador 1
        first_player = int(input("Jogador 1, infome sua jogada: "))

        # Confere se o valor inserido pelo Jogador 1 é valido, caso contrário joga novamente
        while first_player < 1 or first_player > 3:
            print("\nO Jogador 1 informou um número inválido. Por favor digite sua jogada novamente.")
            first_player = int(input("Jogador 1, infome sua jogada: "))

        # Recebe e guarda a opção de jogada inserido Jogador 2
        second_player = int(input("Jogador 2, informe sua jogada: "))
            
        # Confere se o valor inserido pelo Jogador 2 é valido, caso contrário joga novamente
        while second_player < 1 or second_player > 3:
            print("\nO Jogador 2 informou um número inválido. Por favor digite sua jogada novamente.")
            second_player = int(input("Jogador 2, informe sua jogada: "))

        # Confere se o Jogador 1 venceu
        if (first_player == 1 and second_player == 3 or first_player == 2 and second_player == 1 or first_player == 3 and second_player == 2):
            
            # Imprime na tela qual a situação que levou o Jogador 1 à vitória
            if (first_player == 1 and second_player == 3): print("\nResultado: “Pedra” derrota “Tesoura”")
            elif (first_player == 2 and second_player == 1): print("\nResultado: “Papel” derrota “Pedra”")
            else: print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 1 venceu a ",round,"º partida!\n")
            first_player_win += 1

            choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            while choice < 0 or choice > 1:
                print("A opção inserida não é válida! Tente novamente")
                choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # O jogador escolhe continuar jogando e o loop não é interrompido
            if (choice == 1):
                round += 1
                is_playing = is_playing

            # O jogador não que continuar jogando então o loop é interrompido, as estatísticas do jogo são informadas e o programa encerra
            else:
                print("\nO jogo foi encerrado\n")
                print("----> Estatísticas do Jogo <----")
                print("\nPlacar final")
                print("\nJogador 1:", first_player_win, "pontos.")
                print("Jogador 2:", second_player_win, "pontos.\n")

                if (first_player > second_player):
                    print("O Jogador 1 venceu o jogo!")
                elif (second_player > first_player):
                    print("O Jogador 2 venceu o jogo!")
                else:
                    print("O jogo terminou em empate")

                print("\nTotal de partidas realizadas: ", round)
                print("Número de empates: ", tie_occurs)

                first_player_victory_percent = (first_player_win / round) * 100
                second_player_victory_percent = (second_player_win / round) * 100

                print("\nPorcentagem de vitória em relação as partidas")
                print("\nJogador 1:",first_player_victory_percent,"% de vitória.")
                print("Jogador 2:",second_player_victory_percent,"% de vitória.")

                break


        elif (second_player == 1 and first_player == 3 or second_player == 2 and first_player == 1 or second_player == 3 and first_player == 2):
            
            if (second_player == 1 and first_player == 3): print("\nResultado: “Pedra” derrota “Tesoura”")
            elif (second_player == 2 and first_player == 1): print("\nResultado: “Papel” derrota “Pedra”")
            else: print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 2 venceu a " + str(round) + "º partida!\n")
            round += 1
            second_player_win += 1



            """first_player_victory = ((max_first_win / (max_round)) * 100) if max_round != 0 else 0 # verificação para evitar divisão por 0
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
            print("Jogador 2: " + str(second_player_victory) + "% de vitória.")"""

        else: # Em caso de empate
            print("\nEmpate! Joguem novamente.\n")
            round += 1
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
A cada vitória obtida, o jogador receberá 1 ponto no placar.
    """)
    print("Digite [1] para apostar “Pedra”.\nDigite [2] para apostar “Papel”.\nDigite [3] para apostar “Tesoura”.\n")
    print("Digite [0] para encerrar a partida.\n")

    is_playing = True
    round = 1
    tie_occurs = 0
    first_player_points = 0
    second_player_points = 0

    while is_playing:

        print("Partida", round)
        print("-------------------------------------\n")

        # Recebe e guarda a opção de jogada inserido Jogador 1
        first_player = int(input("Jogador 1, infome sua jogada: "))

        # Confere se o valor inserido pelo Jogador 1 é valido, caso contrário joga novamente
        while first_player < 0 or first_player > 3:
            print("\nO Jogador 1 informou um número inválido. Por favor digite sua jogada novamente.")
            first_player = int(input("Jogador 1, infome sua jogada: "))
            
        second_player = randint(1, 3)
        print("Jogador 2 escolheu:", second_player)
        
         # Confere se o Jogador 1 venceu
        if (first_player == 1 and second_player == 3 or first_player == 2 and second_player == 1 or first_player == 3 and second_player == 2):
            
            # Imprime na tela qual a situação que levou o Jogador 1 à vitória
            if (first_player == 1 and second_player == 3): print("\nResultado: “Pedra” derrota “Tesoura”")
            elif (first_player == 2 and second_player == 1): print("\nResultado: “Papel” derrota “Pedra”")
            else: print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 1 venceu a " + str(round) + "º partida!\n")
            round += 1
            first_player_points += 1

        elif (second_player == 1 and first_player == 3 or second_player == 2 and first_player == 1 or second_player == 3 and first_player == 2):
            
            if (second_player == 1 and first_player == 3): print("\nResultado: “Pedra” derrota “Tesoura”")
            elif (second_player == 2 and first_player == 1): print("\nResultado: “Papel” derrota “Pedra”")
            else: print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 2 venceu a " + str(round) + "º partida!\n")
            round += 1
            second_player_points += 1
        
        elif (first_player == 0):
            is_playing = False

            first_player_victory = ((first_player_points / (round)) * 100) if round != 0 else 0
            second_player_victory = ((second_player_points / (round)) * 100) if round != 0 else 0

            print("\nO Jogador 1 encerrou o jogo.\n ")

            print("----> Estatísticas do Jogo <----")
            print("\nPlacar final")
            print("\nJogador 1:", first_player_points, "pontos.")
            print("Jogador 2:", second_player_points, "pontos.\n")

            if (first_player_points > second_player_points): print("O Jogador 1 venceu o jogo!")
            elif (second_player_points > first_player_points): print("O Jogador 2 venceu o jogo!")
            else: print("O jogo terminou em empate")

            if(round == 1): round = 0
            else: round -= 1

            print("\nTotal de partidas realizadas: ", (round))
            print("Número de empates: ", tie_occurs)

            print("\nPorcentagem de vitória em relação as partidas")
            print("\nJogador 1: " + str(format(first_player_victory, ".2f")) + "% de vitória.")
            print("Jogador 2: " + str(format(second_player_victory, ".2f")) + "% de vitória.")

        else: # Em caso de empate
            print("\nEmpate! Joguem novamente.\n")
            round += 1
            tie_occurs += 1
            first_player_points = first_player_points
            second_player_points = second_player_points

# O usuário selecionou o terceiro modo de jogo
elif (user_choice == 3):
    os.system('cls')
    # Instruções de como jogar o modo Humano vs Computador
    print("Modo de Jogo - Computador vs Computador\n")
    print("""-> Instruções

Esse modo de jogo é uma batalha entre inteligências artificiais!
O usuário será um espectador e definirá quantas partidas ocorreram durante o jogo.
A cada vitória obtida na partida, o jogador receberá 1 ponto no placar.
    """)
    tie_occurs = 0
    first_player_points = 0
    second_player_points = 0
    
    number_of_rounds = int(input("Digite quantas partidas deseja presenciar: "))

    while number_of_rounds < 1:
        print("\nOops! Você precisa digitar um número maior do que 0. Tente novamente.")
        number_of_rounds = int(input("Digite quantas partidas deseja presenciar: "))

    for count_round in range(1, number_of_rounds + 1):

        print("\nPartida", count_round)
        print("-------------------------------------\n")

        first_player = randint(1, 3)
        print("Jogador 1 escolheu:", first_player)
        second_player = randint(1, 3)
        print("Jogador 2 escolheu:", second_player)

        if (first_player == 1 and second_player == 3 or first_player == 2 and second_player == 1 or first_player == 3 and second_player == 2):
            
            # Imprime na tela qual a situação que levou o Jogador 1 à vitória
            if (first_player == 1 and second_player == 3): print("\nResultado: “Pedra” derrota “Tesoura”")
            elif (first_player == 2 and second_player == 1): print("\nResultado: “Papel” derrota “Pedra”")
            else: print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 1 venceu a " + str(count_round) + "º partida!\n")
            first_player_points += 1

        elif (second_player == 1 and first_player == 3 or second_player == 2 and first_player == 1 or second_player == 3 and first_player == 2):
            
            if (second_player == 1 and first_player == 3): print("\nResultado: “Pedra” derrota “Tesoura”")
            elif (second_player == 2 and first_player == 1): print("\nResultado: “Papel” derrota “Pedra”")
            else: print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 2 venceu a " + str(count_round) + "º partida!\n")
            second_player_points += 1

        else: # Em caso de empate
            print("\nEmpate! Joguem novamente.\n")
            tie_occurs += 1
            first_player_points = first_player_points
            second_player_points = second_player_points
    
        if (count_round == number_of_rounds):
            first_player_victory = ((first_player_points / (number_of_rounds)) * 100) if number_of_rounds != 0 else 0
            second_player_victory = ((second_player_points / (number_of_rounds)) * 100) if number_of_rounds != 0 else 0

            print("\n----> Estatísticas do Jogo <----")
            print("\nPlacar final")
            print("\nJogador 1:", first_player_points, "pontos.")
            print("Jogador 2:", second_player_points, "pontos.\n")

            if (first_player_points > second_player_points): print("O Jogador 1 venceu o jogo!")
            elif (second_player_points > first_player_points): print("O Jogador 2 venceu o jogo!")
            else: print("O jogo terminou em empate")

            print("\nTotal de partidas realizadas: ", (number_of_rounds))
            print("Número de empates: ", tie_occurs)

            print("\nPorcentagem de vitória em relação as partidas")
            print("\nJogador 1: " + str(first_player_victory) + "% de vitória.")
            print("Jogador 2: " + str(second_player_victory) + "% de vitória.")
    