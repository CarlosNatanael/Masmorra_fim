from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound_py.sound3 import tocar_musica
from game_sound_py.sound3 import parar_musica
from utils.combate import combate
from rich import print
from rich import print as rprint
from rich.panel import Panel
import time
import pygame

pygame.init()
pygame.mixer.init()

def nivel_tres(player):
    tocar_musica()
    rprint(Panel.fit("[bold yellow]Capítulo 3: A Biblioteca Perdida[/]", style="blue"))
    time.sleep(5)
    print('"O último fragmento do meu reflexo se dissolveu no ar, e a porta no final do corredor se abriu com um rangido sinistro."')
    print("O ar que vinha de lá era diferente—pesado, cheio do mofo de páginas antigas e do ferro frio de tinta seca.\n")
    time.sleep(5)
    print('"Uma biblioteca?"\n')
    print('"Entrei em um vasto salão abobadado, tão grande que mal conseguia ver o fim. Prateleiras de madeira negra subiam até o teto"')
    print("repletas de livros encadernados em couro, pergaminhos amarrados com cordas de seda e tomos presos por correntes enferrujadas.\n")
    print("Era lindo.\nEra assustador.\n")
    time.sleep(5)
    from utils.utils import usar_itens
    if not usar_itens(player):
        return False
    time.sleep(5)
    print("\nVocê decide continuar e observa que algumas das prateleiras se moviam sozinhas, deslizando como sombras, reorganizando-se em padrões")
    print('\n"— Bem-vindo, intruso."')
    time.sleep(5)
    print('"A voz veio de todos os lados."')
    print('\n"Não estava sozinho."\n')
    print("Pequenas criaturas—goblins—com olhos amarelos e dentes afiados, espreitavam por entre as estantes.")
    print("Alguns carregavam lanças feitas de ossos, outros folheavam livros com dedos garrudos, como se procurassem algo.")
    time.sleep(5)
    print('\n"Humano... humano cheira a medo," rosnou um deles, lambendo os lábios.\n')
    print("Ele me atacou!\n")
    time.sleep(5)

    goblins = [
        {"nome": "Goblin Aprendiz", "classe": "Mago", "vida": 45, "força": 45, "magia": 45, "defesa": 25, "nivel": 3}
    ]

    input("Prepare-se para o combate! Pressione ENTER...\n")
    if combate(player, goblins):
        mostrar_conquista("exterminador_goblin_2")
    else:
        return False

    print("\nOs goblins eram rápidos, mas burros. Um por um, caíram—guinchando, até que o último fugiu para as sombras.")
    time.sleep(5)
    print("\nMas então, ouvi palmas.")
    print("Lentas. Deliberadas.\n")
    print("[bold black]???[/bold black]: Impressionante. Mas livros não são armas, garoto. São portais..\n")
    time.sleep(5)
    print("No topo de uma escada em espiral, um vulto observava.")
    print('"Seus trajes eram feitos de páginas—folhas de pergaminho costuradas como uma armadura, com runas que brilhavam em vermelho-sangue."')
    print("\nSeu rosto estava escondido sob um capuz, mas seus olhos...")
    print("Eles não eram humanos.\n")
    time.sleep(5)
    print("[bold black]???[/bold black]: Você ousa perturbar o silêncio Eterno da Biblioteca Perdida?\n")
    print("[bold black]???[/bold black]: Eu sou Velkar, o Guardião do Conhecimento Proibido.\n")
    time.sleep(5)
    print("[bold blue]Valker[/bold blue]: Antes brinque um pouco com o meu golem...")
    time.sleep(5)

    golem = {
        "nome": "Golem de elbano", 
        "classe": "Guerreiro", 
        "vida": 100, 
        "força": 26,
        "magia": 45, 
        "defesa": 60, 
        "nivel": player["nivel"] + 1,
    }

    input("\nPrepare-se para o combate! Pressione ENTER...\n")
    if combate(player, [golem]):
        mostrar_conquista("cacador_golem_1")
    else:
        return False

    print("[bold blue]Valker[/bold blue]: Você quer a chave para sair da masmorra, não é? Ele ergueu a mão, e um livro flutuou até ele.")
    print("[bold blue]Valker[/bold blue]: Está aqui. Mas primeiro... vamos ver se você é digno de ler.\n")
    time.sleep(4)

    mago = {
        "nome": "Velkar, o Guardião",
        "classe": "Mago",
        "vida": 95,
        "força": 50,
        "magia": 50,
        "defesa": 50,
        "habilidade": "Explosão Arcana",
        "nivel": player["nivel"] + 2,
    }

    input("Prepare-se para a batalha final deste nível. Pressione ENTER para continuar...\n")
    if combate(player, [mago]):
        mostrar_conquista("velho_guardiao")
    else:
        return False

    print('\n"Velkar caiu de joelhos, seus olhos perdendo o brilho púrpura."')
    print('"Com seu último suspiro, ele murmurou: O saber... deve ser temido..."\n')
    print("O corpo do mago dissolveu-se em tinta escura, seus gritos afogando-se em um redemoinho de páginas rasgadas.")
    time.sleep(5)
    print("Ao seu lado, um livro dourado flutuava até minhas mãos. Um tomo sagrado. Talvez... a chave para entender essa masmorra.\n")
    time.sleep(5)
    print("Um item caiu no chão ,e eu o peguei antes que as sombras o engolissem.")
    print("(Isso deve ser a chave...)\n")
    player["itens"]["chave de ébano"] = 1
    print("Você encontra uma [bright_yellow]Chave de Élbano[/bright_yellow] reluzente no corpo do mago derrotado!")
    print("(A chave foi adicionada ao seu inventário)\n")
    from utils.utils import ver_itens
    ver_itens(player)
    time.sleep(5)
    print("\nChão da biblioteca começou a afundar.\n")
    print("Madeira rachou, estantes desmoronaram, e de repente—")
    time.sleep(5)
    print("—PLOFT—\n")
    time.sleep(5)
    print("Eu estava até o pescoço em água podre.")
    time.sleep(5)
    print("A biblioteca tinha desaparecido. Agora, tudo ao meu redor era lama, névoa e silêncio sufocante.")

    input("\nVocê avança. Pressione ENTER para continuar...\n")
    parar_musica()
    return True