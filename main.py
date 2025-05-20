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
    exit()

def mostrar_status_jogador(player):
    
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
    print("\n[bold red][Pressione ENTER para embarcar nesta aventura...][bold red]\n")
    parar_musica()

def mostrar_status_final(player):
    
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
                status = "✅" if id_conquista in conquistas_desbloqueadas else "❌"
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
        console.print("2. Ver apenas conquistas desbloqueadas")
        console.print("3. Ver apenas conquistas faltantes")
        
        escolha = input("\nEscolha uma opção: ").strip()
        
        if escolha == "1":
            break
        elif escolha == "2":
            # Filtra apenas desbloqueadas
            table.title = f"[bold gold1]Conquistas Desbloqueadas ({progresso})[/]"
            for row in table.rows:
                if row.cells[2] == "❌":
                    row.style = "dim"
        elif escolha == "3":
            # Filtra apenas faltantes
            table.title = f"[bold gold1]Conquistas Faltantes ({progresso})[/]"
            for row in table.rows:
                if row.cells[2] == "✅":
                    row.style = "dim"
        else:
            console.print("[red]Opção inválida![/]")
            time.sleep(1)
        
        limpar_terminal()

def main():
    tocar_musica()
    while True:  # Adicione este loop para o menu principal
        limpar_terminal()
        print("""[bold magenta]
                                 ┳┳┓                 ┓    ┏┓•   
                                 ┃┃┃┏┓┏┏┳┓┏┓┏┓┏┓┏┓  ┏┫┏┓  ┣ ┓┏┳┓
                                 ┛ ┗┗┻┛┛┗┗┗┛┛ ┛ ┗┻  ┗┻┗┛  ┻ ┗┛┗┗               
          [/bold magenta]
          [bold white]
                                         -..--.--.+------.                                          
                                      -........-.-.......-++-                                       
                                  --.+-........---........--.++.                                    
                                -...-...-+#######+++-.........+++-                                  
                               .-.....-.++++#+++++###++........+-++                                 
                              --...--+++#++++++##++#++#-.......----.                                
                             ..-.-+.+++#++++++#++++#####+--....-+..+-                               
                            .+.-.+.+++#++#++##+++#######++.....-+-..-+                              
                          .--.....++++++++++#++++########+-....--.--..+-                            
                         -.-++..+.#++#++++++++++#########+---..--.+-...-+                           
                       .-..--..--.#+##+++++#++#+##########+--.....#-.-..--                          
                       -...--..---#+##++#++#+++###########+--.--.+-+-...++ .-+                      
                       -........--#+#++++++#++++.        #+-..-.-+---.... --.-#.                    
                       -+--.....+.-+##++++               +--.--.-+.......-+...+-.                   
                    .--...-++..-+..+--.                 .+--.+..+-.---++...-+---.-                  
                   ---......-++++-..                                    .--------                        
    [/bold white]""")
        print("""
          
    Progamador/Desenvolvimento:                                             [bold yellow][Masmorra do Fim - Versão 1.0.0][/bold yellow]
    [bold cyan]Carlos Natanael[/bold cyan]
          
    Desenvolvedor Tester:
    [bold cyan]Arthur Yabuchi[/bold cyan]
                                       
    [bold yellow]- JOGO FINALIZADO[/bold yellow]                         [bold yellow]- Adição de nova poção[/bold yellow]
    [bold yellow]- Balanceamento de dano [/bold yellow]                  [bold yellow]- Novas conquistas[/bold yellow]

                       [bold black]Copyright (C) 2025 by Carlos Natanael[/bold black] 
    """)
        
        console.print("\n[bold]MENU PRINCIPAL[/]")
        console.print("1. Iniciar Jogo")
        console.print("2. Ver Conquistas")
        console.print("3. Sair")
        
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
            player = escolher_classe()
            limpar_terminal()
            mostrar_status_jogador(player)
            input()
            parar_musica()
            limpar_terminal()
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
            mostrar_status_final(player)
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