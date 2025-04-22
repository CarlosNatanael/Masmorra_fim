from utils.combate import combate
import time

def nivel_mentira_2(player):
    print("Capítulo 6:  A Floresta dos Espectros Famintos")
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
    print("""
Você sente uma memória emergir. Uma lembrança feliz — talvez da infância, de alguém amado, de um lugar seguro.
Ela se transforma numa pérola dourada que brilha em sua mão.

Você pode:

1. Oferecer a lembrança aos mortos.
2. Recusar-se a esquecê-la e tentar saltar.
    """)
    # time.sleep(5)
    while True:
        escolha_ponte = input("Sua escolha (1 ou 2): ").strip()
        if escolha_ponte == "1":
            print("\nOs esqueletos engolem a pérola em êxtase. A ponte se estabiliza. Você atravessa.")
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
                {"nome": "Esqueleto Guerreiro", "classe": "Guerreiro", "vida": 70, "força": 55, "defesa": 60, "nivel":7},
                {"nome": "Esqueleto Arqueiro", "classe": "Arqueiro", "vida": 40, "força": 75, "defesa": 40, "nivel":7}
            ]
            input("Prepare-se para o combate! Pressione ENTER...\n")
            if not combate(player, inimigos):
                return False
            break
        else:
            print("Escolha inválida.")

    print("""
Mais adiante, no coração da floresta havia uma clareira onde a luz não chegava. Lá, em um trono feito de crânios, estava Ele

o Lorde dos Desesperados. Seu corpo mudava constantemente, alternando entre formas humanoides e monstros primitivos.
    """)
    time.sleep(5)
    print("Lorde dos Desesperados: Ah, o rebelde compassivo... — sua voz é doce, quase sedutora.")
    print("Lorde dos Desesperados: Você quebra regras para ajudar os outros... mas pode ajudar a si mesmo?\n")
    time.sleep(5)
    print("Ele estendeu uma mão que se transformava em garras, depois em tentáculos, depois em algo indescritível.\n")
    time.sleep(5)
    print("Lorde dos Desesperados: Tome um gole do rio de sangue e ganhe poder para destruir Velthurion. O preço? Apenas um pedaço insignificante de sua alma a cada gole.\n")
    time.sleep(5)
    print("Você vê o rio de sangue borbulhar atrás dele. Ao redor, árvores com rostos gritam silenciosamente.")
    print(""""
Enquanto decidia, os rostos nas árvores choravam lágrimas de sangue, e no fundo da clareira, via as sombras de outros que haviam feito suas escolhas
alguns agora árvores, outros criaturas ainda piores que o Lorde.
    """)
    time.sleep(5)
    print(""""
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

Você sai da floresta mais forte, mas menos humano.
            """)
            time.sleep(5)
            player["força"] += 30
            player["vida"] += 10
            print(f"| » Status atual: Monarca das Sombra ({player['classe']})")
            print(f"Nome: {player["nome"]} |Força: {player["força"]} |Vida: {player["vida"]}\n")
            time.sleep(5)
            print("\nVocê sente um vazio na alma... mas um poder sem limites!")
            break
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
                "força": 70,
                "defesa": 80,
                "magia": 80,
                "habilidade": "Corte Sangrento",
                "nivel": 9,
                "xp": 100
            }
            input("\nPrepare-se para enfrentar seu pior pesadelo! Pressione ENTER...\n")
            if not combate(player, [wendigo]):
                return False
            print("Sangrando e esgotado, você encontra uma fenda na escuridão... e escapa.")
            break
        elif escolha_final == "3":
            print("""
Você finge aceitar. Toca o líquido... mas não bebe.
No último segundo, você ataca o Lorde com sua arma.

Ele ri, ferido, mas não morto.

"Esperto... veremos até quando consegue resistir."
            """)
            lorde = {
                "nome": "Lorde dos Desesperados",
                "classe": "Besta",
                "vida": 150,
                "força": 70,
                "defesa": 50,
                "magia": 80,
                "habilidade": "Lama venenosa",
                "nivel": 9,
                "xp": 100
            }
            input("\nPrepare-se para enfrentar O Lorde dos Desesperados! Pressione ENTER...\n")
            if not combate(player, [lorde]):
                return False
            print("Sangrando e esgotado, você encontra uma fenda na escuridão... Você escapa... mas agora está marcado.\n")
            break
        else:
            print("Escolha inválida.")

    input("Você avança. Pressione ENTER para continuar...\n")
    return True