from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound_py.sound6_2 import tocar_musica
from game_sound_py.sound6_2 import parar_musica
from utils.personagem import transformar_em_monarca
from utils.combate import combate
from rich import print
import time
import pygame

pygame.init()
pygame.mixer.init()

def nivel_mentira_2(player):
    tocar_musica()
    print("Capítulo 6:  [bold yellow]A Floresta dos Espectros Famintos[/bold yellow]")
    time.sleep(2)
    print("""
O portal negro me cuspiu em meio a uma floresta que respirava. 
Árvores retorcidas sussurravam meu nome com vozes roucas, seus troncos marcados por rostos humanos congelados em expressões de eterno sofrimento.

O chão sob meus pés era macio e úmido - ao olhar para baixo, vi que pisava em musgo vermelho, encharcado de um líquido que cheirava a ferro velho.

"Bem-vindo ao banquete, nobre tolo."
    """)
    time.sleep(5)
    print(""" 
A voz vinha de todos os lados. Segui adiante, cada passo fazendo com que raízes negras se contorcessem sob meus pés. 
Os rios que cruzavam a floresta não carregavam água, mas sim sangue espesso, onde formas indistintas nadavam sob a superfície.
    """)
    time.sleep(5)
    print("Você descide olhar a sua bolsa de itens.\n")
    from utils.utils import usar_itens
    if not usar_itens(player):
        return False
    time.sleep(5)
    print("""
Você segue em frente. Cada passo provoca o contorcer de raízes negras.
Os rios por onde passa não carregam água, mas sangue... e sombras nadam sob a superfície.

Logo, chega à beira de uma ravina profunda. A única travessia possível: uma ponte feita de ossos humanos.

Quando pisa no primeiro osso, os esqueletos riem:

"Um vivo quer passar!"
"Deixe-o cair como nós!"
"Ofereça algo, vivo... ofeeeeereça..."
    """)
    time.sleep(6)
# Verifica se o jogador tem a chave que evita o sacrifício ou combate
    if "chave de ébano" in player["itens"] and player["itens"]["chave de ébano"] > 0:
        print("""
Ao tocar o primeiro osso da ponte, a chave em seu bolso vibra com intensidade.
Os esqueletos recuam em silêncio, reconhecendo o poder que você carrega.

Sem precisar sacrificar sua lembrança ou lutar, você atravessa a ponte em segurança.
        """)
        time.sleep(5)
    else:
        print("""
Você sente uma memória emergir. Uma lembrança feliz — talvez da infância, de alguém amado, de um lugar seguro.
Ela se transforma numa pérola dourada que brilha em sua mão.

Você pode:

1. Oferecer a lembrança aos mortos.
2. Recusar-se a esquecê-la e tentar saltar.
        """)
    time.sleep(5)
    while True:
        escolha_ponte = input("Sua escolha (1 ou 2): ").strip()
        if escolha_ponte == "1":
            print("\nOs esqueletos engolem a pérola em êxtase. A ponte se estabiliza. Você atravessa.")
            mostrar_conquista("memorias_perdidas")
            time.sleep(5)
            player["vida"] -= 20
            if player["vida"] <= 0:
                return False
            print(f"Reduz 20 pontos de vida! |Vida: {player['vida']}|\n")
            break
        elif escolha_ponte == "2":
            print("\nVocê tenta saltar... mas as raízes o agarram e o obrigam a recuar.")
            print("Sem oferecer algo, você é forçado a enfrentar os esqueletos.\n")
            time.sleep(5)
            inimigos = [
                {"nome": "Esqueleto Guerreiro", "classe": "Guerreiro", "vida": 80, "força": 45, "defesa": 66, "nivel":7},
                {"nome": "Esqueleto Arqueiro", "classe": "Arqueiro", "vida": 70, "força": 47, "defesa": 59, "nivel":7}
            ]
            input("Prepare-se para o combate! Pressione ENTER...\n")
            if combate(player, inimigos):
                mostrar_conquista("danca_ossos")
                player["itens"]["poção de cura"] +=1
                print("'Você encontra uma poção de cura reluzente no corpo dos monstros derrotados!'")
                print("'A poção foi adicionada ao seu inventário'\n")
                print("[bold cyan]Inventario atual:[bold cyan]")
                for item, qtd in player["itens"].items():
                    print(f"- {item}: [bold reverse]{qtd}[/bold reverse]")
                time.sleep(5)
            else:
                return False
            break
        else:
            print("Escolha inválida.")

    print("""
Mais adiante, no coração da floresta havia uma clareira onde a luz não chegava. Lá, em um trono feito de crânios, estava Ele

o Lorde dos Desesperados. Seu corpo mudava constantemente, alternando entre formas humanoides e monstros primitivos.
    """)
    time.sleep(5)
    print("[bold tan]Lorde dos Desesperados[/bold tan]: Ah, o rebelde compassivo... — sua voz é doce, quase sedutora.")
    print("[bold tan]Lorde dos Desesperados[/bold tan]: Você quebra regras para ajudar os outros... mas pode ajudar a si mesmo?\n")
    time.sleep(5)
    print("'Ele estendeu uma mão que se transformava em garras, depois em tentáculos, depois em algo indescritível.'\n")
    time.sleep(5)
    print("[bold tan]Lorde dos Desesperados[/bold tan]: Tome um gole do rio de sangue e ganhe poder para destruir Eldramar. O preço? Apenas um pedaço insignificante de sua alma a cada gole.\n")
    time.sleep(5)
    print("'Você vê o rio de sangue borbulhar atrás dele. Ao redor, árvores com rostos gritam silenciosamente.'")
    print("""
Enquanto decidia, os rostos nas árvores choravam lágrimas de sangue, e no fundo da clareira, via as sombras de outros que haviam feito suas escolhas
alguns agora árvores, outros criaturas ainda piores que o Lorde.
    """)
    time.sleep(5)
    print("""
Você pode:

1. Beber e aceitar o poder sombrio.
2. Recusar e tentar fugir da floresta por conta própria.
3. Fingir que aceita, para tentar enganá-lo.
    """)
    # Encontro com o Lorde dos Desesperados
    while True:
        escolha_final = input("Sua decisão (1, 2 ou 3): ").strip()
        if escolha_final == "1":
            print("""
Você se ajoelha e bebe o sangue.
Um calor cruel o consome, e você sente sua alma se fragmentar... mas seu corpo se fortalece.

O Lorde sorri: "Boa escolha, criatura."

Você sai da floresta mais forte.
            """)
            time.sleep(5)
            print("Sua forma muda. Suas emoções desaparecem lentamente. Você se torna uma nova forma.\n")
            print(f"| » [bold cyan]Status atual[/bold cyan]: [bold black]Monarca das Sombras[/bold black]\n")
            mostrar_conquista("abraco_trevas")
            time.sleep(5)
            print("\nVocê sente um vazio na alma... mas um poder sem limites!\n")
            transformar_em_monarca(player)
            input("Você avança. Pressione ENTER para continuar...\n")
            parar_musica()
            return "sombra"
        elif escolha_final == "2":
            print("""
Você recusa e corre pela floresta.
As árvores tentam prendê-lo, os rios gritam, mas você continua.

Sangrando e esgotado, você encontra uma fenda na escuridão... e encontra algo pior que o Lorde.
            """)
            time.sleep(5)
            print("Você encontra um Wendigo um espírito de canibalismo e fome insaciável")
            time.sleep(5)
            wendigo = {
                "nome": "Wendigo",
                "classe": "Besta",
                "vida": 110,
                "força": 60,
                "defesa": 80,
                "magia": 80,
                "habilidade": "Corte Sangrento",
                "nivel": 9,
                "xp": 100
            }
            input("\nPrepare-se para enfrentar seu pior pesadelo! Pressione ENTER...\n")
            if combate(player, [wendigo]):
                mostrar_conquista("banquete_wendigo")
            else:
                return False
            print("'Sangrando e esgotado, você encontra uma fenda na escuridão... e escapa.'\n")
            input("Você avança. Pressione ENTER para continuar...\n")
            parar_musica()
            return "humano"
        elif escolha_final == "3":
            print("""
Você finge aceitar. Toca o líquido... mas não bebe.
No último segundo, você ataca o Lorde com sua arma.

Ele ri, ferido, mas não morto.

"Esperto... veremos até quando consegue resistir."
            """)
            time.sleep(5)
            lorde = {
                "nome": "Lorde dos Desesperados",
                "classe": "Besta",
                "vida": 120,
                "força": 57,
                "defesa": 70,
                "magia": 80,
                "habilidade": "Lama venenosa",
                "nivel": 9,
                "xp": 100
            }
            input("\nPrepare-se para enfrentar O Lorde dos Desesperados! Pressione ENTER...\n")
            if combate(player, [lorde]):
                mostrar_conquista("fim_lorde")
            else:
                return False
            print("Sangrando e esgotado, você encontra uma fenda na escuridão... Você escapa... mas agora está marcado.\n")
            input("Você avança. Pressione ENTER para continuar...\n")
            parar_musica()
            return "humano"
        else:
            print("Escolha inválida.")