def partida():
    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    vez_computador = True
   
    if n % (m + 1) == 0:
        print("\nVoce começa!")
        vez_computador = False
    if n % (m + 1) != 0:
        print("\nComputador começa!\n")
        vez_computador = True

    while n > 0:
        if (vez_computador == True):
            jogada = computador_escolhe_jogada(n, m)
            vez_computador = False
            if jogada == 1:
                print("\nO computador tirou uma peça")
            if jogada > 1:
                print("\nO computador tirou", jogada, "peças")          
        else:
            jogada = usuario_escolhe_jogada(n, m)
            vez_computador = True
            if jogada == 1:
                print("\nVocê tirou uma peça")
            if jogada > 1:
                print("\nVocê tirou", jogada, "peças")

        n = n - jogada

        if n > 1:
            print("Agora restam", n, "peças no tabuleiro.\n")
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")

    if (vez_computador == True):
        print("Fim de jogo! Você ganhou!")
        return 1
    else:
        print("Fim de jogo! O computador ganhou!")
        return 0

def usuario_escolhe_jogada(n, m):
    jogada = 0

    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar? "))

        if (jogada == 0) or (jogada > m) or (jogada > n) or (jogada < 1):
            print ("\nOops! Jogada inválida! Tente de novo.\n")
            jogada = 0
             
    return jogada
    
 
def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        peças = n % (m + 1)
        if peças > 0:
            return peças

        return m


def campeonato():
    r = 1
    usuario = 0
    computador = 0

    for _ in range(3):
        print("\n**** Rodada", r, "****\n")
        vencedor = partida()

        if vencedor == 1:
            usuario += 1
        else:
            computador += 1
        r = r + 1
        
    print("Placar final: Você", usuario, "X", computador, "Computador")

jogo = 0
while jogo == 0:
    p = int(input("Bem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

    if p == 1:
        print("\nVoce escolheu uma partida isolada!\n")
        partida()

    if p == 2:
        print("\nVoce escolheu um campeonato!\n")
        campeonato()

    if (p != 1) and (p != 2):
        print("\nOpção inválida!\n")
        jogo = 0
