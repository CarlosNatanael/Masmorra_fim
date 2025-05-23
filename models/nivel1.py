from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound_py.sound1 import tocar_musica
from game_sound_py.sound1 import parar_musica
from utils.combate import combate
from rich import print
from rich import print as rprint
from rich.panel import Panel
import time
import os
import random
import pygame

pygame.init()
pygame.mixer.init()

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

enigmas = [
    {
        "pergunta": "Sou mais leve que uma pena, mas nem o homem mais forte consegue me segurar por muito tempo. O que sou?",
        "respostas": ["respiração", "fôlego", "ar", "sopro"]
    },
    {
        "pergunta": "Quanto mais você tira, maior eu fico. O que sou?",
        "respostas": ["buraco", "cavidade", "vala"]
    },
    {
        "pergunta": "Tenho cidades mas não tenho casas, tenho florestas mas não tenho árvores, tenho rios mas não tenho água. O que sou?",
        "respostas": ["mapa", "cartográfico"]
    },
    {
        "pergunta": "Quanto mais se tira de mim, mais eu aumento. Não sou buraco. O que sou?",
        "respostas": ["dívida", "empréstimo", "déficit"]
    },
    {
        "pergunta": "Tenho um pescoço, mas não cabeça. Tenho dois braços, mas não mãos. O que sou?",
        "respostas": ["camisa", "blusa", "roupa"]
    },
    {
        "pergunta": "Ando sem pernas, voo sem asas, choro sem olhos. O que sou?",
        "respostas": ["nuvem", "vento", "tempestade"]
    }
]

def obter_enigma_aleatorio():
    enigma = random.choice(enigmas)
    return enigma["pergunta"], enigma["respostas"]

def nivel_um(player):
    tocar_musica()
    rprint(Panel.fit("[bold yellow]Capítulo 1: O Despertar no Desconhecido[/]", style="blue"))
    time.sleep(5)
    print("\nEra uma noite chuvosa quando entrei na Biblioteca de Arcanthus, um lugar antigo e abandonado, conhecido apenas por estudiosos de ocultismo.")
    time.sleep(5)
    print("As prateleiras empoeiradas guardavam livros proibidos, manuscritos arcanos e relíquias de eras esquecidas.\n")
    print('Eu, um simples pesquisador de mitos antigos, procurava por um texto chamado "O Grimório dos Reinos Perdidos"')
    print("Um livro que supostamente continha segredos sobre dimensões paralelas. Depois de horas revirando estantes.")
    time.sleep(5)
    print("Encontrei-o escondido atrás de uma cortina de teias de aranha.")
    print("Sua capa era de couro negro, com runas vermelhas que pulsavam levemente ao toque. Ao abri-lo, uma página chamou minha atenção:")
    print('\n"Aqueles que lerem estas palavras sob a lua sangrenta serão julgados. O portal se abrirá, e o destino os aguardará além do véu."\n')
    time.sleep(5)
    print("Antes que eu pudesse reagir, as runas brilharam com intensidade, e o chão sob meus pés desapareceu.")
    print("Um vórtice de luz e sombras me engoliu, e o mundo ao meu redor se despedaçou em fragmentos de realidade.")
    time.sleep(5)
    print("Quando abri os olhos, estava deitado em um campo de flores azuis, sob um céu com dois sóis.")
    time.sleep(5)
    print('O ar cheirava a magia, e no horizonte, torres cristalinas brilhavam ao longe. Um sistema de mensagens apareceu diante de meus olhos, como se fosse parte de um jogo:\n')
    print("| » Bem-vindo, Viajante, ao Mundo de Aldurian!")
    print(f"| » [bold bright_cyan]Status atual[/bold bright_cyan]: Humano ([bold bright_yellow]{player['classe']}[/bold bright_yellow])")
    print("| » [bold bright_cyan]Objetivo[/bold bright_cyan]: Encontre seu destino ou pereça nas terras esquecidas.\n")
    time.sleep(5)
    input("\nPressione ENTER para continuar")
    print("\nVocê desperta em um santuário antigo, com símbolos místicos por toda parte...")
    print("Uma névoa azulada dança ao seu redor. Um velho encapuzado se aproxima.")
    time.sleep(5)
    print(f"\n[bold blue]Eldramar[/bold blue]: Saudações, {player['nome']}. Eu sou Eldramar, o guardião do véu entre os mundos.")
    print("[bold blue]Eldramar[/bold blue]: Você foi trazido a Aldurian por forças que nem mesmo eu compreendo por completo.")
    time.sleep(5)

    opcoes_disponiveis = {
        "1": "Fazer perguntas sobre Aldurian",
        "2": "Levantar-se e observar o local",
        "3": "Ficar em silêncio"
    }
    
    while True:
        print("\nO que você deseja fazer?")
        
        # Mostra apenas as opções ainda disponíveis
        for num, texto in opcoes_disponiveis.items():
            print(f"{num}. {texto}")
        
        escolha = input("Digite o número da sua ação: ")
        
        if escolha == "1" and "1" in opcoes_disponiveis:
            print("\n[bold blue]Eldramar[/bold blue]: Aldurian é um mundo fragmentado entre luz e trevas. Você terá um papel crucial aqui.")
            del opcoes_disponiveis["1"]  # Remove esta opção
            
        elif escolha == "2" and "2" in opcoes_disponiveis:
            print("\nVocê se levanta. As paredes do templo estão cobertas de inscrições antigas.")
            del opcoes_disponiveis["2"]  # Remove esta opção
            
        elif escolha == "3" and "3" in opcoes_disponiveis:
            print("\nVocê apenas observa em silêncio. Eldramar entende sua hesitação.\n")
            time.sleep(5)
            print(f"[bold blue]Eldramar[/bold blue]: Entendo o seu silêncio {player['nome']}, mas quero saber mais sobre sua personalidade\n")
            time.sleep(5)
            print("(Em instantes Eldramar estala os dedos e me leva um mercado aonde encontro tal situação)")
            print("(Encontro a seguinte cena a rua empoeirada, a criança faminta, a maçã roubada. O mercador gritava, a criança tremia, e eu estava parado no meio)\n")
            time.sleep(5)
            print("[bold blue]Eldramar[/bold blue]: Você vê uma criança furtando uma maçã.")
            print("1. Repreende a criança e devolve a maçã ao dono.")
            print("2. Ajudar a Criança a Fugir.")
            print("3. Pagar e Ficar em Silêncio.")

            escolha1 = input("O que faz?: ").lower()
            if escolha1 == "1":
                player["personalidade"] = "Justo"
                mostrar_conquista("guardiao_lei")
            elif escolha1 == "2":
                player["personalidade"] = "Heroico"
                mostrar_conquista("coracao_heroico")
            elif escolha1 == "3":
                player["personalidade"] = "Pacifista"
                mostrar_conquista("pacifista_iluminado")
            else:
                print("\nEscolha inválida. Assumindo natureza misteriosa.")
                player["personalidade"] = "Enigmático"
                time.sleep(5)
            print(f"\n[bold blue]Eldramar[/bold blue]: Interessante... Vejo que você é {player['personalidade']}.\n")
            break # Sai do loop quando escolhe ficar em silêncio
            
        else:
            print("Escolha inválida ou opção já selecionada. Tente novamente.")

        if len(opcoes_disponiveis) == 1 and "3" in opcoes_disponiveis:
            print("\nVocê já explorou todas as outras opções. Fica em silêncio.\n")
            time.sleep(5)
            print(f"[bold blue]Eldramar[/bold blue]: Entendo o seu silêncio {player['nome']}, mas quero saber mais sobre sua personalidade\n")
            time.sleep(5)
            print("(Em instantes Eldramar estala os dedos e me leva um mercado aonde encontro tal situação)")
            print("(Encontro a seguinte cena a rua empoeirada, a criança faminta, a maçã roubada. O mercador gritava, a criança tremia, e eu estava parado no meio)\n")
            time.sleep(5)
            print("[bold blue]Eldramar[/bold blue]: Você vê uma criança furtando uma maçã.")
            print("1. Repreende a criança e devolve a maçã ao dono.")
            print("2. Ajudar a Criança a Fugir.")
            print("3. Pagar e Ficar em Silêncio.")

            escolha1 = input("O que faz?: ").lower()
            if escolha1 == "1":
                player["personalidade"] = "Justo"
                mostrar_conquista("guardiao_lei")
            elif escolha1 == "2":
                player["personalidade"] = "Heroico"
                mostrar_conquista("coracao_heroico")
            elif escolha1 == "3":
                player["personalidade"] = "Pacifista"
                mostrar_conquista("pacifista_iluminado")
            else:
                print("\nEscolha inválida. Assumindo natureza misteriosa.")
                player["personalidade"] = "Enigmático"
                time.sleep(5)
            print(f"\n[bold blue]Eldramar[/bold blue]: Interessante... Vejo que você é {player['personalidade']}.\n")
            break
    print('"Você se pergunta em como Eldramar sabe o seu nome."\n')
    time.sleep(5)
    print(f"[bold red]{player['nome']}[/bold red]: Como você sabe meu nome?")
    time.sleep(5)
    print('\n"O mago sorri, lento, como um gato diante de um rato."\n')
    time.sleep(5)
    print("[bold blue]Eldramar[/bold blue]: Você acha que foi um acidente? Que caiu aqui por... sorte?")
    time.sleep(5)
    print('\n"Ele dá um passo à frente, e as sombras ao seu redor parecem se esticar."\n')
    time.sleep(5)
    print("[bold blue]Eldramar[/bold blue]: Nomes têm poder, jovem. E o seu... ecoou através do Véu.\n")
    time.sleep(5)
    print(f"[bold red]{player['nome']}[/bold red]: Isso não explica nada. Quem é você? O que quer?")
    time.sleep(5)
    print('\n"Eldramar ergue uma mão enrugada, e um globo de névoa escura se forma entre seus dedos, mostrando flashes do passado: a biblioteca, o grimório, o portal."\n')
    time.sleep(5)
    print("[bold blue]Eldramar[/bold blue]: Sou o último dos Vigias Eternos. Acompanhei o nascimento deste mundo, e talvez seu fim.")
    time.sleep(5)
    print("[bold blue]Eldramar[/bold blue]: (O globo se desfaz, e seu sorriso some.) Agora resta saber se você é forte o bastante para descobrir por quê.")
    time.sleep(5)
    print(f'\n"Um silêncio pesado cai. {player['nome']} sente um frio na nuca."\n')
    time.sleep(5)
    print(f"[bold red]{player['nome']}[/bold red]: Isso é uma ameaça?")
    time.sleep(5)
    print('\n"O mago vira as costas, suas vestes arrastando-se como fumaça."\n')
    time.sleep(5)
    print('[bold blue]Eldramar[/bold blue]: É um fato. Mas não se preocupe... por enquanto. "Ele olha por cima do ombro, os olhos faiscando." A masmorra fará pior.')
    time.sleep(5)
    input("\nPressione ENTER para continuar")
    print("\n[bold blue]Eldramar[/bold blue]: Antes de seguir adiante, responda ao seguinte enigma. Caso falhe, as criaturas da sombras virão cobrar o preço...\n")
    time.sleep(5)
    print(f"(E antes que {player['nome']} possa responder, Eldramar se dissolve nas sombras, deixando apenas um riso ecoando nas paredes de pedra.)\n")
    time.sleep(5)
    pergunta, respostas_possiveis = obter_enigma_aleatorio()
    print(f"\n[bold black]Voz sussurrante[/bold black]: {pergunta}")
    resposta = input("Sua resposta: ").strip().lower()
    if resposta in respostas_possiveis:
        print("\n[bold black]Voz sussurrante[/bold black]: 'Muito bem... Você poderá continuar.'")
        rprint(Panel.fit("[green]Resposta Correta![/]", style="green"))
        mostrar_conquista("sombra_sorte_1")
    else:
        time.sleep(5)
        rprint(Panel.fit("[red]X Resposta Incorreta![/]", style="red"))
        print(f"\n[bold black]Voz sussurrante[/bold black]: 'Errado... As sombras não perdoa a ignorância. Prepare-se para lutar!'\n")
        inimigos = [
            {"nome": "Sombra Goblin", "classe": "Guerreiro", "vida": 30, "força": 25, "defesa": 30, "nivel":1},
            {"nome": "Sombra Goblin", "classe": "Guerreiro", "vida": 35, "força": 28, "defesa": 30, "nivel":2}
        ]
        input("Prepare-se para o combate! Pressione ENTER...\n")
        if combate(player, inimigos):
            mostrar_conquista("exterminador_goblin_1")
        else:
            return False
        
    print(f"\n[bold black]Voz sussurrante[/bold black]: 'Agora siga, {player['classe']}. Aldurian te aguarda.'")
    time.sleep(5)
    print("Você caminha por entre árvores milenares até avistar a entrada da Masmorra do Fim...\n")

    input("\nPressione ENTER para continuar\n")
    parar_musica()
    return True