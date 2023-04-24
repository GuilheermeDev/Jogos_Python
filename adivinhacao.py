# MESMO JOGO MAS COM WHILE

import random 

def jogar():
    
    print("************************")
    print("Jogo de adivinhação")
    print("************************")

    numero_sec = random.randint(1, 100)
    print("Número secreto:", numero_sec)  # Adicionado para depuração
    total_tentativas = 0
    rodada = 0
    chute = 0
    pontos = 1000
    print(numero_sec)
    print("""Qual o nível de dificuldade você quer? 
    (1) Fácil (2) Médio (3) Difícil""")
    nivel = int(input("Digite o número da dificuldade que você quer! "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print(f"Você está na rodada {rodada} de {total_tentativas}")
        chute = int(input("Digite um número entre 1 e 100: "))

        if chute < 1 or chute > 100:
            print("Número inválido, digite um número entre 1 e 100 ")
            continue

        if chute == numero_sec:
            print("Você acertou, parabéns! e a sua pontuação foi", pontos)
            break
        if chute > numero_sec:
            print("O número que você digitou é maior, tente novamente")
        else:
            print("O número que você digitou é menor, tente novamente")
        pontos_perdidos = abs(numero_sec - chute)
        pontos = pontos - pontos_perdidos

    print(f"O número era {numero_sec} e você fez um total de {pontos} ")
    
if (__name__=="__main__"):
    jogar()