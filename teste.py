from rich.table import Table
from rich.console import Console

console = Console()

table = Table(title="Resumo da Jornada", title_style="bold magenta")

table.add_column("Nível", justify="center", style="cyan")
table.add_column("Conquista", style="green")
table.add_column("Status", justify="right", style="bold yellow")

table.add_row("9", "Toque da Eternidade", "Desbloqueada")
table.add_row("8", "Marca do Tempo", "Concluído")
table.add_row("7", "Príncipe do Eclipse", "Concluído")

console.print(table)


from rich import print

print("[bold]Texto em negrito[/bold]")
print("[italic]Texto em itálico[/italic]")
print("[bold red]Texto vermelho e em negrito[/bold red]")
print("[underline green]Texto verde sublinhado[/underline green]")


from rich.progress import Progress
with Progress() as progress:
    task = progress.add_task("Carregando...", total=100)
    for i in range(100):
        progress.update(task, advance=1)


from rich.table import Table
table = Table(title="Ranking de Jogadores")
table.add_column("Nome", style="cyan")
table.add_column("Nível", justify="center")
table.add_row("Cael", "9")
console.print(table)

from rich.panel import Panel
console.print(Panel("Você desbloqueou uma conquista!", title="Conquista"))

from rich.console import Console
console = Console()
console.print("Texto estilizado com [bold magenta]Rich[/bold magenta]!")


from rich.text import Text
text = Text("Conquista: ")
text.append("Toque da Eternidade", style="bold red")
console.print(text)


from rich.syntax import Syntax
code = '''def ola():\n    print("Oi Cael!")'''
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)

print("[bold italic underline red]Texto estilizado[/]")


from rich.console import Console
from rich.text import Text

console = Console()

texto = Text("Este é um texto marrom!", style="tan")
console.print(texto)
