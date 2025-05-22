from rich import print as rprint
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from utils.utils import limpar_terminal
from game_sound_py.menu_sound import tocar_musica, parar_musica
from conquistas_imag.sistema_conquistas import get_progresso_conquistas
from conquistas_imag.sistema_conquistas import mostrar_conquista
from conquistas_imag.sistema_conquistas import verificar_final_classe
from conquistas_imag.conquista import conquistas
from time import sleep
import os

console = Console()

def centralizar(texto, espaco_vertical=0):
    """Centraliza o conteúdo na tela"""
    console.print("\n" * espaco_vertical, end="")
    console.print(texto, justify="center")
    console.print("\n" * espaco_vertical, end="")

def creditos_finais(player):
    tocar_musica()
    verificar_final_classe(player)
    limpar_terminal()
    
    # Configuração de estilo
    estilo_titulo = "bold light_steel_blue on dark_blue"
    estilo_texto = "italic grey74"
    estilo_destaque = "wheat1"
    borda_estilo = "dim steel_blue"

    # Título principal centralizado
    centralizar(
        Panel.fit(
            "[bold]FIM DA JORNADA[/]",
            style=estilo_texto,
        ),
        0
    )
    sleep(3)
    # Mensagem de parabéns centralizada
    centralizar(
        Panel.fit(
            f"[{estilo_destaque}]Parabéns, {player['nome']}![/]\n\n"
            f"[{estilo_texto}]Sua coragem alterou o destino de Aldurian[/]\n"
            f"[{estilo_texto}]e seu nome será lembrado nas crônicas eternas[/]",
            style=borda_estilo
        ),
        1
    )
    sleep(5)
    progresso = get_progresso_conquistas()
    total_conquistas = len(conquistas) - 1
    if progresso.split('/') [0] == str(total_conquistas):
        mensagem = f"[gold1]MESTRE COMPLETO[/]\n[bold]Você coletou todas as {total_conquistas} conquistas![/]"
        mostrar_conquista("mestre_completo")
    else:
        mensagem = f"[bold]Conquistas desbloqueadas:[/] [yellow]{progresso}[/]"
    centralizar(
    Panel.fit(
        f"{mensagem}",
        style=borda_estilo,
        title="[bold white]CONQUISTAS[/]"
        ),
        1
    )

    sleep(5)
    sleep(3)
    # Título dos créditos centralizado
    centralizar(
        Panel.fit(
            "[bold]CRÉDITOS[/]",
            style=estilo_texto
        ),
        0
    )

    # Tabela de créditos centralizada
    creditos_table = Table.grid(expand=True)
    creditos_table.add_column(justify="center", style=estilo_destaque)
    creditos_table.add_column(justify="center", style=estilo_texto)
    
    creditos_table.add_row("Desenvolvido por", "Carlos Natanael")
    creditos_table.add_row("Programação", "Carlos Natanael • Val")
    creditos_table.add_row("Design de Jogo", "Equipe Aldurian")
    creditos_table.add_row("Narrativa", "Carlos Natanael")
    creditos_table.add_row("Testes", "Arthur Yabuchi")
    creditos_table.add_row("Direção Criativa", "Val")

    centralizar(
        Panel.fit(
            creditos_table,
            style=borda_estilo,
            padding=(1, 10)
        ),
        0
    )
    sleep(3)
    # Tecnologias utilizadas centralizada
    tech_table = Table.grid(expand=True)
    tech_table.add_column(justify="center", style=estilo_destaque)
    
    tech_table.add_row("[bold]Tecnologias Utilizadas[/]")
    tech_table.add_row("Python • Rich • PyGame")
    tech_table.add_row("Arte ASCII • Sistema Modular")

    centralizar(
        Panel.fit(
            tech_table,
            style=borda_estilo,
            padding=(1, 10)
        ),
        1
    )
    sleep(3)

    # Mensagem final centralizada
    centralizar(
        Panel.fit(
            f"[{estilo_texto}]Esta aventura pode ter chegado ao fim,[/]\n"
            f"[{estilo_destaque}]mas novas histórias aguardam[/]\n"
            f"[{estilo_texto}]para serem descobertas...[/]",
            style=borda_estilo
        ),
        2
    )

    # Arte final centralizada
    ascii_art = """
    [steel_blue]
██    ██  █████  ██      ███████ ██    ██     ██████   ██████  ██████           ██  ██████   ██████   █████  ██████  
██    ██ ██   ██ ██      ██      ██    ██     ██   ██ ██    ██ ██   ██          ██ ██    ██ ██       ██   ██ ██   ██ 
██    ██ ███████ ██      █████   ██    ██     ██████  ██    ██ ██████           ██ ██    ██ ██   ███ ███████ ██████  
 ██  ██  ██   ██ ██      ██      ██    ██     ██      ██    ██ ██   ██     ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ 
  ████   ██   ██ ███████ ███████  ██████      ██       ██████  ██   ██      █████   ██████   ██████  ██   ██ ██   ██ 
    [/]
    """
    centralizar(ascii_art, 1)

    rprint("\n\n[grey58]Pressione ENTER para encerrar...[/]")
    input("")
    parar_musica()
    limpar_terminal()