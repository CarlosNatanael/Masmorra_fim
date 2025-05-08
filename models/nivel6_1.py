from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound_py.sound6_1 import tocar_musica
from game_sound_py.sound6_1 import parar_musica
from utils.personagem import transformar_em_monarca
from utils.combate import combate
from rich import print
import time
import pygame

pygame.init()
pygame.mixer.init()

def nivel_verdade_1(player):
    tocar_musica()
    print("Capítulo 6:  O Cárcere das Almas Perdidas")
    time.sleep(2)
    print("""
O vazio engoliu-me por um momento infinito, até que meu corpo atingiu algo frio e metálico. 
Quando abri os olhos, estava de joelhos em uma plataforma de ferro, flutuando no meio do nada.
    """)
    time.sleep(5)
    player["itens"]["poção de cura"] +=1
    print("'Você encontra uma poção de cura reluzente no corpo dos monstros derrotados!'")
    print("'A poção foi adicionada ao seu inventário'\n")
    print("[bold cyan]Inventario atual:[bold cyan]")
    for item, qtd in player["itens"].items():
        print(f"- {item}: [bold reverse]{qtd}[/bold reverse]")
    time.sleep(5)
    print("""
À minha volta, centenas de celas suspensas pairando no vazio, cada uma fechada por portas de arame farpado e luzes piscando em vermelho. 
De dentro, mãos esqueléticas se agarravam às grades, e vozes roucas sussurravam em uníssono:          
    """)
    time.sleep(5)
    print("(Liberta-nos... ou junte-se a nós.)")
    time.sleep(5)
    print("""
No centro de tudo, uma torre de ossos se erguia, e no topo, uma figura brilhante observava tudo com olhos impassíveis.          
    """)
    time.sleep(5)
    print("\nO Anjo da Obediência.\n")
    time.sleep(5)
    print("""
As celas não estavam presas ao chão—elas se moviam, girando lentamente como um carrossel macabro. 
Algumas tinham prisioneiros que pareciam humanos, outros eram criaturas que mal conseguia descrever. Todos repetiam a mesma coisa:
          
"Não merecemos estar aqui!"
    """)
    time.sleep(5)
    print("Uma placa de ferro enferrujada estava cravada no chão:")
    print("REGRA 1: A DESOBEDIÊNCIA É O ÚNICO PECADO.")
    time.sleep(5)
    from utils.utils import usar_itens
    if not usar_itens(player):
        return False
    print("""
Você avança por plataformas instáveis, saltando entre elas, desviando das Correntes da Conformidade
que tentam arrastá-lo para as celas vazias. Algumas criaturas imploram. Outras apenas olham.  
    """)
    time.sleep(5)
    print("""
Quando finalmente cheguei à torre, o Anjo desceu.

Ele era belo e terrível—asas de luz cortadas por arames farpados, um rosto perfeito sem boca 
e olhos que refletiam infinitas regras escritas em ar puro.

"Você veio pela chave," ele disse, sem mover os lábios. "Mas ela só é dada àqueles que entendem."
    """)
    time.sleep(6)
    anjo = {
        "nome": "Anjo da Obediência",
        "classe": "Anjo",
        "vida": 120,
        "força": 55,
        "defesa": 70,
        "magia": 80,
        "nivel": 10,
        "habilidade": "Julgamento Divino"
    }
    input("\nPrepare-se para enfrentar Anjo da Obediência ! Pressione ENTER...\n")
    if combate(player, [anjo]):
        mostrar_conquista("anjo_perdicao")
    else:
        return False
    
    print("Após uma arda batalha contra o anjo, ele se afasta")

    print(f"""
Você vê uma alavanca cravada no chão metálico da torre. O Anjo se cala, esperando.
Você sente a presença de Eldramar nas sombras, observando.

"Escolha, {player["nome"]}. Você prefere ser o juiz... ou o condenado?"

1. Puxar a alavanca e libertar todos.
2. Destruir a alavanca e manter o cárcere selado.
3. Não fazer nada e assumir o lugar do Anjo.
    """)

    while True:
        escolha_6 = input("Sua decisão final (1-3): ").strip()
    
        if escolha_6 == "1":
            print("\nVocê puxa a alavanca. As celas se abrem. Gritos. Sussurros. Algumas criaturas fogem em silêncio.")
            mostrar_conquista("libertador_correntes")
            time.sleep(5)
            print("Outras atacam. Mas entre elas, olhos humanos choram de gratidão. O Anjo rui...")
            time.sleep(5)
            print("Após isso o Anjo invoca um portal...")
            time.sleep(4)
            print("Você escapa por um portal...\n")
            input("Você avança. Pressione ENTER para continuar...\n")
            parar_musica()
            return "humano"
    
        elif escolha_6 == "2":
            print("\nVocê destrói a alavanca. O Anjo observa em silêncio... e então sorri.")
            mostrar_conquista("carcereiro_eterno")
            time.sleep(5)
            print("Ele lhe entrega a chave mestra. Você pode sair... mas carrega o peso de saber que perpetuou o sofrimento.")
            time.sleep(5)
            print("Sua forma muda. Suas emoções desaparecem lentamente. Você se torna uma nova forma.\n")
            print(f"| » [bold cyan]Status atual[/bold cyan]: [bold black]Monarca das Sombras[/bold black]\n")
            mostrar_conquista("coroa_trevas")
            time.sleep(5)
            print("""
Então o Anjo invade minha mente e deixa a seguinte frase:
              
    A cada nivel você se torna mais parecido com ele....
            """)
            time.sleep(5)
            print("Você escapa por um portal...\n")
            transformar_em_monarca(player)
            input("Você avança. Pressione ENTER para continuar...\n")
            parar_musica()
            return "sombra"  
    
        elif escolha_6 == "3":
            print("\nVocê não se move. O Anjo toca sua testa. Um brilho o envolve.")
            mostrar_conquista("juiz_sombras")
            time.sleep(5)
            print("Sua forma muda. Suas emoções desaparecem lentamente. Você se torna uma nova forma.\n")
            print(f"| » [bold cyan]Status atual[/bold cyan]: [bold black]Monarca das Sombras[/bold black]\n")
            mostrar_conquista("coroa_trevas")
            time.sleep(5)
            print("""
Então o Anjo invade minha mente e deixa a seguinte frase:
              
    A cada nivel você se torna mais parecido com ele....
            """)
            time.sleep(5)
            print("Você escapa por um portal...\n")
            transformar_em_monarca(player)
            input("Você avança. Pressione ENTER para continuar...\n")
            parar_musica()
            return "sombra"
    
        else:
            print("Escolha inválida! Digite 1, 2 ou 3")
            continue