import random

def jogar():
    print("Bem Vindo ao jogo de adivinhação")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha o nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1) :
        print("Tentativas {} de {}".format(rodada, total_tentativas))

        chute = input("Digite o seu nuúmero entre 1 a 100: ")
        numero_chutado = int(chute)

        if (numero_chutado < 1 or numero_chutado > 100):
            print("Você deve digitar um numero entre 1 e 100")
            continue

        acertou = numero_chutado == numero_secreto
        chute_maio = numero_chutado > numero_secreto
        chute_menor = numero_chutado < numero_secreto

        print("você digitou", numero_chutado)

        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(chute_maio):
                print("Você errou, o seu chute foi maior que o numero secreto")
            elif(chute_menor):
                print("Você errou, o seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - numero_chutado)
            pontos = pontos - pontos_perdidos

    print("Fim de Jogo!")

if (__name__ == "__main__"):
    jogar()