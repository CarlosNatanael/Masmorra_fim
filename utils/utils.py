from utils.combate import combate
from conquistas_imag.sistema_conquistas import mostrar_conquista
from rich import print
from rich import print as rprint
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from rich import print as rprint
from rich.table import Table
import sys
import time
import random
import os

console = Console()

def mostrar_status_jogador(player):
    print(f"""
┌───────────────────┬───────────────────┐
│      [bold yellow]STATUS[/bold yellow]       │     [bold cyan]ATRIBUTOS[/bold cyan]     │
├───────────────────┼───────────────────┤
│                   │ Vida:   {player['vida']:<5}     │
│Nível: {player['nivel']:<8}    │ Força:  {player['força']:<5}     │
│XP: {player['xp']:<3}            │ Magia:  {player['magia']:<5}     │
│                   │ Defsa: {player['defesa']:<5}      │
┴───────────────────┴───────────────────┴
""")

def usar_itens(player, pode_usar_chave=True):
    while True:
        
        # Mostra status do jogador
        mostrar_status_jogador(player)
        
        # Filtra itens com quantidade > 0
        itens_disponiveis = {k: v for k, v in player["itens"].items() if v > 0}
        
        # Se não houver itens disponíveis
        if not itens_disponiveis:
            rprint(Panel.fit(
                "[bold red]Seu inventário está vazio![/]",
                style="red"
            ))
            input("\nPressione ENTER para continuar...")
            return True
        
        # Tabela de itens
        rprint(Panel.fit("[bold green]ITENS DISPONÍVEIS[/]", style="green"))
        
        itens_table = Table.grid(padding=(0, 2))
        itens_table.add_column("#", style="cyan")
        itens_table.add_column("Item", style="white")
        itens_table.add_column("Quantidade", style="yellow")
        
        for i, (item, qtd) in enumerate(itens_disponiveis.items(), 1):
            # Formatação especial para cada tipo de item
            if "poção" in item.lower():
                item_display = f"[red]Poção[/] de [green]{item.split()[-1]}[/]"
            elif "sangue" in item.lower():
                item_display = f"[dark_red]{item}[/]"
            elif "vigor" in item.lower():
                item_display = f"[orange_red1]{item}[/]"
            elif "chave" in item.lower():
                item_display = f"[gold1]{item}[/]"
            else:
                item_display = item
            
            itens_table.add_row(str(i), item_display, f"x{qtd}")
        
        rprint(itens_table)
        rprint(f"\n[bold cyan]{len(itens_disponiveis)+1}.[/] Continuar adiante")
        
        escolha = input("\nEscolha o item ou volte: ").strip()
        
        # Opção para continuar
        if escolha == str(len(itens_disponiveis)+1):
            return True
        
        try:
            escolha_num = int(escolha)-1
            item = list(itens_disponiveis.keys())[escolha_num]
            
            # Efeitos dos itens
            efeitos = {
                "poção de cura": {
                    "attr": "vida",
                    "valor": 20,
                    "msg": f"Você usou a [red]Poção de Cura[/] e recuperou [green]20[/] de vida ([green]{player['vida']+20}[/])"
                },
                "poção de força": {
                    "attr": "força",
                    "valor": 10,
                    "msg": f"Você usou a [red]Poção de Força[/] e aumentou [yellow]10[/] de força ([yellow]{player['força']+10}[/])"
                },
                "poção de defesa": {
                    "attr": "defesa",
                    "valor": 20,
                    "msg": f"Você usou a [red]Poção de Defesa[/] e aumentou [blue]20[/] de defesa ([blue]{player['defesa']+20}[/])"
                },
                "sangue de dragão": {
                    "attr": "vida",
                    "valor": 50,
                    "msg": f"Você usou o [dark_red]Sangue de Dragão[/] e recuperou [green]50[/] de vida ([green]{player['vida']+50}[/])"
                },
                "vigor do vulcão": {
                    "attr": "força",
                    "valor": 30,
                    "msg": f"Você usou o [orange_red1]Vigor do Vulcão[/] e aumentou [yellow]30[/] de força ([yellow]{player['força']+30}[/])"
                },
                "sangue da montanha": {
                    "attr": "defesa",
                    "valor": 30,
                    "msg": f"Você usou o [dark_red]Sangue da Montanha[/] e aumentou [blue]30[/] de defesa ([blue]{player['defesa']+30}[/])"
                },
                "chave de ébano": {
                    "attr": None,
                    "valor": None,
                    "msg": "[gold1]Chave de Ébano[/] só pode ser usada em locais específicos!"
                }
            }
            
            if item.lower() == "chave de ébano" and not pode_usar_chave:
                rprint(Panel.fit(
                    efeitos[item.lower()]["msg"],
                    style="yellow"
                ))
                input("\nPressione ENTER para continuar...")
                continue
            
            # Aplica efeito do item
            if item.lower() in efeitos:
                efeito = efeitos[item.lower()]
                
                if efeito["attr"]:
                    player[efeito["attr"]] += efeito["valor"]
                
                player["itens"][item] -= 1
                
                rprint(Panel.fit(
                    efeito["msg"],
                    style="green"
                ))
                input("\nPressione ENTER para continuar...")
                return True
            else:
                rprint(Panel.fit(
                    "[yellow]Este item ainda não tem uso definido.[/]",
                    style="yellow"
                ))
                input("\nPressione ENTER para continuar...")
                return True
                
        except (ValueError, IndexError):
            rprint(Panel.fit(
                "[red]Escolha inválida![/]",
                style="red"
            ))
            input("\nPressione ENTER para continuar...")


def tem_chave(player):
    return player["itens"].get("chave de ébano", 0) > 0

def usar_chave(player):
    itens = player.get("itens", {})
    if itens.get("chave de ébano", 0) > 0:
        itens["chave de ébano"] -= 1
        if itens["chave de ébano"] <= 0:
            del itens["chave de ébano"]
        return True
    return False

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def gerar_itens_aleatorios():
    itens_possiveis = {
        "poção de cura": "[red]Poção[/] de [green]Cura[/]",
        "poção de força": "[red]Poção[/] de [yellow]Força[/]",
        "poção de defesa": "[red]Poção[/] de [blue]Defesa[/]"
    }
    
    item_chave = random.choice(list(itens_possiveis.keys()))
    itens = [{"nome": item_chave, "display": itens_possiveis[item_chave]}]
    
    # Chance de itens adicionais (30% para 2 itens, 10% para 3 itens)
    if random.random() < 0.3:
        item_chave = random.choice(list(itens_possiveis.keys()))
        itens.append({"nome": item_chave, "display": itens_possiveis[item_chave]})
    if random.random() < 0.1:
        item_chave = random.choice(list(itens_possiveis.keys()))
        itens.append({"nome": item_chave, "display": itens_possiveis[item_chave]})
    
    return itens

def encontrar_bau(player):
    # 20% de chance de ser um baú mímico
    if random.random() < 0.2:
        rprint(Panel.fit(
            "[bold gold1]Você encontra um baú ornamentado...[/]\n"
            "[italic red]mas algo parece estranho![/]",
            style="yellow"
        ))
        time.sleep(2)
        
        rprint(Panel.fit(
            "[blink red]CRACK![/] O baú se transforma em\n"
            "uma criatura monstruosa!",
            style="red"
        ))
        time.sleep(2)
        
        mimico = {
            "nome": "[gold1]Baú Mímico[/]",
            "classe": "Monstro",
            "vida": 40 + player["nivel"] * 5,
            "força": 30 + player["nivel"] * 3,
            "defesa": 60,
            "magia": 0,
            "habilidade": "[red]Engolir[/]",
            "nivel": player["nivel"] + 2,
            "xp": 50
        }
        
        if combate(player, [mimico]):
            rprint(Panel.fit(
                "O mímico se dissolve, revelando\n"
                "[italic]itens roubados de outras vítimas![/]",
                style="gold1"
            ))
            
            itens = gerar_itens_aleatorios()
            for item in itens:
                player["itens"][item["nome"]] = player["itens"].get(item["nome"], 0) + 1
                rprint(f"Você encontrou: {item['display']}!")
            mostrar_conquista("devorador_de_mimicos")
        else:
            return False
    else:
        rprint(Panel.fit(
            "[bold gold1]Você encontrou um baú antigo![/]",
            style="yellow"
        ))
        time.sleep(2)
        
        rprint(Panel.fit(
            "Ao abri-lo, encontra alguns itens úteis...",
            style="gold1"
        ))
        
        mostrar_conquista("mestre_dos_baús")
        itens = gerar_itens_aleatorios()
        
        for item in itens:
            player["itens"][item["nome"]] = player["itens"].get(item["nome"], 0) + 1
            rprint(Panel.fit(
                f"Você encontrou: {item['display']}!",
                style="green"
            ))
    
    return True