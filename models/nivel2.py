from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound_py.sound2 import tocar_musica
from game_sound_py.sound2 import parar_musica
from utils.combate import combate
from utils.utils import encontrar_bau
from rich import print
from rich import print as rprint
from rich.panel import Panel
import time
import random
import pygame

pygame.init()
pygame.mixer.init()


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
    tocar_musica()
    rprint(Panel.fit("[bold yellow]Capítulo 2: O Salão dos Espelhos[/]", style="blue"))
    time.sleep(5)
    print('"O velho Eldramar havia me alertado:"')
    print("A Masmorra do Fim não é apenas um labirinto de pedra. Ela testará sua mente, sua alma e sua coragem. Se você falhar, seu corpo se tornará mais uma sombra presa em seus corredores.\n")
    time.sleep(5)
    print("Agora, diante de mim, erguia-se uma enorme porta de ébano, cravejada de espelhos quebrados. Um frio percorreu minha espinha.")
    time.sleep(5)
    print('— "O Salão dos Espelhos," murmurei.')
    # Chance de encontrar baús antes da batalha final
    if random.random() < 0.5:  # 50% de chance de encontrar 1-3 baús
        num_baus = random.randint(1, 3)
        print(f"\nEnquanto avança, você encontra {num_baus} baús suspeitos...")
        
        for _ in range(num_baus):
            if not encontrar_bau(player):
                return False  # Se o jogador morrer para um mímico
    time.sleep(5)
    print("\nAo entrar, o portal se fechou atrás de mim com um click sinistro. O que vi foi um corredor infinito,")
    print("onde centenas—talvez milhares—de reflexos me encaravam. Mas algo estava errado.")
    time.sleep(5)
    print("\nAlguns não eram eu.\n")
    print('"Alguns sorriam quando eu não sorria. Outros me observavam com olhos vazios, como se fossem espectros à espera."')
    time.sleep(5)
    print("'— Ilusão? — perguntei em voz alta.'")
    time.sleep(5)
    print('"Ou será que você é a ilusão?" — uma voz sussurrou, ecoando de todos os lados.\n')
    time.sleep(5)
    print("De repente, um dos meus reflexos moveu-se sozinho. Ele ergueu a mão e tocou o vidro do outro lado.\n")
    time.sleep(5)
    print(f"[bold black]Clone Corrompido de {player['nome']}[/bold black]: Você não deveria estar aqui") 
    time.sleep(5)
    print("Ele disse, com minha voz, mas distorcida, como se falasse através de água.")
    time.sleep(5)
    input("\nPressione ENTER para continuar")
    print(f"\n[bold black]Clone Corrompido de {player['nome']}[/bold black]: Você acha que merece escapar? — o clone sussurrou")
    time.sleep(5)
    desafio = random.choice(desafios_clone)
    print(f"\n[bold black]Clone Corrompido de {player['nome']}[/bold black]: Vamos brincar com a sua sorte, logo à frente no centro do salão há três espelhos.")
    for i, opcao in enumerate(desafio["opcoes"], 1):
        print(f"{i}. {opcao}")
    
    escolha = input("\nQual espelho você toca? (1/2/3): ").strip()
    
    if escolha == str(desafio["correta"] + 1):  # +1 porque o usuário vê 1-based
        rprint(Panel.fit("[green]✓ Resposta Correta![/]", style="green"))
        time.sleep(3)
        print('\n"Você se conhece melhor do que pensa. Avance."')
        mostrar_conquista("sombra_sorte_2")
    else:
        rprint(Panel.fit("[red]✗ Resposta Incorreta![/]", style="red"))
        time.sleep(3)
        print("\nO clone salta do espelho para enfrentar você!")
        time.sleep(5)
        print("\nAntes que eu pudesse reagir, o espelho diante de mim se dissolveu em névoa, e ele saiu.")
        print("Era eu—mas não. Seus olhos eram negros como breu, e sua boca se torcia em um sorriso que nunca faria.")
        time.sleep(5)
        print(f"\nUm clone distorcido de você salta do espelho! Erguendo um {player["arma"]} que surgiu do nada.")
        time.sleep(5)
        print(f'[bold black]Clone Corrompido de {player['nome']}[/bold black]: Você não pode me vencer, "ele riu". Eu sou você.\n')
        time.sleep(5)
        clone = {
            "nome": f"Clone Corrompido de {player['nome']}",
            "classe": player["classe"],
            "vida": player["vida"],
            "força": player["força"] + 5,
            "magia": player["magia"] + 5 if player["classe"] == "Mago" else 0,
            "defesa": player["defesa"] + 2,
            "habilidade": player["habilidade"],
            "nivel": player["nivel"] + 1,
            "xp": 100
        }
        clone["força"] = max(5, clone["força"])
        input("Prepare-se para o combate! Pressione ENTER...\n")
        if combate(player, [clone]):
            mostrar_conquista("encontro_eu")
        else:
            return False

    print("\nUma nova porta surgiu no final do salão. Você avança para o próximo nível.")
    time.sleep(5)
    input("\nPressione ENTER para continuar\n")
    parar_musica()
    return True