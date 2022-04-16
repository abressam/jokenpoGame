# Jokênpo Game - By Amanda Bressam Martins

# Importando a biblioteca random
from random import randint

# Informações iniciais do menu
print("Escolha o modo de jogo\nDigite o número correspondente ao modo\n")
print("Humano vs Humano [1]\n")
print("Humano vs Computador [2]\n")
print("Computador vs Computador [3]\n")

# Recebe e guarda a escolha do modo de jogo digitada pelo usuário
game_mode = int(input("Digite o modo de jogo desejado: "))

# Confere se o valor inserido pelo usuário é válido (1, 2 ou 3), caso contrário ele deve digitar novamente
while game_mode < 1 or game_mode > 3:
    print("\nOops! Esse valor não é válido, tente novamente.")
    game_mode = int(input("Digite o modo de jogo desejado: "))

# O usuário selecionou o primeiro modo de jogo
if game_mode == 1:
    # Instruções de como jogar o modo Humano vs Humano
    print("\n\nModo de Jogo - Humano vs Humano\n")
    print("""-> Instruções

    Nesse modo de jogo é necessário dois jogadores humanos
    e toda vez que um jogador vencer uma partida, ele
    ganha 1 ponto no placar.
    """)
    print("Digite [1] para jogar “Pedra”.\nDigite [2] para jogar “Papel”.\nDigite [3] para jogar “Tesoura”.\n")

    is_playing = 1

    round = 1 # partidas
    tie_occurs = 0 # empates

    first_player_win = 0 # vitórias do Jogador 1
    second_player_win = 0 # vitórias do Jogador 2

    while is_playing == 1: # Inicia a partida

        # Imprime na tela a rodada atual
        print("\nPartida", round)
        print("-------------------------------------\n")

        # Recebe e guarda a opção de jogada inserido Jogador 1
        first_player = int(input("Jogador 1, infome sua jogada: "))

        # Confere se o valor inserido pelo Jogador 1 é valido (1, 2 ou 3), caso contrário joga novamente
        while first_player < 1 or first_player > 3:
            print("\nO Jogador 1 informou um número inválido. Por favor digite sua jogada novamente.")
            first_player = int(input("Jogador 1, infome sua jogada: "))

        # Recebe e guarda a opção de jogada inserido Jogador 2
        second_player = int(input("Jogador 2, informe sua jogada: "))
            
        # Confere se o valor inserido pelo Jogador 2 é valido (1, 2 ou 3), caso contrário joga novamente
        while second_player < 1 or second_player > 3:
            print("\nO Jogador 2 informou um número inválido. Por favor digite sua jogada novamente.")
            second_player = int(input("Jogador 2, informe sua jogada: "))

        # Confere se o Jogador 1 venceu
        if first_player == 1 and second_player == 3 or first_player == 2 and second_player == 1 or first_player == 3 and second_player == 2:
            
            # Imprime na tela qual a situação que levou o Jogador 1 à vitória
            if first_player == 1 and second_player == 3:
                print("\nO Jogador 1 jogou “Pedra” e o Jogador 2 jogou “Tesoura”")
                print("Resultado: “Pedra” derrota “Tesoura”")
            elif first_player == 2 and second_player == 1:
                print("\nO Jogador 1 jogou “Papel” e o Jogador 2 jogou “Pedra”")
                print("Resultado: “Papel” derrota “Pedra”")
            else:
                print("\nO Jogador 1 jogou “Tesoura” e o Jogador 2 jogou “Papel”")
                print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 1 venceu a ",round,"º partida!\n")
            first_player_win += 1 # soma +1 às vitórias do Jogador 1 

            # Recebe e guarda a opção do usuário sobre continuar ou não o jogo
            continue_playing = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # Confere se o valor inserido pelo usuário é válido (0 ou 1), caso contrário ele deve digitar novamente
            while continue_playing < 0 or continue_playing > 1:
                print("A opção inserida não é válida! Tente novamente")
                choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # O jogador escolhe continuar jogando
            if continue_playing == 1:
                round += 1
                continue

            # O jogador escolhe encerrar o jogo, as estatísticas são informadas e o programa encerra
            else:
                print("\nO jogo foi encerrado\n")
                print("----> Estatísticas do Jogo <----")
                print("\nPlacar final")
                print("\nJogador 1:", first_player_win, "pontos.")
                print("Jogador 2:", second_player_win, "pontos.\n")

                # Confere e informa qual jogador venceu o jogo ou se houve empate
                if first_player_win > second_player_win:
                    print("O Jogador 1 venceu o jogo!")
                elif second_player_win > first_player_win:
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
        elif second_player == 1 and first_player == 3 or second_player == 2 and first_player == 1 or second_player == 3 and first_player == 2:
            
            # Imprime na tela qual a situação que levou o Jogador 2 à vitória
            if second_player == 1 and first_player == 3: 
                print("\nO Jogador 2 jogou “Pedra” e o Jogador 1 jogou “Tesoura”")
                print("Resultado: “Pedra” derrota “Tesoura”")
            elif second_player == 2 and first_player == 1: 
                print("\nO Jogador 2 jogou “Papel” e o Jogador 1 jogou “Pedra”")
                print("Resultado: “Papel” derrota “Pedra”")
            else: 
                print("\nO Jogador 2 jogou “Tesoura” e o Jogador 1 jogou “Papel”")
                print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 2 venceu a",round,"º partida!\n")
            second_player_win += 1 # soma +1 às vitórias do Jogador 2

            # Recebe e guarda a opção do usuário sobre continuar ou não o jogo
            continue_playing = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # Confere se o valor inserido pelo usuário é válido (0 ou 1), caso contrário ele deve digitar novamente
            while continue_playing < 0 or continue_playing > 1:
                print("A opção inserida não é válida! Tente novamente")
                choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # O jogador escolhe continuar jogando
            if continue_playing == 1:
                round += 1
                continue

            # O jogador escolhe encerrar o jogo, as estatísticas são informadas e o programa encerra
            else:
                print("\nO jogo foi encerrado\n")
                print("----> Estatísticas do Jogo <----")
                print("\nPlacar final")
                print("\nJogador 1:", first_player_win, "pontos.")
                print("Jogador 2:", second_player_win, "pontos.\n")

                # Confere e informa qual jogador venceu o jogo ou se houve empate
                if first_player_win > second_player_win:
                    print("O Jogador 1 venceu o jogo!")
                elif second_player_win > first_player_win:
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
            tie_occurs += 1 # soma +1 aos empates

            # Mantêm os valores correspondentes às vitórias de cada jogador
            first_player_win = first_player_win
            second_player_win = second_player_win

            # Recebe e guarda a opção do usuário sobre continuar ou não o jogo
            continue_playing = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # Confere se o valor inserido pelo usuário é válido (0 ou 1), caso contrário ele deve digitar novamente
            while continue_playing < 0 or continue_playing > 1:
                print("A opção inserida não é válida! Tente novamente")
                choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # O jogador escolhe continuar jogando
            if continue_playing == 1:
                round += 1
                continue

            # O jogador escolhe encerrar o jogo, as estatísticas são informadas e o programa encerra
            else:
                print("\nO jogo foi encerrado\n")
                print("----> Estatísticas do Jogo <----")
                print("\nPlacar final")
                print("\nJogador 1:", first_player_win, "pontos.")
                print("Jogador 2:", second_player_win, "pontos.\n")

                # Confere e informa qual jogador venceu o jogo ou se houve empate
                if first_player_win > second_player_win:
                    print("O Jogador 1 venceu o jogo!")
                elif second_player_win > first_player_win:
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
elif game_mode == 2:
    # Instruções de como jogar o modo Humano vs Computador
    print("\n\nModo de Jogo - Humano vs Computador\n")
    print("""-> Instruções

    Nesse modo de jogo o Jogador 1 é humano e o Jogador 2 é uma inteligência artificial. 
    A cada vitória obtida, o jogador receberá 1 ponto no placar.
    """)
    print("Digite [1] para jogar “Pedra”.\nDigite [2] para jogar “Papel”.\nDigite [3] para jogar “Tesoura”.\n")

    is_playing = 1
    round = 1 # partidas
    tie_occurs = 0 # empates
    first_player_win = 0 # vitórias do Jogador 1
    second_player_win = 0 # vitórias do Jogador 2

    while is_playing == 1: # Inicia a partida

        # Imprime na tela a rodada atual
        print("\nPartida", round)
        print("-------------------------------------\n")

        # Recebe e guarda a opção de jogada inserido Jogador 1
        first_player = int(input("Jogador 1, infome sua jogada: "))

        # Confere se o valor inserido pelo Jogador 1 é valido (1, 2 ou 3), caso contrário joga novamente
        while first_player < 1 or first_player > 3:
            print("\nO Jogador 1 informou um número inválido. Por favor digite sua jogada novamente.")
            first_player = int(input("Jogador 1, infome sua jogada: "))

        # O Jogador 2 terá a jogada definida aleatóriamente, no intervalo de 1 a 3 
        second_player = randint(1, 3)
        print("Jogador 2 escolheu:", second_player)
        
        # Confere se o Jogador 1 venceu
        if first_player == 1 and second_player == 3 or first_player == 2 and second_player == 1 or first_player == 3 and second_player == 2:
            
            # Imprime na tela qual a situação que levou o Jogador 1 à vitória
            if first_player == 1 and second_player == 3:
                print("\nO Jogador 1 jogou “Pedra” e o Jogador 2 jogou “Tesoura”")
                print("Resultado: “Pedra” derrota “Tesoura”")
            elif first_player == 2 and second_player == 1:
                print("\nO Jogador 1 jogou “Papel” e o Jogador 2 jogou “Pedra”")
                print("Resultado: “Papel” derrota “Pedra”")
            else:
                print("\nO Jogador 1 jogou “Tesoura” e o Jogador 2 jogou “Papel”")
                print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 1 venceu a ",round,"º partida!\n")
            first_player_win += 1 # soma +1 às vitórias do Jogador 1

            # Recebe e guarda a opção do usuário sobre continuar ou não o jogo
            continue_playing = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # Confere se o valor inserido pelo usuário é válido (0 ou 1), caso contrário ele deve digitar novamente
            while continue_playing < 0 or continue_playing > 1:
                print("A opção inserida não é válida! Tente novamente")
                choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # O jogador escolhe continuar jogando
            if continue_playing == 1:
                round += 1
                continue

            # O jogador escolhe encerrar o jogo, as estatísticas são informadas e o programa encerra
            else:
                print("\nO jogo foi encerrado\n")
                print("----> Estatísticas do Jogo <----")
                print("\nPlacar final")
                print("\nJogador 1:", first_player_win, "pontos.")
                print("Jogador 2:", second_player_win, "pontos.\n")

                # Confere e informa qual jogador venceu o jogo ou se houve empate
                if first_player_win > second_player_win:
                    print("O Jogador 1 venceu o jogo!")
                elif second_player_win > first_player_win:
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
        elif second_player == 1 and first_player == 3 or second_player == 2 and first_player == 1 or second_player == 3 and first_player == 2:

            # Imprime na tela qual a situação que levou o Jogador 2 à vitória
            if second_player == 1 and first_player == 3: 
                print("\nO Jogador 2 jogou “Pedra” e o Jogador 1 jogou “Tesoura”")
                print("Resultado: “Pedra” derrota “Tesoura”")
            elif second_player == 2 and first_player == 1: 
                print("\nO Jogador 2 jogou “Papel” e o Jogador 1 jogou “Pedra”")
                print("Resultado: “Papel” derrota “Pedra”")
            else: 
                print("\nO Jogador 2 jogou “Tesoura” e o Jogador 1 jogou “Papel”")
                print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 2 venceu a ",round,"º partida!\n")
            second_player_win += 1 # soma +1 às vitórias do Jogador 2

            # Recebe e guarda a opção do usuário sobre continuar ou não o jogo
            continue_playing = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # Confere se o valor inserido pelo usuário é válido (0 ou 1), caso contrário ele deve digitar novamente
            while continue_playing < 0 or continue_playing > 1:
                print("A opção inserida não é válida! Tente novamente")
                choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # O jogador escolhe continuar jogando
            if continue_playing == 1:
                round += 1
                continue

            # O jogador escolhe encerrar o jogo, as estatísticas são informadas e o programa encerra
            else:
                print("\nO jogo foi encerrado\n")
                print("----> Estatísticas do Jogo <----")
                print("\nPlacar final")
                print("\nJogador 1:", first_player_win, "pontos.")
                print("Jogador 2:", second_player_win, "pontos.\n")

                # Confere e informa qual jogador venceu o jogo ou se houve empate
                if first_player_win > second_player_win:
                    print("O Jogador 1 venceu o jogo!")
                elif second_player_win > first_player_win:
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
            tie_occurs += 1 # soma +1 aos empates

            # Mantêm os valores correspondentes às vitórias de cada jogador
            first_player_win = first_player_win
            second_player_win = second_player_win

            # Recebe e guarda a opção do usuário sobre continuar ou não o jogo
            continue_playing = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # Confere se o valor inserido pelo usuário é válido (0 ou 1), caso contrário ele deve digitar novamente
            while continue_playing < 0 or continue_playing > 1:
                print("A opção inserida não é válida! Tente novamente")
                choice = int(input("Deseja jogar novamente?\nDigite [0] para encerrar o jogo ou digite [1] para continuar jogando: "))

            # O jogador escolhe continuar jogando
            if continue_playing == 1:
                round += 1
                continue

            # O jogador escolhe encerrar o jogo, as estatísticas são informadas e o programa encerra
            else:
                print("\nO jogo foi encerrado\n")
                print("----> Estatísticas do Jogo <----")
                print("\nPlacar final")
                print("\nJogador 1:", first_player_win, "pontos.")
                print("Jogador 2:", second_player_win, "pontos.\n")

                # Confere e informa qual jogador venceu o jogo ou se houve empate
                if first_player_win > second_player_win:
                    print("O Jogador 1 venceu o jogo!")
                elif second_player_win > first_player_win:
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
    tie_occurs = 0 # empates
    first_player_win = 0 # vitórias do Jogador 1
    second_player_win = 0 # vitórias do Jogador 2

    # Recebe e guarda o número de partidas informadas pelo usuário    
    number_of_rounds = int(input("Digite quantas partidas deseja presenciar: "))

    # Confere se o número inserido pelo usuário é maior que 0, caso contrário ele deve digitar novamente
    while number_of_rounds < 1:
        print("\nOops! Você precisa digitar um número maior do que 0 para iniciar o jogo. Tente novamente.")
        number_of_rounds = int(input("Digite quantas partidas deseja presenciar: "))

    # As partidas iniciam a partir do número 1 e terminam no valor informado pelo usuário
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
        if first_player == 1 and second_player == 3 or first_player == 2 and second_player == 1 or first_player == 3 and second_player == 2:
                
            # Imprime na tela qual a situação que levou o Jogador 1 à vitória
            if first_player == 1 and second_player == 3:
                print("\n O Jogador 1 jogou “Pedra” e o Jogador 2 jogou “Tesoura”")
                print("Resultado: “Pedra” derrota “Tesoura”")
            elif first_player == 2 and second_player == 1:
                print("\n O Jogador 1 jogou “Papel” e o Jogador 2 jogou “Pedra”")
                print("Resultado: “Papel” derrota “Pedra”")
            else:
                print("\n O Jogador 1 jogou “Tesoura” e o Jogador 2 jogou “Papel”")
                print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 1 venceu a ",count_round,"º partida!\n")
            first_player_win += 1 # soma +1 às vitórias do Jogador 1
            
        # Confere se o Jogador 2 venceu
        elif second_player == 1 and first_player == 3 or second_player == 2 and first_player == 1 or second_player == 3 and first_player == 2:

            # Imprime na tela qual a situação que levou o Jogador 2 à vitória
            if second_player == 1 and first_player == 3: 
                print("\nO Jogador 2 jogou “Pedra” e o Jogador 1 jogou “Tesoura”")
                print("Resultado: “Pedra” derrota “Tesoura”")
            elif second_player == 2 and first_player == 1: 
                print("\nO Jogador 2 jogou “Papel” e o Jogador 1 jogou “Pedra”")
                print("Resultado: “Papel” derrota “Pedra”")
            else: 
                print("\nO Jogador 2 jogou “Tesoura” e o Jogador 1 jogou “Papel”")
                print("\nResultado: “Tesoura” derrota “Papel”")

            print("\n-> O Jogador 2 venceu a ",count_round,"º partida!\n")
            second_player_win += 1 # soma +1 às vitórias do Jogador 2

        # Confere se houve empate
        else:
            print("\nEmpate!\n")
            tie_occurs += 1 # soma +1 aos empates

            # Mantêm os valores correspondentes às vitórias de cada jogador
            first_player_win = first_player_win
            second_player_win = second_player_win
    