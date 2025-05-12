from game_sound_py.game_over import tocar_game
from game_sound_py.game_over import parar_game
from rich import print
from rich import print as rprint
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.text import Text
from rich import box
import random
import time

console = Console()

def habilidade_especial(player, inimigos):
    player = verificar_status_monarca(player)
    derrotados = []
    rprint(f"\n[bold]{player['nome']}[/] usa [yellow]{player['habilidade']}[/]!")
    
    if player["classe"] == "Mago":
        dano = player["magia"] + random.randint(10, 20)
        for inimigo in inimigos[:]:
            inimigo["vida"] -= dano
            print(f"Você lançou uma [bold yellow]Bola de Fogo[/bold yellow] em {inimigo['nome']} e causou [bold red]{dano}[/bold red] de dano")
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
            print(f"Você usou [bold yellow]Tiro Certeiro[/bold yellow] em {inimigo['nome']} e causou [bold red]{dano}[/bold red] de dano")
            if inimigo["vida"] <= 0:
                print(f"{inimigo['nome']} foi derrotado!")
                derrotados.append(inimigo)
                inimigos.remove(inimigo)

    elif player["classe"] == "Guerreiro":
        dano = player["força"] + random.randint(10, 20)
        for inimigo in inimigos[:]:
            inimigo["vida"] -= dano
            print(f"Você usou [bold yellow]Decapitação[/bold yellow] em {inimigo['nome']} e causou [bold red]{dano}[/bold red] de dano")
            if inimigo["vida"] <= 0:
                print(f"{inimigo['nome']} foi derrotado!")
                derrotados.append(inimigo)
                inimigos.remove(inimigo)

    elif player["classe"] == "Dev_admin":
        dano = player["força"] + random.randint(20, 40)
        for inimigo in inimigos[:]:
            inimigo["vida"] -= dano
            print(f"Você usou o [bold yellow]Bug do Dev[/bold yellow] em {inimigo['nome']} e causou [bold red]{dano}[/bold red] de dano")
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
        rprint(f"| Força aumentada para [red]{player['força']}[/] (+30)")
        rprint(f"| Vida aumentada para [green]{player['vida']}[/] (+20)")
        rprint("| Todos os inimigos sofrem [purple]10[/] de dano sombrio!")
        
        # Dano adicional para o Monarca
        for inimigo in inimigos[:]:
            inimigo["vida"] -= 10
            rprint(f"{inimigo['nome']} sofreu [purple]10[/] de dano das sombras!")
            if inimigo["vida"] <= 0:
                rprint(f"{inimigo['nome']} foi [bold purple]consumido pelas sombras[/]!")
                inimigos.remove(inimigo)
        
        return []
    
    return derrotados

def ganhar_xp(player, xp_ganho):
    """Exibe bonificação de XP e subida de nível com rich"""
    if player.get("monarca_sombra", False):
        # Progressão do Monarca das Sombras
        player["xp"] += xp_ganho
        
        # Painel de ganho de XP
        console.print(Panel.fit(
            f"[bold purple]{player['nome']}[/] absorveu [dark_red]{xp_ganho}[/] pontos de [black]essência sombria[/]!",
            style="purple"
        ))
        
        while player["xp"] >= player["xp_proximo_nivel"]:
            player["xp"] -= player["xp_proximo_nivel"]
            player["nivel"] += 1
            player["xp_proximo_nivel"] = int(player["xp_proximo_nivel"] * 1.5)
            
            # Tabela de atributos do Monarca
            atributos_table = Table.grid(padding=(0, 2))
            atributos_table.add_column(style="cyan", justify="right")
            atributos_table.add_column(style="white")
            
            atributos_table.add_row("Vida", f"{player['vida']} → [green]{player['vida'] + 10}[/] (+10)")
            player["vida"] += 10
            
            atributos_table.add_row("Força", f"{player['força']} → [red]{player['força'] + 5}[/] (+5)")
            player["força"] += 5
            
            atributos_table.add_row("Magia", f"{player['magia']} → [blue]{player['magia'] + 4}[/] (+4)")
            player["magia"] += 4
            
            atributos_table.add_row("Defesa", f"{player['defesa']} → [yellow]{player['defesa'] + 6}[/] (+6)")
            player["defesa"] += 6
            
            console.print(Panel.fit(
                f"[bold purple]🌑 {player['nome']}[/] ascendeu para o [black]Nível {player['nivel']}[/]!\n"
                "As [purple]sombras[/] lhe concederam:",
                box=box.DOUBLE,
                style="purple"
            ))
            console.print(atributos_table)
            console.print()
            
    else:
        # Progressão normal para outras classes
        player["xp"] += xp_ganho
        
        console.print(Panel.fit(
            f"[bold green]{player['nome']}[/] ganhou [yellow]{xp_ganho}[/] de [green]experiência[/]!",
            style="green"
        ))
        
        while player["xp"] >= player["xp_proximo_nivel"]:
            player["xp"] -= player["xp_proximo_nivel"]
            player["nivel"] += 1
            player["xp_proximo_nivel"] = int(player["xp_proximo_nivel"] * 1.5)
            
            # Calcula os bônus de atributo
            bonus = {
                "vida": 10,
                "força": 4,
                "defesa": 3,
                "magia": 4 if player["classe"] in ["Mago", "Paladino"] else 0
            }
            
            if player["classe"] == "Dev_admin":
                bonus["força"] = 10
            
            # Tabela de atributos
            atributos_table = Table.grid(padding=(0, 2))
            atributos_table.add_column(style="cyan", justify="right")
            atributos_table.add_column(style="white")
            
            for attr, value in bonus.items():
                if value > 0:
                    old_val = player[attr]
                    player[attr] += value
                    atributos_table.add_row(
                        attr.capitalize(),
                        f"{old_val} → [green]{player[attr]}[/] ([green]+{value}[/])"
                    )
            
            # Painel de subida de nível
            console.print(Panel.fit(
                f"[bold green]↑ {player['nome']}[/] subiu para o [yellow]Nível {player['nivel']}[/]!\n"
                "Seus atributos aumentaram:",
                box=box.ROUNDED,
                style="green"
            ))
            console.print(atributos_table)
            console.print()

def verificar_status_monarca(player):
    if player.get("monarca_sombra", False) and player["classe"] != "Monarca das Sombras":
        player["classe"] = "Monarca das Sombras"
        if player["habilidade"] != "Domínio das Sombras":
            player["habilidade"] = "Domínio das Sombras"
            print("\nAs sombras corrigiram seu status...")
            rprint("| » Habilidade atualizada para: [bold purple]Domínio das Sombras[/]")
    return player

def combate(player, inimigos):
    player["habilidade_usada"] = False

    rprint(Panel.fit("[bold red]COMBATE INICIADO![/]", style="red"))
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
                tocar_game()
                print("\nVocê foi derrotado! Game over!")
                input("\nPressione ENTER para continuar\n")
                parar_game()
                return False
            continue

        # Exibe status
        print(f"\n{player['nome']} (Nível: {player['nivel']}, Classe: {player['classe']}): Vida = {player['vida']} | XP = {player['xp']}/{player['xp_proximo_nivel']}")
        for i, inimigo in enumerate(inimigos):
            print(f"{i + 1}. {inimigo['nome']} (Nível: {inimigo['nivel']}, Classe: {inimigo['classe']}): Vida = {inimigo['vida']}")

        # Menu de ações
        rprint(Panel.fit("[bold]Escolha sua ação:[/]\n"
                        "1. [red]Atacar[/]\n"
                        "2. [blue]Usar item[/]\n"
                        "3. [yellow]Habilidade especial[/]"))
        
        acao = input("Sua escolha: ").strip()

        # Processa ação
        if acao == "1":
            if not inimigos:
                rprint("[yellow]Não há inimigos para atacar.[/]")
                turno_perdido = True
                continue
            
            try:
                escolha = int(input("Escolha o inimigo para atacar (número): ").strip()) - 1
                if escolha < 0 or escolha >= len(inimigos):
                    rprint("[red]Inimigo inválido![/]")
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
            rprint(f"\nVocê atacou [red]{inimigo['nome']}[/] causando [bold red]{dano}[/] de dano!")
            if inimigo["vida"] <= 0:
                rprint(f"[bold]{inimigo['nome']}[/] foi [red]derrotado[/]!")
                derrotados.append(inimigo)
                inimigos.remove(inimigo)

        elif acao == "2":
            # Lógica de itens
            rprint(Panel.fit("[bold]Seus itens:[/]\n" + 
                          "\n".join(f"- {nome_item} (x{qtd})" for nome_item, qtd in player["itens"].items())))
            
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
                    rprint("Você usou [blue]poção de cura[/] e recuperou 20 de vida\n")
                elif item_encontrado == "poção de força":
                    player["força"] += 10
                    player["itens"][item_encontrado] -= 1
                    rprint("Você usou [blue]poção de força[/] e aumentou 10 de força\n")
                elif item_encontrado == "poção de defesa":
                    player["defesa"] += 20
                    player["itens"][item_encontrado] -= 1
                    rprint("Você usou [blue]poção de defesa[/] e aumentou 20 de defesa\n")
                elif item_encontrado == "sangue de dragão":
                    player["vida"] += 50
                    player["itens"][item_encontrado] -= 1
                    rprint("Você usou [blue]sangue de dragão[/] e recuperou 50 de vida\n")
                elif item_encontrado == "vigor do vulcão":
                    player["força"] += 30
                    player["itens"][item_encontrado] -= 1
                    rprint("Você usou [blue]poção de cura[/] e aumentou 30 de força\n")
                elif item_encontrado == "sangue da montanha":
                    player["defesa"] += 30
                    player["itens"][item_encontrado] -= 1
                    rprint("Você usou [blue]sangue da montanha[/] e aumentou 30 de defesa\n")
                elif item_encontrado == "lagrimas de cura":
                    player["vida"] += 60
                    player["força"] -= 20
                    player["itens"][item_encontrado] -= 1
                    rprint("Você usou [blue]lagrimas de cura[/] e recuperou 60 de vida e perdeu 20 de força\n")
            else:
                rprint("[yellow]Você não possui item ou digitou algo incorretamente[/]")
                turno_perdido = True
                continue

        elif acao == "3":
            if player.get("habilidade_usada", False):
                rprint("[yellow]Você já usou sua habilidade neste combate![/]")
                turno_perdido = True
                continue
            
            derrotados_habilidade = habilidade_especial(player, inimigos)
            derrotados.extend(derrotados_habilidade)
            player["habilidade_usada"] = True

        else:
            rprint("[red]Ação inválida![/]")
            turno_perdido = True
            continue

        # Ataque do inimigo após ação válida do jogador
        if not turno_perdido and inimigos:
            monstro = random.choice(inimigos)
            dano_monstro = max(1, monstro["força"] - (player["defesa"] // 2))  # Garante pelo menos 1 de dano
            player["vida"] -= dano_monstro
            rprint(f"\n[red]{monstro['nome']}[/] atacou causando [bold red]{dano_monstro}[/] de dano!")
            
            if player["vida"] <= 0:
                tocar_game()
                rprint(Panel.fit("[bold red]☠ VOCÊ FOI DERROTADO! ☠[/]", style="red"))
                input("\nPressione ENTER para continuar...")
                parar_game()
                return False

    # Vitória
    rprint(Panel.fit("[bold green]VITÓRIA![/] Todos os inimigos foram derrotados!", style="green"))
    xp_total = sum([inimigo.get("nivel", 1) * 30 for inimigo in derrotados])
    ganhar_xp(player, xp_total)

    # Restauração dos atributos do Monarca
    if player["classe"] == "Monarca das Sombras" and "força_original" in player:
        if player.get("bonus_monarca", False):
            player["força"] = player["força_original"]
            player["vida"] = player["vida_original"]
        rprint("\n[purple]O poder das sombras se dissipa...[/]")
        rprint(f"| Força voltou para [red]{player['força']}[/]")
        rprint(f"| Vida voltou para [green]{player['vida']}[/]\n")
        del player["bonus_monarca"]

        if not player.get("bonus_monarca", False):
            del player["força_original"]
            del player["vida_original"]

    return True