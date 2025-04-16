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
            if not inimigos:
                print("Não há inimigos para atacar.")
                continue
            try:
                escolha = int(input("Escolha o inimigo para atacar (número): ").strip()) - 1
                if escolha < 0 or escolha >= len(inimigos):
                    print("Escolha inválida. Tente novamente.")
                    continue
            except ValueError:
                print("Entrada inválida. Digite um número.")
                continue

            inimigo = inimigos[escolha]
            dano = max(0, player["força"] - random.randint(0, 3))
            inimigo["vida"] -= dano
            print(f"\nVocê atacou {inimigo['nome']} e causou {dano} de dano")
            if inimigo["vida"] <= 0:
                print(f"{inimigo['nome']} foi derrotado!")
                derrotados.append(inimigo)
                inimigos.remove(inimigo)

        elif acao == "2":
            print("Seus itens:")
            for nome_item, qtd in player["itens"].items():
                print(f"- {nome_item} (x{qtd})")
            
            item_input = input("Escolha o item para usar: ").strip().casefold()

            item_encontrado = None
            for nome_item in player["itens"]:
                if item_input == nome_item.casefold():
                    item_encontrado = nome_item
                    break
            if item_encontrado and player["itens"] [item_encontrado] > 0:
                if item_encontrado == "poção de cura":
                    player["vida"] +=20
                    player["itens"] [item_encontrado] -= 1
                    print("Você usou a poção de cura e recuperou 20 de vida\n")
            else:
                print("Você não possui item ou digitou algo incorretamente\n")

        elif acao == "3":
            habilidade_especial(player, inimigos)

        else:
            print("Ação inválida. Tente novamente.")
            continue

        if inimigos:
            monstro = random.choice(inimigos)
            dano_monstro = max(0, monstro["força"] - player["defesa"])
            player["vida"] -= dano_monstro
            print(f"{monstro['nome']} atacou você causando {dano_monstro} de dano!")

        if player["vida"] <= 0:
            print("\nVocê foi derrotado! Game over!")
            return False

    print("\nVocê derrotou todos os inimigos!")

    xp_total = sum([inimigo.get("nivel", 1) * 20 for inimigo in derrotados])
    ganhar_xp(player, xp_total)

    return True