# pyinstaller masmorra.spec

from models.nivel1 import nivel_um
from models.nivel2 import nivel_dois
from models.nivel3 import nivel_tres
from models.nivel4 import nivel_quatro
from models.nivel5 import nivel_cinco
from models.nivel6_1 import nivel_verdade_1
from models.nivel6_2 import nivel_mentira_2
from models.nivel6_3 import nivel_destruicao_3
from models.nivel7_h import nivel_7_humano
from models.nivel7_s import nivel_7_sombra
from models.nivel8 import nivel_oito
from models.nivel9 import nivel_nove
from models.nivel9_s import nivel_nove_1
from models.nivel10 import nivel_dez
from utils.personagem import escolher_classe
from utils.creditos import creditos_finais
from utils.utils import limpar_terminal
from game_sound_py.menu_sound  import tocar_musica
from game_sound_py.menu_sound  import parar_musica
from game_sound_py.game_over import tocar_game
from game_sound_py.game_over import parar_game
from conquistas_imag.sistema_conquistas import get_progresso_conquistas
from conquistas_imag.sistema_conquistas import conquistas_desbloqueadas, conquistas
from rich.progress import Progress
from rich import print as rprint
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich import print
from rich.text import Text
from rich.box import SQUARE
import time
import pygame

console = Console()

pygame.init()
pygame.mixer.init()

def game_over():
    tocar_game()
    progresso = get_progresso_conquistas()
    
    rprint(Panel.fit(
        f"\n             [bold]Sua jornada termina aqui...                  [/]\n\n"
        f"            Mas suas ações serão lembradas.\n\n"
        f"          Conquistas desbloqueadas: [yellow]{progresso}[/]\n\n"
        ""
        f"             [white]Pressione ENTER para sair[/]\n",
        title="[bold white]GAME OVER[/]",
        style="red",
        border_style="red",
        width=60
    ))
    
    input()
    parar_game()
    limpar_terminal()
    main()

def verificar_save():
    """Verifica e cria arquivo de save se necessário"""
    from conquistas_imag.sistema_conquistas import SAVE_FILE
    import os
    import json
    
    if not os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'w') as f:
                json.dump([], f)
        except Exception as e:
            print(f"Erro ao criar arquivo de save: {e}")


def mostrar_status_pos_nivel(player):
    limpar_terminal()
    mostrar_status_jogador(player)
    input()
    limpar_terminal()

def mostrar_status_jogador(player):
    progresso = get_progresso_conquistas()
    nome = player['nome']
    classe = player['classe'][:15]  # Limita a 15 caracteres
    habilidade = player['habilidade'][:25]  # Limita a 25 caracteres

    topo = f"{nome}, {classe}"
    largura_total = 42
    centro = topo.center(largura_total)
    tocar_musica()
    print("╔" + "═" * largura_total + "╗")
    print(f"║{centro}║")
    print("║" + "    Prepare-se para sua Jornada!    ".center(largura_total) + "║")
    print("╚" + "═" * largura_total + "╝")

    print("┌" + "─" * 19 + "┬" + "─" * 19 + "┐")
    print("│      [bold yellow]STATUS[/bold yellow]       │     [bold cyan]ATRIBUTOS[/bold cyan]     │")
    print("├" + "─" * 19 + "┼" + "─" * 19 + "┤")
    print(f"│{'':19}│ Vida:   {player['vida']:<5}     │")
    print(f"│Classe: [bold magenta]{player['classe']:<11}[/bold magenta]│ Força:  {player['força']:<5}     │")
    print(f"│Nível: {player['nivel']:<12}│ Magia:  {player['magia']:<5}     │")
    print(f"│XP: {player['xp']:<15}│ Defesa: {player['defesa']:<5}     │")
    print("├" + "─" * 39 + "┤")
    print(f"│ Habilidade Especial: [bold yellow]{habilidade:<16}[/bold yellow] │")
    print("└" + "─" * 39 + "┘")
    rprint(Panel.fit(f"[bold gold1]Conquistas Faltantes ({progresso})[/]"))
    print("\n[bold red][Pressione ENTER para embarcar nesta aventura...][bold red]\n")
    parar_musica()

def menu_conquistas():
    limpar_terminal()
    progresso = get_progresso_conquistas()
    
    # Cria tabela de conquistas
    table = Table(
        title=f"[bold gold1]Conquistas ({progresso})[/]",
        box=SQUARE,
        border_style="blue",
        header_style="bold magenta",
        width=80
    )
    
    table.add_column("Conquista", style="cyan", width=30)
    table.add_column("Descrição", style="yellow", width=45)
    table.add_column("Status", justify="center", width=10)
    
    # Organiza conquistas por nível
    niveis = sorted({c["nivel"] for c in conquistas.values()})
    
    for nivel in niveis:
        # Adiciona cabeçalho do nível
        table.add_row(
            f"[bold green]Nível {nivel}[/]",
            f"[bold green]Conquistas do Nível {nivel}[/]",
            "[bold green]Status[/]",
            style="on black"
        )
        
        # Adiciona conquistas deste nível
        for id_conquista, dados in conquistas.items():
            if dados["nivel"] == nivel:
                status = "[bold green]V[/bold green]" if id_conquista in conquistas_desbloqueadas else "[bold red]X[/bold red]"
                estilo = "bold white" if id_conquista in conquistas_desbloqueadas else "dim"
                
                table.add_row(
                    f"[{estilo}]{dados['titulo']}[/]",
                    f"[{estilo}]{dados['descricao']}[/]",
                    status,
                    style="on black" if id_conquista in conquistas_desbloqueadas else None
                )
    
    # Mostra menu
    while True:
        console.print(table)
        console.print("\n[bold]Opções:[/]")
        console.print("1. Voltar ao menu principal")
        console.print("2. Ver apenas conquistas faltantes")
        
        escolha = input("\nEscolha uma opção: ").strip()
        
        if escolha == "1":
            break
        elif escolha == "2":
            # Filtra apenas faltantes
            rprint(Panel.fit(f"[bold gold1]Conquistas Faltantes ({progresso})[/]"))
            limpar_terminal()
        else:
            console.print("[red]Opção inválida![/]")
            time.sleep(1)
        
        limpar_terminal()

def main():
    verificar_save()
    tocar_musica()
    while True:  # Adicione este loop para o menu principal
        limpar_terminal()
        rprint("""[bold magenta]
                                 ┳┳┓                 ┓    ┏┓•   
                                 ┃┃┃┏┓┏┏┳┓┏┓┏┓┏┓┏┓  ┏┫┏┓  ┣ ┓┏┳┓
                                 ┛ ┗┗┻┛┛┗┗┗┛┛ ┛ ┗┻  ┗┻┗┛  ┻ ┗┛┗┗               
          [/bold magenta]
          [bold white]
                                         [bold green]-..--.--.+------.[/]                                          
                                      [bold green]-........-.-.......-++-[/]                                       
                                  [bold green]--.+-........---........--.++.[/]                                    
                                [bold green]-...-...[bold gold1]-+#######+++-[/].........+++-[/]                                  
                               [bold green].-.....-[bold gold1].++++#+++++###++[/]........+-++[/]                                 
                              [bold green]--...[bold gold1]--+++#++++++##++#++#-[/].......----.[/]                                
                             [bold green]..-.-+[bold gold1].+++#++++++#++++#####+[/]--....-+..+-[/]                               
                            [bold green].+.-.+[bold gold1].+++#++#++##+++#######++[/].....-+-..-+[/]                              
                          [bold green].--.....[bold gold1]++++++++++#++++########+[/]-....--.--..+-[/]                            
                         [bold green]-.-++..+.[bold gold1]#++#++++++++++#########+[/]---..--.+-...-+[/]                           
                       [bold green].-..--..--.[bold gold1]#+##+++++#++#+##########+[/]--.....#-.-..--[/]                          
                       [bold green]-...--..---[bold gold1]#+##++#++#+++###########+[/]--.--.+-+-...++ .-+[/]                      
                       [bold green]-........--[bold gold1]#+#++++++#++++.        #+-[/]..-.-+---.... --.-#.[/]                    
                       [bold green]-+--.....+.-[bold gold1]+##++++               +[/]--.--.-+.......-+...+-.[/]                   
                    [bold green].--...-++..-+..+--.                 .+--.+..+-.---++...-+---.-[/]                  
                   [bold green]---......-++++-..                                    .--------[/]                        
    [/bold white]""")
        print("""
          
    Progamador/Desenvolvimento:                                             [bold yellow][Masmorra do Fim - Versão 4.1.0][/bold yellow]
    [bold cyan]Carlos Natanael[/bold cyan]
          
    Desenvolvedor Tester:
    [bold cyan]Arthur Yabuchi[/bold cyan]
                                       
    [bold yellow]- Nivel de dificuldade adicionado[/bold yellow]         [bold yellow]- Melhorias visuais[/bold yellow]
    [bold yellow]- Novas conquistas [/bold yellow]                       [bold yellow]- Novo Menu player[/bold yellow]

                       [bold black]Copyright (C) 2025 by Carlos Natanael[/bold black] 
    """)
        estilo_texto = "dim steel_blue"
        rprint(Panel.fit("""\n[bold cyan]1[/]. [bold white]Iniciar Jogo[/]\n[bold cyan]2[/]. [bold white]Ver conquista[/]\n[bold cyan]3[/]. [bold white]Sair[/]""", style=estilo_texto, title="[bold]MENU PRINCIPAL[/]"))
        
        escolha = input("\nEscolha uma opção: ").strip()
        if escolha == "1":
            # Código existente para iniciar o jogo
            with Progress() as progress:
                task = progress.add_task("Carregando...", total=100)
                for i in range(100):
                    time.sleep(0.05)
                    progress.update(task, advance=1)
            print("\n[bold red][Pressione ENTER para embarcar nesta aventura...][bold red]\n")
            input()
            limpar_terminal()
            player, capitulo_inicial = escolher_classe()
            limpar_terminal()
            mostrar_status_jogador(player)
            input()
            parar_musica()
            limpar_terminal()

            # Dicionário de capítulos
            capitulos = {
                1: nivel_um,
                2: nivel_dois,
                3: nivel_tres,
                4: nivel_quatro,
                5: nivel_cinco,
                8: nivel_oito,
                9: nivel_nove,
                10: nivel_dez
            }

            if capitulo_inicial <= 5:
                # Capítulos lineares (1-5)
                for cap in range(capitulo_inicial, 6):
                    if not capitulos[cap](player):
                        game_over()
                        return
                    mostrar_status_pos_nivel(player)

                # Processar nível 5 (escolhas)
                resultado_nivel5 = nivel_cinco(player)
                if not resultado_nivel5:
                    game_over()
                    return

                # Processar ramificação do nível 6
                escolha_final = resultado_nivel5
                if escolha_final == "1":
                    if not nivel_verdade_1(player):
                        game_over()
                        return
                elif escolha_final == "2":
                    if not nivel_mentira_2(player):
                        game_over()
                        return
                elif escolha_final == "3":
                    if not nivel_destruicao_3(player):
                        game_over()
                        return

                mostrar_status_pos_nivel(player)

                # Processar nível 7 baseado na escolha do 6
                if resultado_nivel6 := ("humano" if escolha_final in ["1", "3"] else "sombra"):
                    if resultado_nivel6 == "humano":
                        if not nivel_7_humano(player):
                            game_over()
                            return
                    else:
                        if not nivel_7_sombra(player):
                            game_over()
                            return

                mostrar_status_pos_nivel(player)

            elif capitulo_inicial == 6:
                # Menu para escolher caminho do nível 6
                print("Escolha o caminho para o nível 6:")
                print("1. Caminho da Verdade")
                print("2. Caminho da Mentira")
                print("3. Caminho da Destruição")
                escolha = input("> ").strip()

                if escolha == "1":
                    if not nivel_verdade_1(player):
                        game_over()
                        return
                elif escolha == "2":
                    if not nivel_mentira_2(player):
                        game_over()
                        return
                elif escolha == "3":
                    if not nivel_destruicao_3(player):
                        game_over()
                        return

                mostrar_status_pos_nivel(player)

                # Continuar com nível 7
                if not nivel_7_humano(player) if escolha in ["1", "3"] else not nivel_7_sombra(player):
                    game_over()
                    return

                mostrar_status_pos_nivel(player)

            elif capitulo_inicial == 7:
                # Menu para escolher caminho do nível 7
                print("Escolha o caminho para o nível 7:")
                print("1. Caminho Humano")
                print("2. Caminho das Sombras")
                escolha = input("> ").strip()

                if escolha == "1":
                    if not nivel_7_humano(player):
                        game_over()
                        return
                elif escolha == "2":
                    if not nivel_7_sombra(player):
                        game_over()
                        return

                mostrar_status_pos_nivel(player)

            # Continuar com capítulos 8+
            for cap in range(8 if capitulo_inicial < 8 else capitulo_inicial, 11):
                if not capitulos[cap](player):
                    game_over()
                    return
                mostrar_status_pos_nivel(player)

            creditos_finais(player)

            #=====================
            #   Nivel 1
            if not nivel_um(player):
                game_over()
                return
            limpar_terminal()
            #=====================
            #   Status jogador nivel1
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
            #=====================
            #   Nivel 2
            if not nivel_dois(player):
                game_over()
                return
            limpar_terminal()
            #=====================
            #   Status jogador nivel2
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
            #=====================
            #   Nivel 3
            if not nivel_tres(player):
                game_over()
                return
            limpar_terminal()
            #=====================
            #   Status jogador nivel3
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
            #=====================
            #   Nivel 4
            if not nivel_quatro(player):
                game_over()
                return
            limpar_terminal()
            #=====================
            #   Status jogador nivel4
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
            #=====================
            #   Nivel 5
            resultado_nivel5 = nivel_cinco(player)
            if resultado_nivel5 is False:
                game_over()
                return
            if resultado_nivel5:
                escolha_final = resultado_nivel5
            #===================================================================
            #   Nivel 6_1
                if escolha_final  == "1":
                    print("""
        Você age como antes, seguindo as regras sem questionar.

        Eldramar sorri, mas não há calor em sua expressão.
        "Ordem. Respeito às estruturas. Interessante... mas será que a masmorra precisa de mais um carcereiro?"
        Ele ergue a mão, e o chão se abre sob seus pés.

        Você cai... e acorda em um lugar novo:
                    """)
                    input("Pressione ENTER para continuar")
                    limpar_terminal()
                    mostrar_status_jogador(player)
                    input()
                    limpar_terminal()
            #===================================================================
            #   Nivel 6_2
            elif escolha_final == "2":
                print("""
        Você protege a criança, mesmo sabendo que está quebrando as regras.

        Eldramar ri, um som que ecoa como vidro quebrando.
        "Ah, o herói. O justiceiro. Mas será que sua bondade sobreviverá quando você vir o que realmente habita nas sombras?"
        Ele abre um portal negro com um gesto.

        Você é sugado para dentro... e acorda em:
                """)
                input("Pressione ENTER para continuar")
                limpar_terminal()
                mostrar_status_jogador(player)
                input()
                limpar_terminal()
            #===================================================================
            #   Nivel 6_3
            elif escolha_final == "3":
                print("""
        Você resolve o conflito sem violência, mas sem ignorar a injustiça.

        Eldramar franze a testa, como se sua resposta fosse um enigma.
        "Equilíbrio... mas equilíbrio pode ser apenas covardia disfarçada."
        Ele abre um portal prateado, e você é puxado para dentro.

        Você acorda em:
                """)
                input("Pressione ENTER para continuar")
                limpar_terminal()
                mostrar_status_jogador(player)
                input()
                limpar_terminal()
            else:
                game_over()
                limpar_terminal()
                return
            resultado_nivel6 = None
            if escolha_final == "1":
                resultado_nivel6 = nivel_verdade_1(player)
            elif escolha_final == "2":
                resultado_nivel6 = nivel_mentira_2(player)
            elif escolha_final == "3":
                resultado_nivel6 = nivel_destruicao_3(player)
            if resultado_nivel6 is False:
                game_over()
                return
            limpar_terminal()
            #=====================
            #    Status jogador nivel6
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
            #==============================
            # Nivel 7 Humano
            if resultado_nivel6 == "humano":
                print("\nA luz ainda brilha em você, mas o desafio final aguarda...")
                input("\nPressione ENTER para continuar...")
                limpar_terminal()
                if not nivel_7_humano(player):
                    game_over()
                    return
            #==============================
            # Nivel 7 Sombra
            elif resultado_nivel6 == "sombra":
                print("\nAs trevas sussurram seus novos poderes... a masmorra obedece!")
                input("\nPressione ENTER para continuar...")
                limpar_terminal()
                if not nivel_7_sombra(player):
                    game_over()
                    return
            #==============================
            #    Status jogador nivel7
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
            #==============================
            #   Nivel 8
            if not nivel_oito(player):
                game_over()
                return
            limpar_terminal()
            #=====================
            #   Status jogador nivel8
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
            #=====================
            #   Nivel 9
            if not nivel_nove(player):
                game_over()
                return
            limpar_terminal()
            #=====================
            #   Status jogador nivel9
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
            #=====================
            #   Nivel 9_1
            if not nivel_nove_1(player):
                game_over()
                return
            limpar_terminal()
            #=====================
            #   Status jogador nivel9_1
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
            #=====================
            #   Nivel 10
            if not nivel_dez(player):
                game_over()
                return
            limpar_terminal()
            #=====================
            #   Status jogador nivel10
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
            #=====================
            creditos_finais(player)
        elif escolha == "2":
            menu_conquistas()
        elif escolha == "3":
            exit()
        else:
            console.print("[red]Opção inválida![/]")
            time.sleep(1)

if __name__ == "__main__":
    main()