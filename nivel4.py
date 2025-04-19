import time
from utils.combate import combate
import random

def nivel_quatro(player):
    print("Capítulo 4: O Pântano do Desespero\n")
    time.sleep(5)
    print("O corpo do mago dissolveu-se em tinta escura, seus gritos afogando-se em um redemoinho de páginas rasgadas.")
    print("O livro que ele guardava caiu no chão com um thud solene, e eu o peguei antes que as sombras o engolissem.\n")
    print("(Isso deve ser a chave...)\n")
    time.sleep(5)
    print("Mas antes que eu pudesse abri-lo, o chão da biblioteca começou a afundar.\n")
    print("Madeira rachou, estantes desmoronaram, e de repente—")
    print("—PLOFT—")
    print("Eu estava até o pescoço em água podre.")
    print("A biblioteca tinha desaparecido. Agora, tudo ao meu redor era lama, névoa e silêncio sufocante.")
    print("""
    O ar cheirava a folhas apodrecidas e carne em decomposição. Árvores esqueléticas se contorciam como dedos ossudos, e a água estagnada borbulhava com coisas se movendo sob a superfície.
    """)
    print("\n(Pisei em algo macio.)")
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
            {"nome": "Lizard", "classe": "Guerreiro", "vida": 50, "força": 45, "magia": 20, "defesa": 30, "nivel": 4},
            {"nome": "Golem do pântano", "classe": "Guerreiro", "vida": 80, "força": 36, "magia": 30, "defesa": 60, "nivel": 5}
        ]

        input("Prepare-se para o combate! Pressione ENTER...\n")
        if not combate(player, monstros):
            return False
        print("\nVocê derrota as criaturas e continua, coberto de lama e suor...\n")
    else:
        print("\nVocê avança cuidadosamente e encontra uma trilha firme. Parece o caminho certo!\n")
        time.sleep(3)

    print("Ao longe, um brilho vermelho corta a névoa... uma criatura gigante se aproxima!")
    print("Ela é feita de galhos, ossos e lodo... olhos como carvões em brasa.\n")
    print("Chefe do Pântano: Grumor, o Devorador de Errantes.\n")

    chefe = {
        "nome": "Grumor, o Devorador de Errantes",
        "classe": "Besta",
        "vida": 120,
        "força": 50,
        "magia": 40,
        "defesa": 50,
        "habilidade": "Sufocamento de Lama",
        "nivel": player["nivel"] + 3,
    }

    input("Prepare-se para o confronto final do nível! Pressione ENTER...\n")
    if not combate(player, [chefe]):
        return False

    print("\nGrumor desfaz-se em lama fétida e galhos partidos.")
    print("No meio da poça, surge uma flor brilhante. Um símbolo mágico emana dela — um selo que protege o próximo portal.\n")
    time.sleep(5)

    input("Você colhe a flor e segue adiante... Pressione ENTER para continuar.\n")
    return True