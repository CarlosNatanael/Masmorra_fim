import random
import time

def habilidade_especial(player, inimigos):
    player = verificar_status_monarca(player)
    derrotados = []
    print(f"\n{player['nome']} usa {player['habilidade']}!")
    
    if player["classe"] == "Mago":
        dano = player["magia"] + random.randint(10, 20)
        for inimigo in inimigos[:]:
            inimigo["vida"] -= dano
            print(f"Você lançou uma Bola de Fogo em {inimigo['nome']} e causou {dano} de dano")
            if inimigo["vida"] <= 0:
                print(f"{inimigo['nome']} foi derrotado!")
                derrotados.append(inimigo)
                inimigos.remove(inimigo)

    elif player["classe"] == "Paladino":
        player["vida"] += 20
        print("Você usou Benção divina e recuperou 20 de vida")

    elif player["classe"] == "Arqueiro":
        dano = player["força"] + random.randint(10, 20)
        for inimigo in inimigos[:]:
            inimigo["vida"] -= dano
            print(f"Você usou Tiro Certeiro em {inimigo['nome']} e causou {dano} de dano")
            if inimigo["vida"] <= 0:
                print(f"{inimigo['nome']} foi derrotado!")
                derrotados.append(inimigo)
                inimigos.remove(inimigo)

    elif player["classe"] == "Guerreiro":
        dano = player["força"] + random.randint(10, 20)
        for inimigo in inimigos[:]:
            inimigo["vida"] -= dano
            print(f"Você usou Decapitação em {inimigo['nome']} e causou {dano} de dano")
            if inimigo["vida"] <= 0:
                print(f"{inimigo['nome']} foi derrotado!")
                derrotados.append(inimigo)
                inimigos.remove(inimigo)
                
    elif player["classe"] == "Monarca das Sombras":
        if "força_original" not in player:
            player["força_original"] = player["força"]
            player["vida_original"] = player["vida"]
        
        player["força"] += 30
        player["vida"] += 20
        print("\nVocê invocou o Domínio das Sombras!")
        print(f"| Força aumentada para {player['força']} (+30)")
        print(f"| Vida aumentada para {player['vida']} (+20)")
        print("| Todos os inimigos sofrem 10 de dano sombrio!")
        
        # Dano adicional para o Monarca
        for inimigo in inimigos[:]:
            inimigo["vida"] -= 10
            print(f"{inimigo['nome']} sofreu 10 de dano das sombras!")
            if inimigo["vida"] <= 0:
                print(f"{inimigo['nome']} foi consumido pelas sombras!")
                inimigos.remove(inimigo)
        
        return []
    
    return derrotados

def ganhar_xp(player, xp_ganho):
    if player.get("monarca_sombra", False):
        # Progressão diferente para o Monarca
        player["xp"] += xp_ganho
        print(f"\n{player['nome']} absorveu {xp_ganho} pontos de essência sombria!")
        
        while player["xp"] >= player["xp_proximo_nivel"]:
            player["xp"] -= player["xp_proximo_nivel"]
            player["nivel"] += 1
            player["xp_proximo_nivel"] = int(player["xp_proximo_nivel"] * 1.5)  # Progressão mais lenta
            
            # Melhoria de atributos do Monarca
            player["vida"] += 10
            player["força"] += 5
            player["magia"] += 4
            player["defesa"] += 6
            
            print(f"\n🌑 {player['nome']} ascendeu para o nível {player['nivel']}!")
            print("As sombras lhe concederam:")
            print(f"Vida: {player['vida']} (+10)")
            print(f"Força: {player['força']} (+5)")
            print(f"Magia: {player['magia']} (+4)")
            print(f"Defesa: {player['defesa']} (+6)\n")
    else:
        
        player["xp"] += xp_ganho
        print(f"\n{player['nome']} ganhou {xp_ganho} de experiência!")

        while player["xp"] >= player["xp_proximo_nivel"]:
            player["xp"] -= player["xp_proximo_nivel"]
            player["nivel"] += 1
            player["xp_proximo_nivel"] = int(player["xp_proximo_nivel"] * 1.5)

            player["vida"] += 10
            player["força"] += 4
            player["defesa"] += 3
            if player["classe"] == "Mago":
                player["magia"] += 4
            elif player["classe"] == "Paladino":
                player["vida"] += 4
            elif player["classe"] == "Arqueiro":
                player["força"] += 4
            elif player["classe"] == "Guerreiro":
                player["força"] += 4

            print(f"\n {player['nome']} subiu para o nível {player['nivel']}!")
            print("Seus atributos aumentaram:")
            print(f"Vida: {player['vida']}, Força: {player['força']}, Magia: {player['magia']}, Defesa: {player['defesa']}\n")

def verificar_status_monarca(player):
    if player.get("monarca_sombra", False) and player["classe"] != "Monarca das Sombras":
        player["classe"] = "Monarca das Sombras"
        if player["habilidade"] != "Domínio das Sombras":
            player["habilidade"] = "Domínio das Sombras"
            print("\nAs sombras corrigiram seu status...")
            print("| » Habilidade atualizada para: Domínio das Sombras")
    return player

def combate(player, inimigos):
    player["habilidade_usada"] = False

    print("Você está em combate com os inimigos!")
    time.sleep(2)

    derrotados = []
    turno_perdido = False

    # Inicialização do Monarca das Sombras
    if player["classe"] == "Monarca das Sombras" and "força_original" not in player:
        player["força_original"] = player["força"]
        player["vida_original"] = player["vida"]

    while inimigos and player["vida"] > 0:
        # Se o jogador perdeu o turno anterior
        if turno_perdido:
            turno_perdido = False
            monstro = random.choice(inimigos)
            dano_monstro = max(1, monstro["força"] - (player["defesa"] // 2))  # Garante pelo menos 1 de dano
            player["vida"] -= dano_monstro
            print(f"\n{monstro['nome']} aproveitou sua hesitação e atacou causando {dano_monstro} de dano!")
            if player["vida"] <= 0:
                print("\n💀Você foi derrotado! Game over!💀")
                input("\nPressione ENTER para continuar\n")
                return False
            continue

        # Exibe status
        print(f"\n{player['nome']} (Nível: {player['nivel']}, Classe: {player['classe']}): Vida = {player['vida']} | XP = {player['xp']}/{player['xp_proximo_nivel']}")
        for i, inimigo in enumerate(inimigos):
            print(f"{i + 1}. {inimigo['nome']} (Nível: {inimigo['nivel']}, Classe: {inimigo['classe']}): Vida = {inimigo['vida']}")

        # Menu de ações
        print("\nEscolha sua ação:")
        print("1. Atacar")
        print("2. Usar item")
        print("3. Usar habilidade especial")

        acao = input("Digite o número da ação escolhida: ")

        # Processa ação
        if acao == "1":
            if not inimigos:
                print("Não há inimigos para atacar.")
                turno_perdido = True
                continue
            
            try:
                escolha = int(input("Escolha o inimigo para atacar (número): ").strip()) - 1
                if escolha < 0 or escolha >= len(inimigos):
                    print("Escolha inválida. Tente novamente.")
                    turno_perdido = True
                    continue
            except ValueError:
                print("Entrada inválida. Digite um número.")
                turno_perdido = True
                continue

            # Ataque válido
            inimigo = inimigos[escolha]
            dano = max(1, player["força"] - random.randint(0, 3))  # Garante pelo menos 1 de dano
            inimigo["vida"] -= dano
            print(f"\nVocê atacou {inimigo['nome']} e causou {dano} de dano")
            if inimigo["vida"] <= 0:
                print(f"{inimigo['nome']} foi derrotado!")
                derrotados.append(inimigo)
                inimigos.remove(inimigo)

        elif acao == "2":
            # Lógica de itens
            print("Seus itens:")
            for nome_item, qtd in player["itens"].items():
                print(f"- {nome_item} (x{qtd})")
            
            item_input = input("Escolha o item para usar: ").strip().casefold()

            item_encontrado = None
            for nome_item in player["itens"]:
                if item_input == nome_item.casefold():
                    item_encontrado = nome_item
                    break
            
            if item_encontrado and player["itens"][item_encontrado] > 0:
                if item_encontrado == "poção de cura":
                    player["vida"] += 20
                    player["itens"][item_encontrado] -= 1
                    print("Você usou a poção de cura e recuperou 20 de vida\n")
                elif item_encontrado == "poção de força":
                    player["força"] += 10
                    player["itens"][item_encontrado] -= 1
                    print("Você usou a poção de força e aumentou 10 de força\n")
                elif item_encontrado == "poção de defesa":
                    player["defesa"] += 20
                    player["itens"][item_encontrado] -= 1
                    print("Você usou a poção de defesa e aumentou 20 de defesa\n")
            else:
                print("Você não possui item ou digitou algo incorretamente\n")
                turno_perdido = True
                continue

        elif acao == "3":
            if player.get("habilidade_usada", False):
                print("\nVocê já usou sua habilidade especial nesta batalha!")
                turno_perdido = True
                continue
            
            derrotados_habilidade = habilidade_especial(player, inimigos)
            derrotados.extend(derrotados_habilidade)
            player["habilidade_usada"] = True

        else:
            print("\nAção inválida. Tente novamente.")
            turno_perdido = True
            continue

        # Ataque do inimigo após ação válida do jogador
        if not turno_perdido and inimigos:
            monstro = random.choice(inimigos)
            dano_monstro = max(1, monstro["força"] - (player["defesa"] // 2))  # Garante pelo menos 1 de dano
            player["vida"] -= dano_monstro
            print(f"\n{monstro['nome']} atacou você causando {dano_monstro} de dano!")

        # Verificação de derrota
        if player["vida"] <= 0:
            print("\n💀 Você foi derrotado! Game over! 💀\n")
            input("Pressione ENTER para continuar\n")
            return False

    # Vitória
    print("\nVocê derrotou todos os inimigos!")
    xp_total = sum([inimigo.get("nivel", 1) * 30 for inimigo in derrotados])
    ganhar_xp(player, xp_total)

    # Restauração dos atributos do Monarca
    if player["classe"] == "Monarca das Sombras" and "força_original" in player:
        if player.get("bonus_monarca", False):
            player["força"] = player["força_original"]
            player["vida"] = player["vida_original"]
            print("\nO poder das sombras se dissipa...")
            print(f"| Força voltou para {player['força']}")
            print(f"| Vida voltou para {player['vida']}\n")
            del player["bonus_monarca"]

        if not player.get("bonus_monarca", False):
            del player["força_original"]
            del player["vida_original"]

    return True