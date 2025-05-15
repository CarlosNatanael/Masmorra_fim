from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound_py.sound10 import tocar_musica
from game_sound_py.sound10 import parar_musica
from utils.combate import combate
from rich import print
from rich import print as rprint
from rich.panel import Panel
import random
import time
import pygame


def nivel_dez(player):
    tocar_musica()
    rprint(Panel.fit("[bold yellow]Capítulo Final: O Trono de ossos e a última escolha[/]", style="blue"))

    rprint("\n[bold blue]A ASCENSÃO AO TRONO[/]\n")
    rprint("O portal de espelhos quebrados o leva a uma [bold yellow]catedral de ossos[/], onde o teto é sustentado por colunas de 'gritos petrificados'.")
    rprint("No centro, um trono feito de [bold yellow]crânios fundidos[/] irradia um calor maligno.\n")
    rprint("Dois [bold black]Comandantes da Masmorra[/] guardam o caminho:")
    print('\n"Kharath, o Lamento Encarnado"')
    print('"Sylria, a Última Memória"\n')
    print('"Os dois estão discutindo quem ira primeiro enfrentar o intruso"')
    print("Você observa os dois jogando jokenpo...")
    print("Então em instantes os dois somem\n")

    # Kharath
    print('O ar fica pesado com o som de correntes arrastando. "Kharath emerge das sombras", seu corpo uma massa de ferros retorcidos e lâminas pulsantes.')
    rprint("[bold yellow]Kharath[/]: '(voz metálica ecoando)' O Ceifador falhou... mas eu não falharei. Sua alma será minha última adição.")
    rprint(f"[bold blue]{player["nome"]}[/]: Você era o aprendiz do Ceifador?")
    rprint("[bold yellow]Kharath[/]: '(correntes rangendo)' Eu era seu sucessor! Até que...até que me tornei melhor que ele. Eldramar não gosta de rivais.")
    rprint(f"[bold blue]{player["nome"]}[/]: Então você é só mais um prisioneiro?")
    rprint("[bold yellow]Kharath[/]: '(gargalhada de metal)' Prisoneriro? Não. Eu 'ESCOLHI' isso. Pelo poder... pelo esquecimento. (correntes se esticam) Agora, 'SILÊNCIO!'")
    kharath = {
        "nome": "Kharath",
        "classe": "Guerreiro",
        "vida": 320,
        "força": 110,
        "magia": 90,
        "defesa": 110,
        "habilidade": "Corte Maligno",
        "nivel": 20,
        "xp": 5000
    }
    input("\nPrepare-se para enfrentar Kharath, o Lamento Encarnado! Pressione ENTER...\n")
    if combate(player, [kharath]):
        mostrar_conquista("fim_tirano")
    else:
        return False
    rprint("[bold yellow]Kharath[/]: Vejo agora como você escapou do abismo... Como estava o meu Mestr- !")
    print("O lamentador é derrotado e algo muda na atmosfera da Masmorra !")

    print("Você descide olhar a sua bolsa de itens.\n")
    from utils.utils import usar_itens
    if not usar_itens(player):
        return False
    time.sleep(5)

    # Sylria 
    print("O chão se transforma em veias pulsantes. Sylria desce do teto como uma aranha feita de carne viva, rostos se contorcendo em sua superfície.")
    rprint("[bold red]Sylria[/]: Vejo seu destino escrito em suas veias. Eldramar já escolheu seu fim.")
    rprint("[bold red]Sylria[/]: '(voz múltipla, suave)' Ahhh... você cheira como ela.")
    rprint("[bold red]Sylria[/]: Eu a torturei por mais de 73 dias, até que você destruiu a forja")
    rprint(f"[bold blue]{player["nome"]}[/]: Por que ajudar Eldramar?")
    rprint("[bold red]Sylria[/]: '(se aproximando)' Porque ele prometeu... que se eu te matasse... me daria um ROSTO NOVO. (os rostos gritam em uníssono)")
    rprint("[bold red]Sylria[/]: Quando este mundo acabar, apenas nós, os Escolhidos do Vazio, permaneceremos. (Dedos se alongam em garras)")

    sylria = {
        "nome": "Sylria",
        "classe": "Arqueira",
        "vida": 310,
        "força": 115,
        "magia": 90,
        "defesa": 115,
        "habilidade": "Teia sombria",
        "nivel": 20,
        "xp": 6000
    }
    input("\nPrepare-se para enfrentar Sylria, a Última Memória! Pressione ENTER...\n")
    if combate(player, [sylria]):
        mostrar_conquista("fim_tirano")
    else:
        return False
    rprint("[bold red]Sylria[/]: Eu a queria como minha amiga, mas ela roubou minha preciosa pedra...")
    print("Ela é derrotado e algo muda na atmosfera da Masmorra !")

    print("Você descide olhar a sua bolsa de itens.\n")
    from utils.utils import usar_itens
    if not usar_itens(player):
        return False
    time.sleep(5)

    # eldramar
    print("Eldramar surge do trono, um homem velho com vestes reais esfarrapadas, coroa de espinhos cravada em sua testa.")
    rprint(f"[bold blue]{player["nome"]}[/]: Por que criar essa masmorra?")
    rprint("[bold black]Eldramar[/]: Porque mortais precisam de limites. E eu sou o abismo que os contém.")
    rprint(f"[bold blue]{player["nome"]}[/]: Você não é um Deus!")
    rprint("[bold black]Eldramar[/]: Não. Sou algo antigo. E você... é apenas um acidente prestes a ser corrigido.")

    cloneEld = {
        "nome": "Eldramar",
        "classe": "Mago Supremo",
        "vida": 400,
        "força": 150,
        "magia": 500,
        "defesa": 130,
        "habilidade": "Bola sombria",
        "nivel": 50,
        "xp": 9000
    }
    input("\nPrepare-se para enfrentar seu pior pesadelo! Pressione ENTER...\n")
    if combate(player, [cloneEld]):
        mostrar_conquista("fim_tirano")
    else:
        return False


    
    # Escolha Final
    rprint(Panel.fit("[bold cyan]O Núcleo da Masmorra pulsa à sua frente...[/]"))
    rprint("[1] Destruir a Masmorra (libertar as almas)\n[2] Assumir a Monarquia das Sombras")
    escolha = input("Sua escolha: ").strip()

    if escolha == "1":
        rprint(Panel.fit("[bold green]Você destrói o núcleo, libertando as almas... mas o preço será cobrado.[/]"))
        rprint("[italic]À noite, vultos te observam das sombras...[/]")
    elif escolha == "2":
        rprint(Panel.fit("[bold purple]Você assume o Trono de Ossos. A Masmorra é sua agora.[/]"))
        rprint("[italic]Valysse surge ao seu lado, um eco na escuridão...[/]")
    else:
        rprint("[yellow]A indecisão consome tudo...[/]")

    rprint(Panel.fit("[bold]FIM.[/]"))
    parar_musica()
    return True
