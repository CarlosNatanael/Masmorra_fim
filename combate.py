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
        print("Você usou Benção divina e recuperou 30 de vida")

    elif player["classe"] == "Arqueiro":
        dano = player["força"] + random.randint(5, 10)
        for inimigo in inimigos[:]:
            inimigo["vida"] -= dano
            print(f"Você usou Tiro Certeiro em {inimigo['nome']} e causou {dano} de dano")
            if inimigo["vida"] <= 0:
                print(f"{inimigo['nome']} foi derrotado!")
                inimigos.remove(inimigo)

    elif player["classe"] == "Guerreiro":
        dano = player["força"] + random.randint(10, 15)
        for inimigo in inimigos[:]:
            inimigo["vida"] -= dano
            print(f"Você usou Decapitação em {inimigo['nome']} e causou {dano} de dano")
            if inimigo["vida"] <= 0:
                print(f"{inimigo['nome']} foi derrotado!")
                inimigos.remove(inimigo)

def ganhar_xp(player, xp_ganho):
    player["xp"] += xp_ganho
    print(f"\n{player['nome']} ganhou {xp_ganho} de experiência!")

    while player["xp"] >= player["xp_proximo_nivel"]:
        player["xp"] -= player["xp_proximo_nivel"]
        player["nivel"] += 1
        player["xp_proximo_nivel"] = int(player["xp_proximo_nivel"] * 1.5)

        player["vida"] += 10
        player["força"] += 2
        player["defesa"] += 1
        if player["classe"] == "Mago":
            player["magia"] += 3
        elif player["classe"] == "Paladino":
            player["força"] += 3
        elif player["classe"] == "Arqueiro":
            player["força"] += 3
        elif player["classe"] == "Guerreiro":
            player["força"] += 3

        print(f"\n🎉 {player['nome']} subiu para o nível {player['nivel']}!")
        print("Seus atributos aumentaram:")
        print(f"Vida: {player['vida']}, Força: {player['força']}, Defesa: {player['defesa']}")


def combate(player, inimigos):
    print("Você está em combate com os inimigos!")
    time.sleep(2)

    derrotados = []

    while inimigos and player["vida"] > 0:
        print(f"\n{player['nome']} (Nível: {player['nivel']}, Classe: {player['classe']}): Vida = {player['vida']} | XP = {player['xp']}/{player['xp_proximo_nivel']}")
        for i, inimigo in enumerate(inimigos):
            print(f"{i + 1}. {inimigo['nome']} - Vida = {inimigo['vida']}")

        print("\nEscolha sua ação:")
        print("1. Atacar")
        print("2. Usar item")
        print("3. Usar habilidade especial")

        acao = input("Digite o número da ação escolhida: ")

        if acao == "1":
            escolha = int(input("Escolha o inimigo para atacar (número): ")) - 1
            if 0 <= escolha < len(inimigos):
                inimigo = inimigos[escolha]
                dano = max(0, player["força"] - random.randint(0, 3))
                inimigo["vida"] -= dano
                print(f"\nVocê atacou {inimigo['nome']} e causou {dano} de dano")
                if inimigo["vida"] <= 0:
                    print(f"{inimigo['nome']} foi derrotado!")
                    derrotados.append(inimigo)
                    inimigos.remove(inimigo)
            else:
                print("Inimigo inválido. Tente novamente.")

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

        if inimigos:
            goblin = random.choice(inimigos)
            dano_goblin = max(0, goblin["força"] - player["defesa"])
            player["vida"] -= dano_goblin
            print(f"{goblin['nome']} atacou você causando {dano_goblin} de dano!")

        if player["vida"] <= 0:
            print("\nVocê foi derrotado! Game over!")
            return False

    print("\nVocê derrotou todos os inimigos!")

    # Ganho de XP
    xp_total = sum([inimigo.get("nivel", 1) * 20 for inimigo in derrotados])
    ganhar_xp(player, xp_total)

    return True