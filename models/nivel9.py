from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound_py.sound9 import tocar_musica
from game_sound_py.sound9 import parar_musica
from utils.combate import combate
from utils.utils import encontrar_bau
from rich import print
from rich import print as rprint
from rich.panel import Panel
import random
import time
import pygame

pygame.init()
pygame.mixer.init()

# Função segura para adicionar itens
def adicionar_item(player, item_nome, quantidade=1):
    if "itens" not in player:
        player["itens"] = {}
    player["itens"][item_nome] = player["itens"].get(item_nome, 0) + quantidade

def nivel_nove(player):
    tocar_musica()
    rprint(Panel.fit("[bold yellow]Capítulo 9: A Última Luz[/]", style="blue"))
    time.sleep(2)
    print("'O chão da masmorra se abre em um abismo, e você cai... só para ser recebido por luz.'")
    time.sleep(2)
    print("'Ao contrário de tudo que viu até agora'")
    time.sleep(2)
    print("O Refúgio dos Esquecidos era um lugar de resistência.")
    time.sleep(2)
    print("\nCasas feitas de ossos entrelaçados iluminadas por vagalumes em frascos...")
    time.sleep(2)
    print("\nFoi ali que você a conheceu.\n")
    time.sleep(5)
    print("Refugiados – almas que escaparam da forja, mas não conseguem sair da masmorra")
    time.sleep(2)
    print("\n'No centro, uma fonte de água negra, onde os habitantes sussurram seus nomes para não os esquecer'")
    time.sleep(2)
    print("\nFoi ali que você a conheceu.\n")
    time.sleep(5)
    print("'—— Armadura feita de lâminas quebradas de inimigos'")
    time.sleep(5)
    print("'—— Olho esquerdo perdido, substituído por um fragmento de espelho que reflete algo que não está lá'")
    time.sleep(5)
    print("'—— Braço direito envolto em correntes – as mesmas que um dia a prenderam na forja'")
    time.sleep(5)
    print("'—— Uma voz áspera, marcada por incontáveis batalhas, ecoa atrás de você':")
    time.sleep(3)
    print("\n[bold black]???[/bold black]: Você é o trouxa que destruiu a forja...") 
    time.sleep(2)
    print("—— O som de uma espada sendo desembainhada corta o ar enquanto uma figura emerge das sombras.")
    time.sleep(4)
    print("—— ela riu, sem humor.")
    time.sleep(3)
    print(f"[bold black]???[/bold black]: Prazer {player["nome"]}, meu nome é Valysse. Mas muitos me chamam de A guardiã dos Perdidos")
    time.sleep(3)
    print("\n[bold red]Valysse[/bold red]: (riso amargo) Todos no Refúgio conhecem você agora.")
    time.sleep(3)
    print("[bold red]Valysse[/bold red]: Fui Caçadora Real de Altheria antes dessa maldita masmorra me engolir.")
    time.sleep(3)
    print("[bold red]Valysse[/bold red]: Treinada nas Artes da Lâmina Fantasma... até que Eldramar achou que eu seria útil como 'combustível'.")
    time.sleep(4)
    print(f"\n[bold yellow]{player["nome"]}[/bold yellow]: Então você também foi...")
    time.sleep(2)
    print("\n[bold red]Valysse[/bold red]: (interrompe) Presa na Forja? Por 73 dias. Contei cada martelada.")
    time.sleep(3)
    print("[bold red]Valysse[/bold red]: Até que consegui escapar quando um idiota distraiu o Artesão. (olha para você significativamente)")
    time.sleep(4)
    print("\n[bold red]Valysse[/bold red]: A cidade inteira vibrou quando você destruiu a forja. Foi como... um suspiro coletivo.")
    time.sleep(3)
    print("[bold red]Valysse[/bold red]: (aperta o punho da espada) Agora só falta Eldramar vir pessoalmente terminar o serviço.")
    time.sleep(4)
    print("[bold red]Valysse[/bold red]: E quando ele vier... (toca o fragmento de espelho no olho) você não estará sozinho.")
    time.sleep(5)
    print("\nEla decide guiá-lo pelo Refúgio.")
    time.sleep(2)

    # Exploração
    if "locais_visitados_9" not in player:
        player["locais_visitados_9"] = []
    
    # [Resto da narrativa inicial...]
    
    # Sistema de visitas
    locais = {
        "1": {"id": "mercado", "nome": "Mercado das Sombras"},
        "2": {"id": "poco", "nome": "Poço dos Sussurros"},
        "3": {"id": "cabana", "nome": "Cabana de Valysse"}
    }
    
    while True:
        print("\nEscolha um local para visitar:")
        for key, local in locais.items():
            status = "(VISITADO)" if local["id"] in player["locais_visitados_9"] else ""
            print(f"{key}. {local['nome']} {status}")
        
        escolha = input("Digite o número da sua escolha (ou 0 para continuar): ")
        
        if escolha == "0":
            break
        elif escolha in locais:
            local = locais[escolha]
            if local["id"] not in player["locais_visitados_9"]:
                player["locais_visitados_9"].append(local["id"])
            
            # Cenas específicas de cada local
            if escolha == "1":
                print("\nVocê visita o Mercado das Sombras, onde memórias são trocadas como moeda.")
                time.sleep(3)
                rprint(f"\n[bold black]Comerciante[/bold black]: O que deseja jovem {player["classe"]}?")
                time.sleep(3)
                rprint("O que deseja fazer?\n1. Andar mais a frente.\n2. Olhar os produtos do comerciante\n\nOBS: Aqui os produtos custam muito caro")
                escolha1 = None
                while escolha1 not in ["1", "2"]:
                    escolha1 = input("Sua decisão (1-2): ").strip()
                    if escolha1 not in ["1", "2"]:
                        print("Escolha inválida! Digite 1 ou 2")
                time.sleep(2)
                if escolha1 == "1":
                    rprint('\n"Você descide andar pelo mercado"')
                    time.sleep(3)
                    print('[bold red]Valysse[/bold red]: "Cuidado com o homem sem lábios. Ele rouba beijos."')
                    time.sleep(4)
                    print('"Após andar com a Valysse por mais alguns mercadores, você esbarra no homem sem lábios"\n')
                    time.sleep(5)
                    if random.random() < 0.8: # 80% de chance de ser beijado
                        rprint("O homem sem lábios avança e rouba um beijo de você\n")
                        time.sleep(4)
                        player["itens"]["poção de cura"] +=1
                        rprint("Ele entrega uma [bold red]poção de cura[/bold red]")
                        time.sleep(4)
                        print("(A poção de cura foi adicionada ao seu inventário)\n")
                        print("[bold cyan]Inventario atual:[/bold cyan]")
                        for item, qtd in player["itens"].items():
                            print(f"- {item}: {qtd}")
                        mostrar_conquista("beijoqueiro")
                elif escolha1 == "2":
                        if player["vida"] <= 12:
                            rprint("\n[bold red]Comerciante:[/] Você está muito ferrado para negociar, volte quando estiver mais saudável!")
                            time.sleep(3)
                        else:
                            rprint("\n[bold black]Comerciante[/]: Venha, venha e aprecie as mercadorias")
                            time.sleep(2)
                            rprint(f"1. Poção de cura   | 'valor 12 pontos de vida'\n2. Poção de defesa | 'valor 20 pontos de vida'\n3. Poção de força  | 'valor 22 pontos de vida'\n\nSua vida atual:({player["vida"]})")
                            escolha2 = None
                            while escolha2 not in ["1", "2", "3", "4"]:
                                escolha2 = input("Sua decisão (1-3) ou 4 para sair: ").strip()
                                if escolha2 not in ["1", "2", "3", "4"]:
                                    print("Escolha inválida! Digite 1, 3 ou 4")

                            if escolha2 == "1":
                                player["itens"]["poção de cura"] +=1
                                rprint("Ele entrega uma [bold red]poção de cura[/bold red]")
                                print("(A poção de cura foi adicionada ao seu inventário)\n")
                                print("[bold cyan]Inventario atual:[/bold cyan]")
                                for item, qtd in player["itens"].items():
                                    print(f"- {item}: {qtd}")
                                player["vida"] -= 12
                                if player["vida"] <= 0:
                                    return False
                                time.sleep(4)
                                print(f"\nReduz 12 pontos de vida! |Vida: {player['vida']}|\n")
                                time.sleep(4)

                            if escolha2 == "2":
                                adicionar_item(player, "poção de defesa")
                                rprint("Ele entrega uma [bold red]poção de defesa[/bold red]")
                                print("(A poção de defesa foi adicionada ao seu inventário)\n")
                                print("[bold cyan]Inventario atual:[/bold cyan]")
                                for item, qtd in player["itens"].items():
                                    print(f"- {item}: {qtd}")
                                player["vida"] -= 20
                                if player["vida"] <= 0:
                                    return False
                                time.sleep(4)
                                print(f"\nReduz 20 pontos de vida! |Vida: {player['vida']}|\n")
                                time.sleep(4)

                            elif escolha2 == "3":
                                adicionar_item(player, "poção de força")
                                rprint("Ele entrega uma [bold red]poção de força[/bold red]")
                                print("(A poção de força foi adicionada ao seu inventário)\n")
                                print("[bold cyan]Inventario atual:[/bold cyan]")
                                for item, qtd in player["itens"].items():
                                    print(f"- {item}: {qtd}")
                                player["vida"] -= 22
                                if player["vida"] <= 0:
                                    return False
                                time.sleep(4)
                                print(f"\nReduz 22 pontos de vida! |Vida: {player['vida']}|\n")
                                time.sleep(4)

                            elif escolha2 == "4":
                                time.sleep(3)
                                rprint("\n[bold black]Comerciante[/]: Não me faça perder tempo, saia... saia")
            elif escolha == "2":
                print("\nVocê visita o Poço dos Sussurros...")
                time.sleep(3)
                # Chance de encontrar baús antes da batalha final
                if random.random() < 0.6:  # 50% de chance de encontrar 1-3 baús
                    num_baus = random.randint(1, 3)
                    print(f"\nEnquanto avança, você encontra {num_baus} baús suspeitos...")
                    for _ in range(num_baus):
                        if not encontrar_bau(player):
                            return False  # Se o jogador morrer para um mímico
                time.sleep(3)
                print("Os ecos dos arrependimentos sussurram que Eldramar teme o poder da Fonte Negra.")
            elif escolha == "3":
                print("\nVocê visita a Cabana de Valysse...")
                print("\nVocê visita a cabana de Valysse, cheia de nomes riscados nas paredes.")
                time.sleep(2)
                print('[bold red]Valysse[/bold red]: Todos que eu não consegui salvar, ela murmura.')
    
    # Verificação final
    if len(player["locais_visitados_9"]) >= 3:
        mostrar_conquista("guardiao_perdido")

    # Ataque de Eldramar
    print("\nEldramar surge como um vendaval de ódio, seu corpo distorcido agora visível em toda sua monstruosidade:")
    time.sleep(3)
    print('\n[bold black]Eldramar[/bold black]: "INSOLENTE! VOCÊ ROUBOU MEU PODER, AGORA ROUBARÁ SUA MORTE!"')
    time.sleep(3)
    print("\nSeus dedos se alongam em garras negras, prontas para esmagar seu crânio...")
    time.sleep(4)

    Eldramar = {
        "nome": "Eldramar",
        "classe": "Mago Supremo",
        "vida": 400,
        "força": 400,
        "magia": 300,
        "defesa": 1000,
        "habilidade": "Bola sombria",
        "nivel": 50,
        "xp": 15000
    }
    input("\nPrepare-se para enfrentar seu pior pesadelo! Pressione ENTER...\n")
    combate(player, [Eldramar])

    print('\n[bold red]Valysse[/bold red]: (gritando enquanto salta na frente) "NÃO HOJE, VERME!"')
    time.sleep(2)
    print('\n"Antes que [bold black]Eldramar[/bold black] diferisse o ultimo golpe [bold red]Valysse[/bold red] defende, repelindo o golpe do Mago"')
    time.sleep(6)
    tocar_musica()
    print("\nSua espada brilha com uma luz prateada - o mesmo material de seu olho artificial - bloqueando o golpe fatal.")
    time.sleep(4)
    print('\n[bold black]Eldramar[/bold black]: (rindo) "A LÂMINA FANTASMA? VOCÊ NÃO APRENDEU NADA, MENINA."')
    time.sleep(3)
    print("\nUm chicote de sombra envolve o braço de Valysse, fazendo sangue escuro jorrar.")
    time.sleep(3)
    print(f'\n[bold red]Valysse[/bold red]: (para {player["nome"]}, urgente) "Ouça bem - ele tem um núcleo sob a clavícula direita!"')
    time.sleep(3)
    print('[bold red]Valysse[/bold red]: "Quando eu disser CORRA, vá para a fonte e GRITE meu nome!"')
    time.sleep(3)
    print("\nValysse agarra seu próprio olho de espelho e o esmaga no chão:")
    time.sleep(2)
    print('\n[bold red]Valysse[/bold red]: "AGORA! CORRA!"')
    time.sleep(1)
    print("\nUma explosão de luz cega Eldramar momentaneamente.")
    time.sleep(2)

    print("\nVocê se lança em direção à fonte enquanto:")
    time.sleep(2)
    print("- As correntes de luz de Valysse prendem Eldramar como serpentes douradas")
    print("- O chão treme com os berros do vilão")
    print("- Sangue escorre das narinas de Valysse, mas ela mantém o feitiço")
    time.sleep(5)

    print('\nVocê alcança a fonte e grita: "VALYSSE DE ALTHERIA!"')
    time.sleep(2)
    print("\nA água negra se transforma em vapor de prata, formando um portal giratório.")
    time.sleep(3)

    print("\nValysse olha para você pela última vez, seu corpo começando a se desintegrar:")
    time.sleep(3)
    print('\n[bold red]Valysse[/bold red]: "Tome isto... meu último golpe guardado..."')
    time.sleep(2)
    print("\nUma estrela de luz voa de seu coração até seu peito.")
    time.sleep(2)

    player["vida"] += 350
    player["força"] += 20
    player["magia"] += 20

    print("*Você ganha: []A Pedra da Fúria Elemental[]")
    print(f"| → Força aumentada para [bold green]{player["força"]}[/bold green] ([bold green]↑[/bold green] 20)")
    print(f"| → Vida aumentada para [bold green]{player["vida"]}[/bold green] ([bold green]↑[/bold green] 20)")
    print(f"| → Magia aumentada para [bold green]{player["magia"]}[/bold green] ([bold green]↑[/bold green] 20)")
    mostrar_conquista("furia_elemental")
    time.sleep(5)

    print('\n[bold red]Valysse[/bold red]: (sorrindo) "Mate-o... por todos nós..."')
    time.sleep(2)
    print("\n'Eldramar finalmente se liberta e lança uma CHAMA SOMBRIA em Valysse pelas costas!'")
    time.sleep(2)
    print('\n[bold black]Eldramar[/bold black]: "SEU SACRIFÍCIO FOI TÃO INÚTIL QUANTO SUA VIDA!"')
    time.sleep(3)
    print("\nO corpo de Valysse se dissolve em pétalas de luz...")
    time.sleep(3)

    print("\nO portal está aberto, mas Eldramar bloqueia seu caminho:")
    time.sleep(2)
    print('\n[bold black]Eldramar[/bold black]: "FUGIR? NUNCA. VOCÊ SERÁ O PRÓXIMO LINGOTE DA FORJA!"')
    time.sleep(3)
    print("\nQuando ele avança, os últimos vestígios do poder de Valysse O EMPURRAM PARA O PORTAL!")
    time.sleep(3)

    print('\nVocê ouve sua voz ecoar: "ENCONTRE O CORAÇÃO VERDADEIRO DA MASMORRA!"')
    time.sleep(3)
    print("\nO portal se fecha mostrando Eldramar lançando um buraco negro sobre a cidade da resistência...")
    time.sleep(3)
    print("\nVocê chega em um novo local - O Abismo dos defeituosos - com o símbolo de Valysse queimando em seu peito.")
    mostrar_conquista("ultima_luz")
    time.sleep(4)
    input("\nPressione ENTER para continuar...\n")
    parar_musica()
    return True