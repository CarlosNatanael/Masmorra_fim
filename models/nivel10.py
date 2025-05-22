from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound_py.sound10 import tocar_musica
from game_sound_py.sound10 import parar_musica
from utils.combate import combate
from rich import print
from rich import print as rprint
from rich.panel import Panel
from time import sleep
import random
import pygame

pygame.init()
pygame.mixer.init()

def nivel_dez(player):
    tocar_musica()
    rprint(Panel.fit("[bold yellow]Capítulo Final: O Trono de ossos e a última escolha[/]", style="blue"))
    sleep(5)
    rprint("\n[bold blue]A ASCENSÃO AO TRONO[/]\n")
    sleep(5)
    rprint("O portal de espelhos quebrados o leva a uma [bold yellow]catedral de ossos[/], onde o teto é sustentado por colunas de 'gritos petrificados'.")
    sleep(5)
    rprint("No centro, um trono feito de [bold yellow]crânios fundidos[/] irradia um calor maligno.\n")
    sleep(5)
    rprint("Dois [bold black]Comandantes da Masmorra[/] guardam o caminho:")
    sleep(5)
    print('\n"Kharath, o Lamento Encarnado"')
    sleep(5)
    print('"Sylria, a Última Memória"\n')
    sleep(5)
    print('"Os dois estão discutindo quem ira primeiro enfrentar o intruso"')
    sleep(5)
    print("Você observa os dois jogando jokenpo...")
    sleep(5)
    print("Então em instantes os dois somem\n")
    sleep(5)

    num = random.choice ([1,2])

    if num == 1:
        # Kharath
        print('O ar fica pesado com o som de correntes arrastando. "Kharath emerge das sombras", seu corpo uma massa de ferros retorcidos e lâminas pulsantes.')
        sleep(5)
        rprint("[bold yellow]Kharath[/]: '(voz metálica ecoando)' O Ceifador falhou... mas eu não falharei. Sua alma será minha última adição.")
        sleep(5)
        rprint(f"[bold blue]{player["nome"]}[/]: Você era o aprendiz do Ceifador?")
        sleep(5)
        rprint("[bold yellow]Kharath[/]: '(correntes rangendo)' Eu era seu sucessor! Até que...até que me tornei melhor que ele. Eldramar não gosta de rivais.")
        sleep(5)
        rprint(f"[bold blue]{player["nome"]}[/]: Então você é só mais um prisioneiro?")
        sleep(5)
        rprint("[bold yellow]Kharath[/]: '(gargalhada de metal)' Prisoneriro? Não. Eu 'ESCOLHI' isso. Pelo poder... pelo esquecimento. (correntes se esticam) Agora, 'SILÊNCIO!'")
        sleep(5)

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
            mostrar_conquista("kharath_derrotado")
        else:
            return False
        rprint("[bold yellow]Kharath[/]: Vejo agora como você escapou do abismo... Como estava o meu Mestr- !")
        sleep(5)
        print("O lamentador é derrotado e algo muda na atmosfera da Masmorra !")
        sleep(5)
        print("Você descide olhar a sua bolsa de itens.\n")
        sleep(5)

        from utils.utils import usar_itens
        if not usar_itens(player):
            return False
        sleep(5)

        # Sylria 
        print("\nO chão se transforma em veias pulsantes. Sylria desce do teto como uma aranha feita de carne viva, rostos se contorcendo em sua superfície.")
        sleep(5)
        rprint("[bold red]Sylria[/]: Vejo seu destino escrito em suas veias. Eldramar já escolheu seu fim.")
        sleep(5)
        rprint("[bold red]Sylria[/]: '(voz múltipla, suave)' Ahhh... você cheira como ela.")
        sleep(5)
        rprint("[bold red]Sylria[/]: Eu a torturei por mais de 73 dias, até que você destruiu a forja")
        sleep(5)
        rprint(f"[bold blue]{player["nome"]}[/]: Por que ajudar Eldramar?")
        sleep(5)
        rprint("[bold red]Sylria[/]: '(se aproximando)' Porque ele prometeu... que se eu te matasse... me daria um ROSTO NOVO. (os rostos gritam em uníssono)")
        sleep(5)
        rprint("[bold red]Sylria[/]: Quando este mundo acabar, apenas nós, os Escolhidos do Vazio, permaneceremos. (Dedos se alongam em garras)")
        sleep(5)
    
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
            mostrar_conquista("sylria_derrotada")
        else:
            return False
        rprint("[bold red]Sylria[/]: Eu a queria como minha amiga, mas ela roubou minha preciosa pedra...")
        sleep(5)
        print("Ela é derrotado e algo muda na atmosfera da Masmorra !")
        sleep(5)
        print("Você descide olhar a sua bolsa de itens.\n")
        sleep(5)
        from utils.utils import usar_itens
        if not usar_itens(player):
            return False
        sleep(5)
    
    elif num == 2:
        # Sylria 
        print("\nO chão se transforma em veias pulsantes. Sylria desce do teto como uma aranha feita de carne viva, rostos se contorcendo em sua superfície.")
        sleep(5)
        rprint("[bold red]Sylria[/]: Vejo seu destino escrito em suas veias. Eldramar já escolheu seu fim.")
        sleep(5)
        rprint("[bold red]Sylria[/]: '(voz múltipla, suave)' Ahhh... você cheira como ela.")
        sleep(5)
        rprint("[bold red]Sylria[/]: Eu a torturei por mais de 73 dias, até que você destruiu a forja")
        sleep(5)
        rprint(f"[bold blue]{player["nome"]}[/]: Por que ajudar Eldramar?")
        sleep(5)
        rprint("[bold red]Sylria[/]: '(se aproximando)' Porque ele prometeu... que se eu te matasse... me daria um ROSTO NOVO. (os rostos gritam em uníssono)")
        sleep(5)
        rprint("[bold red]Sylria[/]: Quando este mundo acabar, apenas nós, os Escolhidos do Vazio, permaneceremos. (Dedos se alongam em garras)")
        sleep(5)

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
            mostrar_conquista("sylria_derrotada")
        else:
            return False
        rprint("[bold red]Sylria[/]: Eu a queria como minha amiga, mas ela roubou minha preciosa pedra...")
        sleep(5)
        print("Ela é derrotado e algo muda na atmosfera da Masmorra !")
        sleep(5)
        print("Você descide olhar a sua bolsa de itens.\n")
        sleep(5)
        from utils.utils import usar_itens
        if not usar_itens(player):
            return False
        sleep(5)

        # Kharath
        print('O ar fica pesado com o som de correntes arrastando. "Kharath emerge das sombras", seu corpo uma massa de ferros retorcidos e lâminas pulsantes.')
        sleep(5)
        rprint("[bold yellow]Kharath[/]: '(voz metálica ecoando)' O Ceifador falhou... mas eu não falharei. Sua alma será minha última adição.")
        sleep(5)
        rprint(f"[bold blue]{player["nome"]}[/]: Você era o aprendiz do Ceifador?")
        sleep(5)
        rprint("[bold yellow]Kharath[/]: '(correntes rangendo)' Eu era seu sucessor! Até que...até que me tornei melhor que ele. Eldramar não gosta de rivais.")
        sleep(5)
        rprint(f"[bold blue]{player["nome"]}[/]: Então você é só mais um prisioneiro?")
        sleep(5)
        rprint("[bold yellow]Kharath[/]: '(gargalhada de metal)' Prisoneriro? Não. Eu 'ESCOLHI' isso. Pelo poder... pelo esquecimento. (correntes se esticam) Agora, 'SILÊNCIO!'")
        sleep(5)

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
            mostrar_conquista("kharath_derrotado")
        else:
            return False
        rprint("[bold yellow]Kharath[/]: Vejo agora como você escapou do abismo... Como estava o meu Mestr- !")
        sleep(5)
        print("O lamentador é derrotado e algo muda na atmosfera da Masmorra !")
        sleep(5)
        print("Você descide olhar a sua bolsa de itens.\n")
        sleep(5)

        from utils.utils import usar_itens
        if not usar_itens(player):
            return False
        sleep(5)

    # eldramar
    print("\nEldramar surge do trono, um homem velho com vestes reais esfarrapadas, coroa de espinhos cravada em sua testa.")
    sleep(5)
    rprint(f"[bold blue]{player["nome"]}[/]: Por que criar essa masmorra?")
    sleep(5)
    rprint("[bold black]Eldramar[/]: Porque mortais precisam de limites. E eu sou o abismo que os contém.")
    sleep(5)
    rprint(f"[bold blue]{player["nome"]}[/]: Você não é um Deus!")
    sleep(5)
    rprint("[bold black]Eldramar[/]: Não. Sou algo antigo. E você... é apenas um acidente prestes a ser corrigido.")
    sleep(5)

    Eldhumano = {
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
    if combate(player, [Eldhumano]):
        mostrar_conquista("eldramar_humanoide")
    else:
        return False
    
    rprint('"(Sua forma humana se rompe, revelando um vortex de membros, olhos e dentições giratórias)"')
    sleep(5)
    rprint("[bold black]Eldramar[/]: VEJA MINHA VERDADEIRA FACE E DESESPERE!")
    sleep(5)
    rprint(f"[bold blue]{player["nome"]}[/]: O que você realmente é?!")
    sleep(5)
    rprint("[bold black]Eldramar[/]: O PRIMEIRO ERRO DA CRIAÇÃO! O PESO QUE TODOS OS MUNDOS CARREGAM!")
    sleep(5)
    rprint(f"[bold blue]{player["nome"]}[/]:Isso não é poder... é loucura!")
    sleep(5)
    rprint(f"[bold blue]{player["nome"]}[/]: LOUCURA? ISSO É LEMBRANÇA. EU SOU O QUE SOBRA QUANDO TUDO MAIS É ESQUECIDO!")
    sleep(5)

    cloneEld2 = {
        "nome": "Eldramar , Devorador de Mundos",
        "classe": "Entidade",
        "vida": 500,
        "força": 200,
        "magia": 500,
        "defesa": 190,
        "habilidade": "Obliterar",
        "nivel": 100,
        "xp": 9000
    }
    input("\nPrepare-se para enfrentar seu pior pesadelo! Pressione ENTER...\n")
    if combate(player, [cloneEld2]):
        mostrar_conquista("eldramar_monstro")
    else:
        return False
    
    rprint('"Seu núcleo exposto - um buraco negro em miniatura - paira sobre os destroços do trono"')
    sleep(5)
    rprint("[bold black]Eldramar[/]: Destrua-me... e outro tomará meu lugar. Aceite-me... e torne-se aquilo que sempre temeu.")
    sleep(5)

    # Escolha Final
    rprint(Panel.fit("\n[bold cyan]O Núcleo da Masmorra pulsa à sua frente...[/]"))
    rprint("[1] Destruir a Masmorra (libertar as almas)\n[2] Assumir a Monarquia das Sombras")
    escolha = input("Sua escolha: ").strip()

    if escolha == "1":
        rprint(f"\n[bold red]{player['nome']}[/]: [Pega sua arma] 'Isso acaba agora!'")
        sleep(5)
        rprint("[bold black]Eldramar[/]: 'Fracassei... mas Aldurian nunca estará segura. Você apenas adiou o inevitável!'")
        sleep(5)
        rprint(Panel.fit("\n[O Núcleo explode em mil fragmentos. Um portal para Aldurian se abre envolto em chamas negras]", style="black"))
        sleep(5)
        rprint(Panel.fit("[bold green]Você destrói a Masmorra, mas seu poder se funde com você:[/]"))
        sleep(5)
        rprint("- Marcas de trevas surgem em seu braço direito")
        sleep(5)
        rprint("- Os dois sóis de Aldurian agora parecem [red]sangrentos[/] aos seus olhos")
        sleep(5)
        rprint("- Nas noites sem lua, você ouve [italic]sussurros[/] das almas libertas")
        sleep(5)
        rprint("\n[bold]EPÍLOGO:[/]")
        sleep(5)
        rprint("Você retorna a Aldurian como [bold purple]O Rompedor de Correntes[/]")
        sleep(5)
        rprint("- Os reinos o celebram como herói")
        sleep(5)
        rprint("- Mas os magos notam seu novo... [red]apetite[/] por magia negra")
        sleep(5)
        rprint("- Eldramar foi derrotado, mas [italic]algo maior[/] desperta nas fronteiras do mundo")
        sleep(5)
        rprint(Panel.fit("[bold]FIM.[/]"))
        mostrar_conquista("final_destruicao")
        sleep(5)
        input("\nPressione ENTER para continuar...\n")
        parar_musica()
        return True
    elif escolha == "2":
        rprint(f"\n[bold purple]{player['nome']}[/]: 'Se este é o meu destino... que seja!'")
        sleep(5)
        rprint("[bold black]Eldramar[/]: '[italic]Sim... sim![/] Tome meu lugar, [red]filho do abismo[/]!'")
        sleep(5)
        rprint("\n[O Trono de Ossos se reforma sob seu corpo. As paredes da masmorra começam a cantar seu nome]")
        sleep(5)
        rprint(Panel.fit("[bold]Você se torna o novo Vigia:[/]"))
        sleep(5)
        rprint("- Comandantes caídos se ajoelham perante você")
        sleep(5)
        rprint("- A masmorra se reconfigura sob seu desejo")
        sleep(5)
        rprint("- No espelho do trono, você vê [italic]dezenas de versões[/] de si mesmo em outros mundos")
        sleep(5)
        rprint("\n[bold]EPÍLOGO:[/]")
        sleep(5)
        rprint("Como novo [bold black] Vigia das Sombras[/], você:")
        sleep(5)
        rprint("- Recebe visitantes... alguns voluntários, outros [red]não tão voluntários[/]")
        sleep(5)
        rprint("- Reescreve as regras da masmorra à sua imagem")
        sleep(5)
        rprint("- Nas noites mais escuras, sente Eldramar [italic]rindo[/] dentro de sua mente")
        sleep(5)
        rprint(Panel.fit("[bold]FIM.[/]"))
        mostrar_conquista("final_monarquia")
        sleep(5)
        input("\nPressione ENTER para continuar...\n")
        parar_musica()
        return True
    else:
        rprint("[yellow]A indecisão consome tudo...[/]")
        sleep(5)
        rprint(f"\n[bold blue]{player['nome']}[/]: 'Eu rejeito ambos os caminhos. Meu lar me espera!'")
        sleep(5)
        rprint("[bold black]Eldramar[/]: '[red]COVARDE![/] Você não merecia meu poder!'")
        sleep(5)
        rprint("\n[Você esfaqueia o Núcleo com sua arma. Um portal dourado se abre, mostrando seu mundo natal]")
        sleep(5)
        rprint(Panel.fit("[bold yellow]O preço do retorno:[/]"))
        sleep(5)
        rprint("- Todas suas memórias de Aldurian começam a se apagar")
        sleep(5)
        rprint("- Seus equipamentos se dissolvem em poeira cósmica")
        sleep(5)
        rprint("- Uma única marca permanece: um [italic]olho prateado[/] que vê além da realidade")
        sleep(5)
        rprint("\n[bold]EPÍLOGO:[/]")
        sleep(5)
        rprint("Você acorda em [bold green]seu mundo original[/], mas:")
        sleep(5)
        rprint("- Sonha constantemente com um [italic]palácio de ossos[/]")
        sleep(5)
        rprint("- Estranhos o reconhecem nas ruas, mas você não os lembra")
        sleep(5)
        rprint("- Às vezes, quando toca em espelhos, sente a masmorra [red]puxando[/] você de volta")
        sleep(5)
        rprint(Panel.fit("[bold]FIM.[/]"))
        mostrar_conquista("final_retorno")
        sleep(5)
        input("\nPressione ENTER para continuar...\n")
        parar_musica()
        return True