import random
import time

def habilidade_especial(player, inimigos):
    print(f"\n{player['nome']} usa {player['habilidade']}!")

    if player["classe"] == "Mago":
        dano = player["magia"] + random.randint(10, 20)
        for inimigo in inimigos[:]:
            inimigo["vida"] -= dano
            print(f"Você lançou uma Bola de Fogo em {inimigo['nome']} e causou {dano} de dano")
            if inimigo["vida"] <= 0:
                print(f"{inimigo['nome']} foi derrotado!")
                inimigos.remove(inimigo)

    elif player["classe"] == "Paladino":
        player["vida"] += 30
        print("Você usou Benção Divina e recuperou 30 de vida")

    elif player["classe"] == "Arqueiro":
        dano = player["força"] + random.randint(5, 10)
        inimigo = random.choice(inimigos)
        inimigo["vida"] -= dano
        print(f"Você usou Tiro Certeiro em {inimigo['nome']} e causou {dano} de dano")
        if inimigo["vida"] <= 0:
            print(f"{inimigo['nome']} foi derrotado!")
            inimigos.remove(inimigo)

    elif player["classe"] == "Guerreiro":
        dano = player["força"] + random.randint(10, 15)
        inimigo = random.choice(inimigos)
        inimigo["vida"] -= dano
        print(f"Você usou Decapitação em {inimigo['nome']} e causou {dano} de dano")
        if inimigo["vida"] <= 0:
            print(f"{inimigo['nome']} foi derrotado!")
            inimigos.remove(inimigo)

def combate(player, inimigos):
    print("Você está em combate com os inimigos!")
    time.sleep(1)

    while inimigos and player["vida"] > 0:
        print(f"\n{player['nome']} (Classe: {player['classe']}): Vida = {player['vida']}")
        for i, inimigo in enumerate(inimigos):
            print(f"{i + 1}. {inimigo['nome']} - Vida = {inimigo['vida']}")

        print("\nEscolha sua ação:")
        print("1. Atacar")
        print("2. Usar item")
        print("3. Usar habilidade especial")
        acao = input("Digite o número da ação escolhida: ")

        if acao == "1":
            try:
                escolha = int(input("Escolha o inimigo para atacar (número): ")) - 1
                inimigo = inimigos[escolha]
                dano = max(0, player["força"] - random.randint(0, 3))
                inimigo["vida"] -= dano
                print(f"\nVocê atacou {inimigo['nome']} e causou {dano} de dano")
                if inimigo["vida"] <= 0:
                    print(f"{inimigo['nome']} foi derrotado!")
                    inimigos.pop(escolha)
            except (ValueError, IndexError):
                print("Escolha inválida. Tente novamente.")
                continue

        elif acao == "2":
            item = input("Escolha o item para usar: poção de cura\n").strip().lower()
            if item == "poção de cura" and player["itens"].get("poção de cura", 0) > 0:
                player["vida"] += 20
                player["itens"]["poção de cura"] -= 1
                print("Você usou a poção de cura e recuperou 20 de vida.")
            else:
                print("Você não possui esse item ou está sem itens.")

        elif acao == "3":
            habilidade_especial(player, inimigos)

        else:
            print("Ação inválida. Tente novamente.")
            continue

        # Ação dos inimigos (se ainda vivos)
        if inimigos:
            monstro = random.choice(inimigos)
            dano_monstro = max(0, monstro["força"] - player["defesa"])
            player["vida"] -= dano_monstro
            print(f"{monstro['nome']} atacou você causando {dano_monstro} de dano!")

        if player["vida"] <= 0:
            print("\nVocê foi derrotado! Game over!")
            return False

    print("\nVocê derrotou todos os inimigos!")
    return True