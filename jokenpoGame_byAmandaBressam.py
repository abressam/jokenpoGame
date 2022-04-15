# Jokênpo Game - By Amanda Bressam Martins

# Importando a biblioteca random
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
    # Instruções de como jogar o modo Humano vs Humano
    print("\n\nModo de Jogo - Humano vs Humano\n")
    print("""-> Instruções

Nesse modo de jogo é necessário dois jogadores humanos
e toda vez que um jogador vencer uma partida, ele
ganha 1 ponto no placar.
    """)
    print("Digite [1] para jogar “Pedra”.\nDigite [2] para jogar “Papel”.\nDigite [3] para jogar “Tesoura”.\n")

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
            if (first_player == 1 and second_player == 3):
                print("\n O Jogador 1 jogou “Pedra” e o Jogador 2 jogou “Tesoura”")
                print("Resultado: “Pedra” derrota “Tesoura”")
            elif (first_player == 2 and second_player == 1):
                print("\n O Jogador 1 jogou “Papel” e o Jogador 2 jogou “Pedra”")
                print("Resultado: “Papel” derrota “Pedra”")
            else:
                print("\n O Jogador 1 jogou “Tesoura” e o Jogador 2 jogou “Papel”")
                print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 1 venceu a ",round,"º partida!\n")
            first_player_win += 1

            choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            while choice < 0 or choice > 1:
                print("A opção inserida não é válida! Tente novamente")
                choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # O jogador escolhe continuar jogando
            if (choice == 1):
                round += 1
                is_playing = is_playing

            # O jogador escolhe encerrar o jogo, as estatísticas são informadas e o programa encerra
            else:
                print("\nO jogo foi encerrado\n")
                print("----> Estatísticas do Jogo <----")
                print("\nPlacar final")
                print("\nJogador 1:", first_player_win, "pontos.")
                print("Jogador 2:", second_player_win, "pontos.\n")

                if (first_player_win > second_player_win):
                    print("O Jogador 1 venceu o jogo!")
                elif (second_player_win > first_player_win):
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

        # Confere se o Jogador 2 venceu
        elif (second_player == 1 and first_player == 3 or second_player == 2 and first_player == 1 or second_player == 3 and first_player == 2):
            
            if (second_player == 1 and first_player == 3): 
                print("\n O Jogador 2 jogou “Pedra” e o Jogador 1 jogou “Tesoura”")
                print("Resultado: “Pedra” derrota “Tesoura”")
            elif (second_player == 2 and first_player == 1): 
                print("\n O Jogador 2 jogou “Papel” e o Jogador 1 jogou “Pedra”")
                print("Resultado: “Papel” derrota “Pedra”")
            else: 
                print("\n O Jogador 2 jogou “Tesoura” e o Jogador 1 jogou “Papel”")
                print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 2 venceu a",round,"º partida!\n")
            second_player_win += 1

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

                if (first_player_win > second_player_win):
                    print("O Jogador 1 venceu o jogo!")
                elif (second_player_win > first_player_win):
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
        
        # Confere se houve empate
        else:
            print("\nEmpate!\n")
            tie_occurs += 1
            first_player_win = first_player_win
            second_player_win = second_player_win

            choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            while choice < 0 or choice > 1:
                print("A opção inserida não é válida! Tente novamente")
                choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            if (choice == 1):
                round += 1
                is_playing = is_playing

            else:
                print("\nO jogo foi encerrado\n")
                print("----> Estatísticas do Jogo <----")
                print("\nPlacar final")
                print("\nJogador 1:", first_player_win, "pontos.")
                print("Jogador 2:", second_player_win, "pontos.\n")

                if (first_player_win > second_player_win):
                    print("O Jogador 1 venceu o jogo!")
                elif (second_player_win > first_player_win):
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

# O usuário selecionou o segundo modo de jogo
elif (user_choice == 2):
    # Instruções de como jogar o modo Humano vs Computador
    print("\n\nModo de Jogo - Humano vs Computador\n")
    print("""-> Instruções

Nesse modo de jogo o Jogador 1 é humano e o Jogador 2 é uma inteligência artificial. 
A cada vitória obtida, o jogador receberá 1 ponto no placar.
    """)
    print("Digite [1] para jogar “Pedra”.\nDigite [2] para jogar “Papel”.\nDigite [3] para jogar “Tesoura”.\n")

    is_playing = 1
    round = 1
    tie_occurs = 0
    first_player_win = 0
    second_player_win = 0

    while is_playing == 1:

        print("\nPartida", round)
        print("-------------------------------------\n")

        # Recebe e guarda a opção de jogada inserido Jogador 1
        first_player = int(input("Jogador 1, infome sua jogada: "))

        # Confere se o valor inserido pelo Jogador 1 é valido, caso contrário joga novamente
        while first_player < 1 or first_player > 3:
            print("\nO Jogador 1 informou um número inválido. Por favor digite sua jogada novamente.")
            first_player = int(input("Jogador 1, infome sua jogada: "))

        # O Jogador 2 terá a jogada definida aleatóriamente, no intervalo de 1 a 3 
        second_player = randint(1, 3)
        print("Jogador 2 escolheu:", second_player)
        
        # Confere se o Jogador 1 venceu
        if (first_player == 1 and second_player == 3 or first_player == 2 and second_player == 1 or first_player == 3 and second_player == 2):
            
            # Imprime na tela qual a situação que levou o Jogador 1 à vitória
            if (first_player == 1 and second_player == 3):
                print("\n O Jogador 1 jogou “Pedra” e o Jogador 2 jogou “Tesoura”")
                print("Resultado: “Pedra” derrota “Tesoura”")
            elif (first_player == 2 and second_player == 1):
                print("\n O Jogador 1 jogou “Papel” e o Jogador 2 jogou “Pedra”")
                print("Resultado: “Papel” derrota “Pedra”")
            else:
                print("\n O Jogador 1 jogou “Tesoura” e o Jogador 2 jogou “Papel”")
                print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 1 venceu a ",round,"º partida!\n")
            first_player_win += 1

            choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            while choice < 0 or choice > 1:
                print("A opção inserida não é válida! Tente novamente")
                choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # O jogador escolhe continuar
            if (choice == 1):
                round += 1
                is_playing = is_playing

            # O jogador escolher encerrar o jogo, as estatísticas são informadas e o programa encerra
            else:
                print("\nO jogo foi encerrado\n")
                print("----> Estatísticas do Jogo <----")
                print("\nPlacar final")
                print("\nJogador 1:", first_player_win, "pontos.")
                print("Jogador 2:", second_player_win, "pontos.\n")

                if (first_player_win > second_player_win):
                    print("O Jogador 1 venceu o jogo!")
                elif (second_player_win > first_player_win):
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

        # Confere se o Jogador 2 venceu
        elif (second_player == 1 and first_player == 3 or second_player == 2 and first_player == 1 or second_player == 3 and first_player == 2):
            
            if (second_player == 1 and first_player == 3): 
                print("\nO Jogador 2 jogou “Pedra” e o Jogador 1 jogou “Tesoura”")
                print("Resultado: “Pedra” derrota “Tesoura”")
            elif (second_player == 2 and first_player == 1): 
                print("\nO Jogador 2 jogou “Papel” e o Jogador 1 jogou “Pedra”")
                print("Resultado: “Papel” derrota “Pedra”")
            else: 
                print("\nO Jogador 2 jogou “Tesoura” e o Jogador 1 jogou “Papel”")
                print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 2 venceu a ",round,"º partida!\n")
            second_player_win += 1

            choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            while choice < 0 or choice > 1:
                print("A opção inserida não é válida! Tente novamente")
                choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # O jogador escolhe continuar jogando
            if (choice == 1):
                round += 1
                is_playing = is_playing

            # O jogador escolhe encerrar o jogo, as estatísticas são informadas e o programa encerra
            else:
                print("\nO jogo foi encerrado\n")
                print("----> Estatísticas do Jogo <----")
                print("\nPlacar final")
                print("\nJogador 1:", first_player_win, "pontos.")
                print("Jogador 2:", second_player_win, "pontos.\n")

                if (first_player_win > second_player_win):
                    print("O Jogador 1 venceu o jogo!")
                elif (second_player_win > first_player_win):
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

        # Confere se houve empate
        else:
            print("\nEmpate!\n")
            tie_occurs += 1
            first_player_win = first_player_win
            second_player_win = second_player_win

            choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            while choice < 0 or choice > 1:
                print("A opção inserida não é válida! Tente novamente")
                choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # O jogador escolhe continuar jogando
            if (choice == 1):
                round += 1
                is_playing = is_playing

            # O jogador escolhe encerrar o jogo, as estatísticas são informadas e o programa encerra
            else:
                print("\nO jogo foi encerrado\n")
                print("----> Estatísticas do Jogo <----")
                print("\nPlacar final")
                print("\nJogador 1:", first_player_win, "pontos.")
                print("Jogador 2:", second_player_win, "pontos.\n")

                if (first_player_win > second_player_win):
                    print("O Jogador 1 venceu o jogo!")
                elif (second_player_win > first_player_win):
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

# O usuário selecionou o terceiro modo de jogo
else:
    # Instruções de como jogar o modo Humano vs Computador
    print("\n\nModo de Jogo - Computador vs Computador\n")
    print("""-> Instruções

Esse modo de jogo é uma batalha entre inteligências artificiais!
O usuário será um espectador e definirá quantas partidas ocorrerão durante o jogo.
A cada vitória obtida na partida, o jogador receberá 1 ponto no placar.
    """)
    tie_occurs = 0
    first_player_win = 0
    second_player_win = 0

    # Recebe e guarda o número de partidas informadas pelo usuário    
    number_of_rounds = int(input("Digite quantas partidas deseja presenciar: "))

    # Confere se o número inserido pelo usuário é maior que 0, caso contrário deve digitar novamente
    while number_of_rounds < 1:
        print("\nOops! Você precisa digitar um número maior do que 0. Tente novamente.")
        number_of_rounds = int(input("Digite quantas partidas deseja presenciar: "))

    # O número de partidas é dado pelo intervalo de 1 até o número digitado pelo usuário
    for count_round in range(1, number_of_rounds + 1):

        # Informa a partida atual
        print("\nPartida", count_round)
        print("-------------------------------------\n")

        # A escolha de cada jogador é obtida aleatóriamente, no intervalo de 1 a 3
        first_player = randint(1, 3)
        print("Jogador 1 escolheu:", first_player)

        second_player = randint(1, 3)
        print("Jogador 2 escolheu:", second_player)

        # Confere se o Jogador 1 venceu
        if (first_player == 1 and second_player == 3 or first_player == 2 and second_player == 1 or first_player == 3 and second_player == 2):
                
            # Imprime na tela qual a situação que levou o Jogador 1 à vitória
            if (first_player == 1 and second_player == 3):
                print("\n O Jogador 1 jogou “Pedra” e o Jogador 2 jogou “Tesoura”")
                print("Resultado: “Pedra” derrota “Tesoura”")
            elif (first_player == 2 and second_player == 1):
                print("\n O Jogador 1 jogou “Papel” e o Jogador 2 jogou “Pedra”")
                print("Resultado: “Papel” derrota “Pedra”")
            else:
                print("\n O Jogador 1 jogou “Tesoura” e o Jogador 2 jogou “Papel”")
                print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 1 venceu a ",count_round,"º partida!\n")
            first_player_win += 1
            
        # Confere se o Jogador 2 venceu
        elif (second_player == 1 and first_player == 3 or second_player == 2 and first_player == 1 or second_player == 3 and first_player == 2):
                
            if (second_player == 1 and first_player == 3): 
                print("\nO Jogador 2 jogou “Pedra” e o Jogador 1 jogou “Tesoura”")
                print("Resultado: “Pedra” derrota “Tesoura”")
            elif (second_player == 2 and first_player == 1): 
                print("\nO Jogador 2 jogou “Papel” e o Jogador 1 jogou “Pedra”")
                print("Resultado: “Papel” derrota “Pedra”")
            else: 
                print("\nO Jogador 2 jogou “Tesoura” e o Jogador 1 jogou “Papel”")
                print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 2 venceu a ",count_round,"º partida!\n")
            second_player_win += 1

        # Confere se houve empate
        else:
            print("\nEmpate!\n")
            tie_occurs += 1
            first_player_win = first_player_win
            second_player_win = second_player_win
    