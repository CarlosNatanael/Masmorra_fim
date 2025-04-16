import time
from combate import combate

def nivel_dois(player):
    print("Capítulo 2: O Salão dos Espelhos\n")
    time.sleep(2)
    print('"O velho Eldramar havia me alertado:"')
    print("A Masmorra do Fim não é apenas um labirinto de pedra. Ela testará sua mente, sua alma e sua coragem. Se você falhar, seu corpo se tornará mais uma sombra presa em seus corredores.\n")
    time.sleep(2)
    print("Agora, diante de mim, erguia-se uma enorme porta de ébano, cravejada de espelhos quebrados. Um frio percorreu minha espinha.")
    time.sleep(3)
    print('— "O Salão dos Espelhos," murmurei.')
    time.sleep(1)
    print("Ao entrar, o portal se fechou atrás de mim com um click sinistro. O que vi foi um corredor infinito,")
    print("onde centenas—talvez milhares—de reflexos me encaravam. Mas algo estava errado.")
    time.sleep(3)
    print("\nAlguns não eram eu.\n")
    print('Alguns sorriam quando eu não sorria. Outros me observavam com olhos vazios, como se fossem espectros à espera.')
    time.sleep(3)
    print("— Ilusão? — perguntei em voz alta.")
    time.sleep(3)
    print('"Ou será que você é a ilusão?" — uma voz sussurrou, ecoando de todos os lados.\n')
    time.sleep(3)
    print("De repente, um dos meus reflexos moveu-se sozinho. Ele ergueu a mão e tocou o vidro do outro lado.\n")
    time.sleep(3)
    print(f"Clone Corrompido de {player['nome']}: Você não deveria estar aqui") 
    time.sleep(3)
    print("Ele disse, com minha voz, mas distorcida, como se falasse através de água.")
    time.sleep(3)
    input("\nPrecione ENTER para continuar")
    print(f"\nClone Corrompido de {player['nome']}: Você acha que merece escapar? — o clone sussurrou")
    time.sleep(2)
    print(f"Clone Corrompido de {player['nome']}: Vamos brincar com a sua sorte, logo a frente no centro do salão há três espelhos.")
    print("1. 'A verdade nem sempre é vista com os olhos.'")
    print("2. 'A imagem que vês é quem você é.'")
    print("3. 'O reflexo invertido é o caminho certo.'")

    escolha = input(f"Clone Corrompido de {player['nome']}:Qual espelho você toca? (1/2/3): ").strip()
    while escolha not in ["1", "2", "3"]:
        escolha = input("Escolha inválida. Tente novamente (1/2/3): ").strip()

    if escolha == "3":
        print('\n"Você se conhece melhor do que pensa. Avance."')
        time.sleep(3)
    else:
        time.sleep(2)
        print("\nAntes que eu pudesse reagir, o espelho diante de mim se dissolveu em névoa, e ele saiu.")
        print("Era eu—mas não. Seus olhos eram negros como breu, e sua boca se torcia em um sorriso que nunca faria.")
        time.sleep(3)
        print("\nUm clone distorcido de você salta do espelho! Erguendo uma adaga que surgiu do nada.")
        time.sleep(2)
        print(f'Clone Corrompido de {player['nome']}: Você não pode me vencer, "ele riu". Eu sou você.\n')
        time.sleep(3)
        clone = {
            "nome": f"Clone Corrompido de {player['nome']}",
            "classe": player["classe"],
            "vida": player["vida"],
            "força": player["força"],
            "magia": player["magia"],
            "defesa": player["defesa"],
            "habilidade": player["habilidade"],
        }
        if not combate(player, [clone]):
            return False

    print("\nUma nova porta surgiu no final do salão. E avança para o próximo nível.")
    time.sleep(3)
    input("\nPressione ENTER para continuar\n")
    return True