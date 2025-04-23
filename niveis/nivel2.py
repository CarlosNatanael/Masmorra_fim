from utils.combate import combate
import time
import random


desafios_clone = [
    {
        "opcoes": [
            "'A verdade nem sempre é vista com os olhos.'",
            "'A imagem que vês é quem você é.'",
            "'O reflexo invertido é o caminho certo.'"
        ],
        "correta": random.choice([0, 1, 2])
    },
    {
        "opcoes": [
            "'O caminho da esquerda traz poder.'",
            "'O caminho do centro traz sabedoria.'",
            "'O caminho da direita traz a vitória.'"
        ],
        "correta": random.choice([0, 1, 2])
    },
    {
        "opcoes": [
            "'Aquilo que teme é o que te molda.'",
            "'A força está em negar sua essência.'",
            "'O silêncio vence qualquer guerra.'"
        ],
        "correta": random.choice([0, 1, 2])
    },
    {
        "opcoes": [
            "'A sombra é apenas a luz adormecida.'",
            "'Tudo que brilha é falso.'",
            "'A duplicata carrega o fardo da perfeição.'"
        ],
        "correta": random.choice([0, 1, 2])
    },
    {
        "opcoes": [
            "'Negar a dor é negar a si mesmo.'",
            "'A vitória vem de evitar o conflito.'",
            "'Só os tolos enfrentam seus iguais.'"
        ],
        "correta": random.choice([0, 1, 2])
    },
    {
        "opcoes": [
            "'Se tudo é espelho, onde está o real?'",
            "'A cópia supera o original com tempo.'",
            "'Quem enfrenta o reflexo perde o eu.'"
        ],
        "correta": random.choice([0, 1, 2])
    }
]

def nivel_dois(player):
    print("Capítulo 2: O Salão dos Espelhos\n")
    time.sleep(5)
    print('"O velho Velthurion havia me alertado:"')
    print("A Masmorra do Fim não é apenas um labirinto de pedra. Ela testará sua mente, sua alma e sua coragem. Se você falhar, seu corpo se tornará mais uma sombra presa em seus corredores.\n")
    time.sleep(5)
    print("Agora, diante de mim, erguia-se uma enorme porta de ébano, cravejada de espelhos quebrados. Um frio percorreu minha espinha.")
    time.sleep(5)
    print('— "O Salão dos Espelhos," murmurei.')
    time.sleep(5)
    print("Ao entrar, o portal se fechou atrás de mim com um click sinistro. O que vi foi um corredor infinito,")
    print("onde centenas—talvez milhares—de reflexos me encaravam. Mas algo estava errado.")
    time.sleep(5)
    print("\nAlguns não eram eu.\n")
    print('Alguns sorriam quando eu não sorria. Outros me observavam com olhos vazios, como se fossem espectros à espera.')
    time.sleep(5)
    print("— Ilusão? — perguntei em voz alta.")
    time.sleep(5)
    print('"Ou será que você é a ilusão?" — uma voz sussurrou, ecoando de todos os lados.\n')
    time.sleep(5)
    print("De repente, um dos meus reflexos moveu-se sozinho. Ele ergueu a mão e tocou o vidro do outro lado.\n")
    time.sleep(5)
    print(f"Clone Corrompido de {player['nome']}: Você não deveria estar aqui") 
    time.sleep(5)
    print("Ele disse, com minha voz, mas distorcida, como se falasse através de água.")
    time.sleep(5)
    input("\nPressione ENTER para continuar")
    print(f"\nClone Corrompido de {player['nome']}: Você acha que merece escapar? — o clone sussurrou")
    time.sleep(5)
    desafio = random.choice(desafios_clone)
    print(f"\nClone Corrompido de {player['nome']}: Vamos brincar com a sua sorte, logo à frente no centro do salão há três espelhos.")
    for i, opcao in enumerate(desafio["opcoes"], 1):
        print(f"{i}. {opcao}")
    
    escolha = input("\nQual espelho você toca? (1/2/3): ").strip()
    
    if escolha == str(desafio["correta"] + 1):  # +1 porque o usuário vê 1-based
        print('\n"Você se conhece melhor do que pensa. Avance."')
    else:
        print("\nO clone salta do espelho para enfrentar você!")
        time.sleep(5)
        print("\nAntes que eu pudesse reagir, o espelho diante de mim se dissolveu em névoa, e ele saiu.")
        print("Era eu—mas não. Seus olhos eram negros como breu, e sua boca se torcia em um sorriso que nunca faria.")
        time.sleep(5)
        print(f"\nUm clone distorcido de você salta do espelho! Erguendo um {player["arma"]} que surgiu do nada.")
        time.sleep(5)
        print(f'Clone Corrompido de {player["nome"]}: Você não pode me vencer, "ele riu". Eu sou você.\n')
        time.sleep(5)
        clone = {
            "nome": f"Clone Corrompido de {player['nome']}",
            "classe": player["classe"],
            "vida": player["vida"],
            "força": player["força"] * 1,
            "magia": player["magia"] * 1 if player["classe"] == "Mago" else 0,
            "defesa": player["defesa"] * 1,
            "habilidade": player["habilidade"],
            "nivel": player["nivel"],
            "xp": 50
        }
        clone["força"] = max(5, clone["força"])
        input("Prepare-se para o combate! Pressione ENTER...\n")
        if not combate(player, [clone]):
            return False

    print("\nUma nova porta surgiu no final do salão. Você avança para o próximo nível.")
    time.sleep(5)
    input("\nPressione ENTER para continuar\n")
    return True