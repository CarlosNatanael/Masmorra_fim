from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound.sound1 import tocar_musica
from game_sound.sound1 import parar_musica
from utils.combate import combate
from utils.utils import tem_chave
from utils.utils import usar_chave
import random
import time
import pygame

pygame.init()
pygame.mixer.init()

def nivel_quatro(player):
    tocar_musica()
    print("Capítulo 4: O Pântano do Desespero\n")
    time.sleep(5)
    print("""
O ar cheirava a folhas apodrecidas e carne em decomposição. Árvores esqueléticas se contorciam como dedos ossudos, 
e a água estagnada borbulhava com coisas se movendo sob a superfície.
    """)
    print("Você descide olhar a sua bolsa de itens.\n")
    from utils.utils import usar_itens
    if not usar_itens(player):
        return False
    time.sleep(5)
    print("\n(Você continua e pisa em algo macio.)")
    print("(Era um rosto.)\n")
    print("Um cadáver preservado pelo pântano, seus olhos ainda abertos, a boca congelada em um grito silencioso.")
    print('??? : "Bem-vindo ao Pântano das Almas Perdidas," sussurrou uma voz na névoa. ')
    print("??? : Você vai ser o próximo? um passo em falso pode custar caro...\n")
    caminhos = ["esquerda", "direita", "frente"]
    caminho_correto = random.choice(caminhos)

    tentativa = input("Você caminha para (esquerda, direita ou frente)? ").lower()
    if tentativa != caminho_correto:
        print("\nVocê pisa em uma área traiçoeira! Criaturas emergem da lama!\n")
        time.sleep(3)

        monstros = [
            {"nome": "Lizard", "classe": "Guerreiro", "vida": 70, "força": 39, "magia": 20, "defesa": 30, "nivel": 4},
            {"nome": "Golem do pântano", "classe": "Guerreiro", "vida": 80, "força": 30, "magia": 30, "defesa": 60, "nivel": 5}
        ]

        input("Prepare-se para o combate! Pressione ENTER...\n")
        if combate(player, monstros):
            mostrar_conquista("quebrador_pedra_2")
        else:
            return False
        print("\nVocê derrota as criaturas e continua, coberto de lama e suor...\n")
    else:
        print("\nVocê avança cuidadosamente e encontra uma trilha firme. Parece o caminho certo!\n")
        mostrar_conquista("sombra_sorte_3")
        time.sleep(3)

    print("Ao longe, um brilho vermelho corta a névoa... uma criatura gigante se aproxima!")
    print("Ela é feita de galhos, ossos e lodo... olhos como carvões em brasa.\n")
    print("Chefe do Pântano: Grumor, o Devorador de Errantes.\n")

    chefe = {
        "nome": "Grumor, o Devorador de Errantes",
        "classe": "Besta",
        "vida": 120,
        "força": 40,
        "magia": 40,
        "defesa": 50,
        "habilidade": "Sufocamento de Lama",
        "nivel": player["nivel"] + 3,
    }

    input("Prepare-se para o confronto final do nível! Pressione ENTER...\n")
    if combate(player, [chefe]):
        mostrar_conquista("devorador_devorado")
    else:
        return False

    print("\nGrumor desfaz-se em lama fétida e galhos partidos.\n")
    print("\n" + "="*60)
    print("O chão começa a tremer violentamente!".center(60))
    print("="*60 + "\n")
    time.sleep(2)
    print("Diante de seus olhos, a poça de água negra se agita como se fervesse.")
    time.sleep(3)
    print("Das profundezas, uma massa de rocha negra emerge lentamente, arrastando-se para a superfície...\n")
    time.sleep(4)
    print("A rocha se ergue, revelando-se maior que uma casa, e em sua face frontal,")
    print("um símbolo ancestral começa a brilhar com uma luz púrpura pulsante.\n")
    time.sleep(5)
    print("O ar vibra com energia arcana enquanto você se aproxima.")
    print("O símbolo se transforma em uma complexa fechadura mágica que emite um zumbido baixo.")
    time.sleep(4)

    if tem_chave(player):
        while True:
            print("\n" + "━"*40)
            print(" O selo reconhece sua presença! ".center(40, "~"))
            print("━"*40 + "\n")

            print(f"1. {player['classe']} | Usar {player['habilidade']} no selo")
            print(f"2. Tentar romper o selo bruscamente [Força: {player['força']}]")
            print("3. Inserir a chave de ébano")
            print("━"*40)

            escolha = input("Sua decisão: ").strip()

            if escolha == "3":
                if usar_chave(player):
                    print("\nA chave se encaixa perfeitamente, como se fosse feita para este momento.")
                    time.sleep(2)
                    print("O símbolo ancestral começa a girar, cada runa se acendendo em sequência...\n")
                    time.sleep(3)
                    print("A rocha treme violentamente, rachando-se no meio!\n")
                    time.sleep(2)
                    print("Dentro da fissura, um vórtice de energia púrpura se forma, crescendo até")
                    print("atingir o tamanho de um portal plenamente funcional.\n")
                    time.sleep(4)
                    print("O portal estabiliza, mostrando visões de um corredor infinito repleto de estrelas")
                    input("\nPressione ENTER para atravessar o portal...")
                    parar_musica()
                    return True
                else:
                    print("\nVocê revira seus bolsos, mas a chave não está lá!")
                    time.sleep(2)
                    continue

            elif escolha == "1":
                if not player.get("atacou_rocha", False):
                    print("\nVocê conjura sua habilidade, mas a magia ancestral da rocha absorve o ataque sem efeito!")
                    time.sleep(2)
                    print("Um impacto violento ecoa pela caverna...")
                    time.sleep(3)

                    print("A rocha não cedeu, mas agora apresenta pequenas rachaduras pulsantes.")
                    print("Você sente uma energia antiga se agitando dentro dela...")
                    time.sleep(3)

                    player["atacou_rocha"] = True
                    
                elif player.get("atacou_rocha"):
                    print("\nVocê conjura novamente sua habilidade, e novamente a magia ancestral da rocha absorve o ataque")
                    time.sleep(2)
                    print("As rachaduras começam a brilhar intensamente...")
                    time.sleep(3)
                    print("Pedras e terra se aglutinam, formando uma figura colossal!\n")
                    time.sleep(3)

                    print("""
╔════════════════════════════════════════════════╗
║            A ROCHA GANHA VIDA!                 ║
║                                                ║
║        UM GOLEM DE FOGO DESPERTA!              ║
╚════════════════════════════════════════════════╝
                    """)
                    time.sleep(5)

                    golem = {
                        "nome": "Golem de Fogo Ancestral",
                        "classe": "Guerreiro",
                        "vida": 120,
                        "força": 55,
                        "defesa": 80,
                        "habilidade": "Impacto Sísmico",
                        "nivel": player["nivel"] + 2,
                        "xp": 200
                    }

                    if combate(player, [golem]):
                        mostrar_conquista("quebrador_pedra_3_fogo")
                    else:
                        return False
                
                    print("\nO golem se desfaz em pedras, revelando o portal instável por trás dele!")
                    input("\nPressione ENTER para atravessar o portal...")
                    parar_musica()
                    return True
                continue
        
            elif escolha == "2":
                if not player.get("atacou_rocha", False):
                    print("\nVocê cerra os punhos e investe contra a rocha com toda a sua força!")
                    time.sleep(2)
                    print("Um impacto violento ecoa pela caverna...")
                    time.sleep(3)

                    if player.get("força",0) > 36:
                        dano_sofrido = 10
                        print("Sua força impressionante reduz o dano recebido!")
                    else:
                        dano_sofrido = 15
                    
                    player["vida"] -= dano_sofrido
                    

                    print(f"\n╔{'═'*60}╗")
                    print(f"║{'CRÍTICO!'.center(60)}║")
                    print(f"║{'Você se machucou gravemente!'.center(60)}║")
                    print(f"║{f'-{dano_sofrido} de vida'.center(60)}║")
                    print(f"║{f'Vida atual: {player['vida']}'.center(60)}║")
                    print(f"╚{'═'*60}╝\n")
                    time.sleep(3)

                    print("A rocha não cedeu, mas agora apresenta pequenas rachaduras pulsantes.")
                    print("Você sente uma energia antiga se agitando dentro dela...")
                    time.sleep(3)

                    player["atacou_rocha"] = True
                    
                    if player["vida"] <= 0:
                        print("\nSua ferida é grave demais para continuar...")
                        return False
                    
                elif player.get("atacou_rocha"):
                    print("\nVocê golpeia a rocha novamente, ignorando a dor!")
                    mostrar_conquista("punhos_aco")
                    time.sleep(2)
                    print("As rachaduras começam a brilhar intensamente...")
                    time.sleep(3)
                    print("Pedras e terra se aglutinam, formando uma figura colossal!\n")
                    time.sleep(3)

                    print("""
╔════════════════════════════════════════════════╗
║            A ROCHA GANHA VIDA!                 ║
║                                                ║
║        UM GOLEM DE TERRA DESPERTA!             ║
╚════════════════════════════════════════════════╝
                    """)
                    time.sleep(5)

                    golem = {
                        "nome": "Golem de Terra Ancestral",
                        "classe": "Guerreiro",
                        "vida": 120,
                        "força": 45,
                        "defesa": 80,
                        "habilidade": "Impacto Sísmico",
                        "nivel": player["nivel"] + 2,
                        "xp": 200
                    }

                    if combate(player, [golem]):
                        mostrar_conquista("quebrador_pedra_3_terra")
                    else:
                        return False
                
                    print("\nO golem se desfaz em pedras, revelando o portal instável por trás dele!")
                    input("\nPressione ENTER para atravessar o portal...")
                    parar_musica()
                    return True
    else:
        print("\nO portal permanece selado. Você precisa encontrar a chave adequada!")
        return False