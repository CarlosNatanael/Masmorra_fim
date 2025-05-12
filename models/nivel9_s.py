from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound_py.sound9 import tocar_musica
from game_sound_py.sound9 import parar_musica
from utils.combate import combate
from utils.utils import encontrar_bau
from utils.utils import usar_itens
from rich import print
from rich import print as rprint
from rich.panel import Panel
from time import sleep
from rich.console import Console
import random
import pygame

pygame.init()
pygame.mixer.init()

console = Console()

def cena_fonte_negra(player):
    # Apresentação inicial
    rprint(Panel.fit("[bold]Você vê uma fonte de água negra.[/]", style="dark_blue"))
    
    # Menu de escolhas
    while True:
        rprint("\n[bold]O que você faz?[/]")
        rprint("1. [dark_goldenrod]Avançar nas sombras[/]")
        rprint("2. [blue]Ir para a fonte[/]")
        rprint("3. [green]Verificar bolsa de itens[/]")
        
        escolha = input("\nSua decisão (1-3): ").strip()
        
        if escolha == "1":
            return cena_espelho(player)
        elif escolha == "2":
            return cena_fonte_sagrada(player)
        elif escolha == "3":
            return usar_itens_menu(player)
        else:
            rprint(Panel.fit("[red]Escolha inválida! Digite 1, 2 ou 3[/]", style="red"))

def cena_espelho(player):
    rprint(Panel.fit(
        "[bold]Você entra em uma sala circular...[/]\n"
        "[italic]Um espelho perfeito reflete sua imagem... mas algo está errado.[/]",
        style="dark_blue"
    ))
    return True

def cena_fonte_sagrada(player):
    # Primeira batalha
    rprint(Panel.fit(
        "[bold red]Ao se aproximar, sombras tentam puxá-lo para dentro![/]\n"
        "[italic]Derrote-as para beber a água e recuperar energia.[/]",
        style="red"
    ))
    input("\nPressione ENTER para o combate...")
    
    inimigos = [
        {"nome": "Sombra Hobgoblin", "classe": "Guerreiro", "vida": 99, "força": 80, "defesa": 70, "nivel":9},
        {"nome": "Soldado Sombra", "classe": "Guerreiro", "vida": 105, "força": 85, "defesa": 80, "nivel":10}
    ]
    if not combate(player, inimigos):
        return False
    
    # Decisão pós-combate 1
    if not confirmar_continuar("Deseja continuar em direção à fonte sagrada?"):
        return False
    
    # Segunda batalha
    rprint(Panel.fit("[bold]Você avança mais e encontra mais monstros![/]", style="red"))
    input("\nPressione ENTER para o combate...")
    
    inimigos2 = [
        {"nome": "Sombra Lizardfolk", "classe": "Guerreiro", "vida": 119, "força": 90, "defesa": 70, "nivel":11},
        {"nome": "Mago das Sombra", "classe": "Mago", "vida": 99, "força": 100, "defesa": 70, "nivel":10},
    ]
    if combate(player, inimigos2):
        mostrar_conquista("domador_das_trevas")
    else:
        return False
    
    # Decisão pós-combate 2
    if not confirmar_continuar("Deseja continuar até a fonte sagrada?"):
        if random.random() < 0.9:
            rprint(Panel.fit("[bold]Você encontra um baú misterioso![/]", style="gold1"))
            return encontrar_bau(player)
        return True
    
    # Batalha final
    rprint(Panel.fit("[bold red]A Dama do Lago surge das águas negras![/]", style="dark_red"))
    input("\nPressione ENTER para o combate final...")
    
    trevas = {
        "nome": "Dama do Lago",
        "classe": "Mago",
        "vida": 230,
        "força": 90,
        "defesa": 90,
        "magia": 90,
        "habilidade": "Água Marinha",
        "nivel": 13,
        "xp": 600
    }
    
    if combate(player, [trevas]):
        mostrar_conquista("dama_do_lago")
        
        # Verifica se o jogador tem o dicionário de itens
        if "itens" not in player:
            player["itens"] = {}
        
        # Primeiro verifica se o baú aparece (90% de chance)
        if random.random() < 0.9:
            itens_especiais = [
                ("sangue de dragão", 0.4),    # 40% dos 30% (18% total)
                ("vigor do vulcão", 0.2),     # 20% dos 30% (3% total)
                ("sangue da montanha", 0.2)   # 20% dos 30% (9% total)
            ]
            itens, pesos = zip(*itens_especiais)
            item_especial = random.choices(itens, weights=pesos, k=1)[0]
            
            # Inicializa o item se não existir
            if item_especial not in player["itens"]:
                player["itens"][item_especial] = 0
            
            player["itens"][item_especial] += 1

            rprint(Panel.fit(
                f"[bold gold1]Você encontrou o item lendário:[/] [dark_red]{item_especial}[/]!",
                style="gold1"
            ))
            sleep(2)
            
            # Mostra inventário atualizado
            rprint(Panel.fit(
                "[bold]Inventário Atualizado:[/]",
                style="blue"
            ))
            for item, qtd in player["itens"].items():
                rprint(f"- {item}: [green]{qtd}[/]")
            
            sleep(3)
    return True

def confirmar_continuar(mensagem):
    while True:
        rprint(f"\n{mensagem}")
        escolha = input("1. Sim\n2. Não\nEscolha: ").lower().strip()
        if escolha in ["1", "sim"]:
            return True
        elif escolha in ["2", "não", "nao"]:
            return False
        rprint(Panel.fit("[red]Opção inválida! Escolha 1 ou 2[/]", style="red"))

def usar_itens_menu(player):
    rprint(Panel.fit("[bold]Você decide olhar sua bolsa de itens[/]", style="green"))
    sleep(1)
    return usar_itens(player)

def nivel_nove_1(player):
    tocar_musica()
    rprint(Panel.fit("[bold yellow]Capítulo 9: O Abismo dos defeituosos[/]", style="blue"))
    sleep(5)
    rprint(f"[bold blue]Quando o portal de Valysse se fecha, você cai em um vazio que dói.[/bold blue]")
    sleep(5)
    rprint('"Não é escuridão comum - é uma ausência que arranca pedaços da sua alma. O chão [bold black](se é que existe)[/bold black] parece carne podre sob seus pés."')
    sleep(5)
    rprint("\n[italic dark_red]Este é o Poço dos Rejeitados.[/italic dark_red]")
    sleep(5)
    rprint("- Criaturas sem propósito.\n- Pedaços de almas queimadas.\n- Memórias que a própria masmorra esqueceu.\n")
    sleep(5)
    rprint('"E agora... Você"\n')
    # Chance de encontrar baús antes da batalha final
    if random.random() < 0.4:  # 40% de chance de encontrar 1-3 baús
        num_baus = random.randint(1, 3)
        print(f"\nEnquanto avança, você encontra {num_baus} baús suspeitos...")
        
        for _ in range(num_baus):
            if not encontrar_bau(player):
                return False  # Se o jogador morrer para um mímico

    # Primeiro monstro: Ceifador Sem Foice
    rprint("""
                        "O ambiente é úmido e ecoa com gemidos distantes."
    O ar cheira a carne queimada e metal enferrujado. "Cada monstro surge das sombras, marcado por cicatrizes da forja..."
    """)
    sleep(5)
    rprint("Você avança cuidadosamente, quando de repente—")
    rprint("""
CRUNCH.

Seu pé esmaga algo no chão. Ossos.

De repente, um rangido metálico ecoa à sua frente.

[bold black]Ceifador[/bold black]: "Pare... de... pisar... em... nós..."
    """)
    rprint("""
Um esqueleto colossal, suas costelas quebradas expostas, mãos transformadas em lâminas irregulares.
           
"Ele se arrasta, cada passo fazendo suas próprias lâminas cortarem seu corpo"
    """)
    sleep(5)
    rprint('[bold black]Ceifador[/bold black]: "Você... você também foi descartado?" (voz rangendo como portão enferrujado)\n')
    sleep(5)
    rprint(f'[bold blue]{player["nome"]}[/bold blue]: O que aconteceu com você?')
    sleep(3)
    rprint('[bold black]Ceifador[/bold black]: Eu era o carrasco de Eldramar... cortava almas para a forja. "(olha para suas mãos)" "Até que uma delas... sorriu para mim.')
    sleep(5)
    rprint('[bold black]Ceifador[/bold black]: Parei o golpe. E por isso... ele me deu lâminas que nunca param de crescer. "(uma nova lâmina rompe de seu ombro, fazendo-o gritar)"\n')
    sleep(3)
    rprint(f'[bold blue]{player["nome"]}[/bold blue]: Por que não fugiu?\n')
    sleep(5)
    rprint('[bold black]Ceifador[/bold black]: Para onde? Ele colocou minha foice no meu coração... agora eu a carrego para sempre.\n')
    sleep(3)
    ceifador = {
        "nome": "Ceifador Sem Foice",
        "classe": "Guerreiro",
        "vida": 210,
        "força": 90,
        "magia": 80,
        "defesa": 90,
        "habilidade": "Morte",
        "nivel": 11 + 3,
        "xp": 550
    }
    input("\nPrepare-se para enfrentar O Ceifador Sem Foice! Pressione ENTER...\n")
    if combate(player, [ceifador]):
        mostrar_conquista("ceifeiro")
    else:
        return False
    rprint('[bold black]Ceifador[/bold black]: Eldramar tem um ritmo... três golpes, depois pausa. Conte... e ataque.')
    sleep(5)
    rprint("Você avança, mas percebe que o chão está coberto de ossos que se mexem sozinhos.\n")
    sleep(5)
    print("Você descide olhar a sua bolsa de itens.")
    from utils.utils import usar_itens
    if not usar_itens(player):
        return False
    sleep(5)

    # Segundo monstro: A Noiva de Sangue Seco
    rprint("""
Uma figura envolta em um vestido de pele remendada
           
"Seu rosto escondido por um véu de unhas humanas. Quando chora, o sangue escorre como ácido."
    """)
    sleep(5)
    rprint('[bold red]Noiva[/bold red]: Meu amor... você voltou para mim? "(voz melíflua, mas quebrada)"\n')
    sleep(3)
    rprint(f'\n[bold blue]{player["nome"]}[/bold blue]: Eu não sou quem você pensa.\n')
    sleep(5)
    rprint('[bold red]Noiva[/bold red]: "(riso triste)" Claro que não... ele nunca volta. "(ergue o véu, revelando um rosto sem boca)"')
    sleep(5)
    rprint('[bold red]Noiva[/bold red]: Eu era a esposa de Eldramar. Antes da masmorra... antes da forja.\n')
    sleep(3)
    rprint(f'[bold blue]{player["nome"]}[/bold blue]: Ele te colocou aqui?')
    sleep(5)
    rprint('\n[bold red]Noiva[/bold red]: (tocando o vestido) Não... eu me ofereci. Para salvá-lo. Mas ele já não tinha alma para salvar.')
    sleep(3)
    rprint('[bold red]Noiva[/bold red]: Agora visto os que ele matou... e choro por todos nós." (lágrimas queimam seu próprio colo)\n')
    sleep(5)
    noiva = {
        "nome": "Noiva de Sangue",
        "classe": "Maga",
        "vida": 211,
        "força": 100,
        "magia": 80,
        "defesa": 90,
        "habilidade": "Poça de sangue",
        "nivel": 13,
        "xp": 550
    }
    input("\nPrepare-se para enfrentar A Noiva de Sangue seco! Pressione ENTER...\n")
    if combate(player, [noiva]):
        mostrar_conquista("noiva_cadáver")
    else:
        return False
    rprint('[bold red]Noiva[/bold red]: Leve isto... minhas lágrimas podem dissolver suas correntes... por um instante\n')
    sleep(5)
    player["itens"]["lagrimas de cura"] = 1
    print("(A Lagrima de cura foi adicionada ao seu inventário)\n")
    for item, qtd in player["itens"].items():
        print(f"- {item}: {qtd}")
    print("\n")
    sleep(5)
    cena_fonte_negra(player)
    # Terceiro monstro: O Parceiro do Espelho
    rprint("""
Você entra em uma sala circular, onde um espelho perfeito reflete sua imagem... mas algo está errado.
           
"A cada movimento, ele envelhece e se regenera."
           
([bold red]Seu reflexo sorri sozinho.[/bold red])
    """)
    rprint('[bold green]Parceiro[/bold green]: Ah, finalmente! Um modelo digno para eu copiar!\n')
    sleep(5)
    rprint('"Ele emerge do vidro, seu corpo brilhante, mas rachaduras se espalham a cada movimento."\n')
    sleep(5)
    rprint(f'[bold blue]{player["nome"]}[/bold blue]: Você é mais um prisioneiro?')
    sleep(5)
    rprint('[bold green]Parceiro[/bold green]: O reflexo perfeito... ou quase. (sua pele descasca, revelando metal por baixo) "Eldramar me criou para substituir pessoas... mas eu sempre melhoro o original."\n')
    sleep(5)
    rprint(f'[bold blue]{player["nome"]}[/bold blue]: E por que está aqui')
    sleep(5)
    rprint('[bold green]Parceiro[/bold green]: (rindo) "Porque eu me recusei a substituir Valysse." (seu rosto se deforma momentaneamente no dela)\n')
    sleep(5)
    rprint('[bold green]Parceiro[/bold green]: Ele queria que eu fosse ela... mas ninguém pode ser aquela mulher.')
    sleep(5)
    parceiro = {
        "nome": f"Espelho {player['nome']}",
        "classe": player["classe"],
        "vida": player["vida"] * 2,
        "força": player["força"] * 2,
        "magia": player["magia"] * 2 if player["classe"] == "Mago" else 0,
        "defesa": player["defesa"] * 2,
        "habilidade": player["habilidade"],
        "nivel": player["nivel"] + 3,
        "xp": 500
    }
    input("\nPrepare-se para enfrentar O Parceiro do Espelho! Pressione ENTER...\n")
    if combate(player, [parceiro]):
        mostrar_conquista("espelho_quebrado")
    else:
        return False
    rprint('[bold green]Parceiro[/bold green]: Eldramar tem medo de [bold yellow]luz[/bold yellow]... mostre a ele o que ele realmente é.\n')
    sleep(5)
    input("\nPressione ENTER para continuar...\n")
    parar_musica()
    return True