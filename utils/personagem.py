from rich import print
from rich import print as rprint
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from conquistas_imag.sistema_conquistas import mostrar_conquista
from conquistas_imag.sistema_conquistas import conquistas_desbloqueadas
from utils.utils import limpar_terminal
from rich.box import SQUARE
import time
import random

console = Console()


# Adicione no início do personagem.py
def verificar_nome_dev(nome_jogador):
    """Verifica se o nome é uma conta de desenvolvedor"""
    contas_dev = {
        "dev_master": {"nivel_acesso": 10, "capitulos": list(range(1, 11))},
    }
    return contas_dev.get(nome_jogador.lower(), None)

def menu_selecao_capitulo(capitulos_disponiveis):
    """Menu de seleção de capítulo para devs"""
    from rich import print as rprint
    from rich.panel import Panel
    from rich.table import Table
    
    capitulos_info = {
        1: "Nível 1: A Entrada Misteriosa",
        2: "Nível 2: O Salão dos Espelhos",
        3: "Nível 3: A Biblioteca Perdida",
        4: "Nível 4: O Pântano do Desespero",
        5: "Nível 5: A Sala do Guardião",
        6: "Nível 6: Escolha: humano/sombra",
        7: "Nível 7: Caminho: humano/sombra",
        8: "Nível 8: O Coração da Masmorra",
        9: "Nível 9: O Trono de Ossos",
        10: "Nível 10: O Juízo Final"
    }
    
    while True:
        limpar_terminal()
        rprint(Panel.fit("[bold magenta]SELETOR DE CAPÍTULOS - MODO DEV[/]", style="blue"))
        
        table = Table(box=SQUARE)
        table.add_column("Opção", style="cyan", width=10)
        table.add_column("Capítulo", style="yellow")
        
        for i, cap in enumerate(capitulos_disponiveis, 1):
            table.add_row(str(i), capitulos_info[cap])
        
        rprint(table)
        rprint("\n[bold]Digite o número do capítulo ou 0 para voltar[/]")
        
        escolha = input("> ").strip()
        
        if escolha == "0":
            return None
        elif escolha.isdigit() and 1 <= int(escolha) <= len(capitulos_disponiveis):
            return capitulos_disponiveis[int(escolha)-1]
        else:
            rprint("[red]Opção inválida![/]")
            time.sleep(1)


def escolher_classe():
    nome = input("Digite o nome do seu personagem: ").strip()
    print("")
    while not nome:
        nome = input("Nome não pode estar vazio. Digite novamente: ").strip()
    
    # Verifica se é conta de dev
    dev_info = verificar_nome_dev(nome)
    if dev_info:
        rprint(Panel.fit(f"[bold green]CONTA DE DESENVOLVEDOR DETECTADA![/]\nNível de acesso: {dev_info['nivel_acesso']}", style="blue"))
        capitulo = menu_selecao_capitulo(dev_info['capitulos'])
        if capitulo:
            # Cria personagem dev com capítulo selecionado
            player = criar_personagem_dev(nome)
            return player, capitulo
        else:
            rprint("[yellow]Modo dev cancelado, criando personagem normal...[/]")
            time.sleep(2)
    
    console.print(Panel.fit("\n1. [bold white]Mago[/]\n2. [bold white]Guerreiro[/]\n3. [bold white]Paladino[/]\n4. [bold white]Arqueiro[/]",style="blue", title="Escolha uma classe para o seu personagem:"))

    escolha_valida = False
    while not escolha_valida:
        escolha = input("Digite o número da classe escolhida: ")
        if escolha in ["1", "2", "3", "4"]:
            escolha_valida = True
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2, 3, 4")

    base_player = {
        "nome": nome,
        "xp": 0,
        "nivel": 1,
        "xp_proximo_nivel": 100,
        "itens": {
            "poção de cura": 3,
        }
    }

    if escolha == "1":
        base_player.update({
            "classe": "Mago",
            "vida": random.randint(40, 50),
            "força": random.randint(30, 40),
            "magia": random.randint(36, 46),
            "defesa": random.randint(30, 40),
            "habilidade": "Bola de Fogo",
            "precisao": 90,
            "arma": "Cajado"
        })
    elif escolha == "2":
        base_player.update({
            "classe": "Guerreiro",
            "vida": random.randint(45, 55),
            "força": random.randint(35, 40),
            "magia": random.randint(20, 20),
            "defesa": random.randint(35, 45),
            "habilidade": "Decapitação",
            "precisao": 90,
            "arma": "Machado"
        })
    elif escolha == "3":
        base_player["itens"]["poção de cura"] = 2
        base_player.update({
            "classe": "Paladino",
            "vida": random.randint(50, 60),
            "força": random.randint(30, 45),
            "magia": random.randint(35, 40),
            "defesa": random.randint(36, 46),
            "habilidade": "Benção Divina",
            "precisao": 90,
            "arma": "Espada"
        })
    elif escolha == "4":
        base_player.update({
            "classe": "Arqueiro",
            "vida": random.randint(45, 55),
            "força": random.randint(35, 40),
            "magia": random.randint(20, 20),
            "defesa": random.randint(35, 40),
            "habilidade": "Tiro Certeiro",
            "precisao": 95,
            "arma": "Arco"
        })

    return base_player, 1  # Retorna capítulo 1 por padrão

def transformar_em_monarca(player):
    # Salva apenas o nome e itens básicos
    nome = player["nome"]
    itens = {"poção de cura": 3}  # Itens básicos para o Monarca

    # Define os novos atributos básicos
    novo_player = {
        "nome": nome,
        "classe": "Monarca das Sombras",
        "nivel": 1,
        "xp": 0,
        "xp_proximo_nivel": 100,
        "vida": random.randint(80, 90),
        "força": random.randint(60, 70),
        "magia": random.randint(60, 80),
        "defesa": random.randint(70, 80),
        "habilidade": "Domínio das Sombras",
        "arma": "Espada negra",
        "itens": itens,
        "monarca_sombra": True  # Flag especial
    }
    
    # Atualiza o player original com os novos valores
    player.clear()
    player.update(novo_player)
    
    print("\nSua forma muda completamente. Todas as memórias anteriores se dissipam...")
    rprint("| » Você renasceu como Monarca das Sombras [bold cyab](Nível 1)[/]")
    print(f"| Status básicos: Vida {player['vida']}, Força {player['força']}, Magia {player['magia']}, Defesa {player['defesa']}\n")

    novo_player["transformado"] = True 

    if "coroa_trevas" not in conquistas_desbloqueadas:
        mostrar_conquista("coroa_trevas")
        return novo_player

    return player

def criar_personagem_dev(nome):
    """Cria personagem com atributos de desenvolvedor"""
    return {
        "nome": nome,
        "classe": "Dev_admin",
        "nivel": 99,
        "xp": 0,
        "xp_proximo_nivel": 1,
        "vida": 999,
        "força": 150,
        "magia": 200,
        "defesa": 200,
        "habilidade": "Bug do Dev",
        "precisao": 100,
        "arma": "Teclado Místico",
        "itens": {
            "poção de cura": 99,
            "chave de ébano": 1
        }
    }