from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound.sound import tocar_musica
from game_sound.sound import parar_musica
from utils.combate import combate
import time
import pygame

pygame.init()
pygame.mixer.init()

def nivel_nove(player):
    tocar_musica()
    print("Capítulo 9: A Última Luz\n")
    time.sleep(2)
    print("O chão da masmorra se abre em um abismo, e você cai... só para ser recebido por luz.")
    time.sleep(2)
    print("Ao contrário de tudo que viu até agora")
    time.sleep(2)
    print("O Refúgio dos Esquecidos era um lugar de resistência.")
    time.sleep(2)
    print("\nCasas feitas de ossos entrelaçados iluminadas por vagalumes em frascos...")
    time.sleep(2)
    print("\nFoi ali que você a conheceu.\n")
    time.sleep(5)
    print("Refugiados – almas que escaparam da forja, mas não conseguem sair da masmorra")
    time.sleep(2)
    print("\nNo centro, uma fonte de água negra, onde os habitantes sussurram seus nomes para não os esquecer")
    time.sleep(2)
    print("\nFoi ali que você a conheceu.\n")
    time.sleep(5)
    print("Armadura feita de lâminas quebradas de inimigos")
    time.sleep(5)
    print("Olho esquerdo perdido, substituído por um fragmento de espelho que reflete algo que não está lá")
    time.sleep(5)
    print("Braço direito envolto em correntes – as mesmas que um dia a prenderam na forja")
    time.sleep(5)
    print("\nUma voz áspera, marcada por incontáveis batalhas, ecoa atrás de você:")
    time.sleep(3)
    print("\n??? : Você é o trouxa que destruiu a forja...") 
    time.sleep(2)
    print("—— O som de uma espada sendo desembainhada corta o ar enquanto uma figura emerge das sombras.")
    time.sleep(4)
    print("—— ela riu, sem humor.")
    time.sleep(3)
    print(f"??? : Prazer {player["nome"]}, meu nome é Valysse. Mas muitos me chamam de A guardiã dos Perdidos")
    time.sleep(3)
    print("\nValysse : (riso amargo) Todos no Refúgio conhecem você agora.")
    time.sleep(3)
    print("Valysse : Fui Caçadora Real de Altheria antes dessa maldita masmorra me engolir.")
    time.sleep(3)
    print("Valysse : Treinada nas Artes da Lâmina Fantasma... até que Eldramar achou que eu seria útil como 'combustível'.")
    time.sleep(4)
    print(f"\n{player["nome"]} : Então você também foi...")
    time.sleep(2)
    print("\nValysse : (interrompe) Presa na Forja? Por 73 dias. Contei cada martelada.")
    time.sleep(3)
    print("Valysse : Até que consegui escapar quando um idiota distraiu o Artesão. (olha para você significativamente)")
    time.sleep(4)
    print("\nValysse : A cidade inteira vibrou quando você destruiu a forja. Foi como... um suspiro coletivo.")
    time.sleep(3)
    print("Valysse : (aperta o punho da espada) Agora só falta Eldramar vir pessoalmente terminar o serviço.")
    time.sleep(4)
    print("Valysse : E quando ele vier... (toca o fragmento de espelho no olho) você não estará sozinho.")
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
                print("\nVocê visita o Mercado das Sombras...")
                print("\nVocê visita o Mercado das Sombras, onde memórias são trocadas como moeda.")
                time.sleep(2)
                print('Valysse : "Cuidado com o homem sem lábios. Ele rouba beijos."')
            elif escolha == "2":
                print("\nVocê visita o Poço dos Sussurros...")
                time.sleep(2)
                print("Os ecos dos arrependimentos sussurram que Eldramar teme o poder da Fonte Negra.")
            elif escolha == "3":
                print("\nVocê visita a Cabana de Valysse...")
                print("\nVocê visita a cabana de Valysse, cheia de nomes riscados nas paredes.")
                time.sleep(2)
                print('Valysse : Todos que eu não consegui salvar, ela murmura.')
    
    # Verificação final
    if len(player["locais_visitados_9"]) >= 3:
        mostrar_conquista("guardiao_perdido")

    # Ataque de Eldramar
    print("\nEldramar surge como um vendaval de ódio, seu corpo distorcido agora visível em toda sua monstruosidade:")
    time.sleep(3)
    print('\nEldramar: "INSOLENTE! VOCÊ ROUBOU MEU PODER, AGORA ROUBARÁ SUA MORTE!"')
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

    tocar_musica()
    print('\nValysse: (gritando enquanto salta na frente) "NÃO HOJE, VERME!"')
    time.sleep(2)
    print("\nSua espada brilha com uma luz prateada - o mesmo material de seu olho artificial - bloqueando o golpe fatal.")
    time.sleep(4)
    print('\nEldramar: (rindo) "A LÂMINA FANTASMA? VOCÊ NÃO APRENDEU NADA, MENINA."')
    time.sleep(3)
    print("\nUm chicote de sombra envolve o braço de Valysse, fazendo sangue escuro jorrar.")
    time.sleep(3)
    print(f'\nValysse: (para {player["nome"]}, urgente) "Ouça bem - ele tem um núcleo sob a clavícula direita!"')
    time.sleep(3)
    print('Valysse: "Quando eu disser CORRA, vá para a fonte e GRITE meu nome!"')
    time.sleep(3)
    print("\nValysse agarra seu próprio olho de espelho e o esmaga no chão:")
    time.sleep(2)
    print('\nValysse: "AGORA! CORRA!"')
    time.sleep(1)
    print("\nUma explosão de luz cega Eldramar momentaneamente.")
    time.sleep(2)

    print("\nVocê se lança em direção à fonte enquanto:")
    time.sleep(2)
    print("- As correntes de luz de Valysse prendem Eldramar como serpentes douradas")
    print("- O chão treme com os berros do vilão")
    print("- Sangue escorre das narinas de Valysse, mas ela mantém o feitiço")
    time.sleep(5)

    print('\nVocê alcança a fonte e grita: "Valysse DE ALTHERIA!"')
    time.sleep(2)
    print("\nA água negra se transforma em vapor de prata, formando um portal giratório.")
    time.sleep(3)

    print("\nValysse olha para você pela última vez, seu corpo começando a se desintegrar:")
    time.sleep(3)
    print('\nValysse: "Tome isto... meu último golpe guardado..."')
    time.sleep(2)
    print("\nUma estrela de luz voa de seu coração até seu peito.")
    time.sleep(2)

    player["vida"] += 120
    player["força"] += 20
    player["magia"] += 20

    print("*Você ganha: A Pedra da Fúria Elemental")
    print(f"| → Força aumentada para {player["força"]} (+20)")
    print(f"| → Vida aumentada para {player["vida"]} (+20)")
    print(f"| → Magia aumentada para {player["magia"]} (+20)")
    mostrar_conquista("furia_elemental")
    time.sleep(5)

    print('\nValysse: (sorrindo) "Mate-o... por todos nós..."')
    time.sleep(2)
    print("\nEldramar finalmente se liberta e lança uma CHAMA SOMBRIA em Valysse pelas costas!")
    time.sleep(2)
    print('\nEldramar: "SEU SACRIFÍCIO FOI TÃO INÚTIL QUANTO SUA VIDA!"')
    time.sleep(3)
    print("\nO corpo de Valysse se dissolve em pétalas de luz...")
    time.sleep(3)

    print("\nO portal está aberto, mas Eldramar bloqueia seu caminho:")
    time.sleep(2)
    print('\nEldramar: "FUGIR? NUNCA. VOCÊ SERÁ O PRÓXIMO LINGOTE DA FORJA!"')
    time.sleep(3)
    print("\nQuando ele avança, os últimos vestígios do poder de Valysse O EMPURRAM PARA O PORTAL!")
    time.sleep(3)

    print('\nVocê ouve sua voz ecoar: "ENCONTRE O CORAÇÃO VERDADEIRO DA MASMORRA!"')
    time.sleep(3)
    print("\nO portal se fecha mostrando Eldramar lançando um buraco negro sobre a cidade da resistência...")
    time.sleep(3)
    print("\nVocê chega em um novo local - O SANTUÁRIO ESQUECIDO - com o símbolo de Valysse queimando em seu peito.")
    mostrar_conquista("ultima_luz")
    time.sleep(4)
    input("\nPressione ENTER para continuar...\n")
    parar_musica()
    return True