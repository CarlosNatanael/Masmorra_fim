from utils.utils import limpar_terminal
from utils.combate import combate
import time

def nivel_cinco(player):
    print("Capítulo 5: A Sala do Guardião\n")
    time.sleep(5)
    print(""" 
O portal se fecha atrás de você com um estrondo que ecoa como um trovão agonizante.
O ar está carregado com o cheiro de ossos calcinados e magia antiga. À sua frente,
ergue-se um templo circular onde as leis da realidade parecem dobrar-se sob uma vontade perversa.
    """)
    time.sleep(5)
    
    print("Chamas azuis dançam no ar, congeladas no tempo,\n"
          "iluminando grotescamente o trono central - uma monstruosidade\n"
          "construída com ossos de criaturas que você sequer consegue nomear.")
    time.sleep(5)
    print(""" 
E então você o vê. Velthurion. 

O velho misterioso que você encontrou no início agora se revela em sua verdadeira forma:
Um colosso de três metros de altura, com pele tão pálida que parece translúcida,
vestes negras que se fundem com as sombras ao seu redor. Quando ele abre os olhos,
você vê apenas um abismo - dois poços sem fundo que sugam sua coragem.
    """)
    input("Pressione ENTER para continuar")
    time.sleep(5)
    
    print(f'\nVelthurion : Ah... {player["nome"]}." Sua voz ecoa dentro do seu crânio.\n'
          'Velthurion : Ou devo chamá-lo de... intruso? Sobrevivente? Ou talvez...\n'
          'Velthurion : Apenas mais um tolo que acredita ser especial?"\n')
    time.sleep(5)
    print('Velthurion ergue uma mão esquelética e sussurra: "Mostre-me do que é capaz."\n'
          'O chão se abre e uma figura emerge das profundezas - uma massa de pura escuridão\n'
          'que toma a forma de um guerreiro ancestral, seus olhos queimando com fogo negro.\n')
    time.sleep(5)

    monstro = {
        "nome": "Servo das Sombras",
        "classe": "Guerreiro",
        "vida": 80,
        "força": 36,
        "defesa": 50,
        "habilidade": "Lâmina do Abismo",
        "nivel": 5,
    }

    print("Velthurion riu e o mundo se despedaçou!")
    time.sleep(4)
    input("\nPrepare-se para o combate! Pressione ENTER...\n")
    if not combate(player, [monstro]):
        return False
    
    print('\nVelthurion : Bom... muito bom. Velthurion se levanta do trono, seu manto de sombras se arrastando.\n'
          '"Mas isso foi apenas um aquecimento.\n')
    time.sleep(5)
    print('Velthurion ri enquanto seu corpo começa a se dividir.\n'
          'Velthurion : Você realmente acredita que pode desafiar\n'
          'Velthurion : Aquele que teceu os fios do seu destino desde o início?"')
    time.sleep(5)

    cloneEld = {
        "nome": "Velthurion",
        "classe": "Mago Supremo",
        "vida": 100,
        "força": 45,
        "magia": 100,
        "defesa": 70,
        "habilidade": "Bola sombria",
        "nivel": 8,
        "xp": 200
    }
    input("\nPrepare-se para enfrentar seu pior pesadelo! Pressione ENTER...\n")
    if not combate(player, [cloneEld]):
        return False
    
    print("Sangrando e exausto, você se arrasta até o centro do salão e descide parar.")
    from utils.utils import usar_itens
    if not usar_itens(player):
        return False
    print("\nVelthurion está sentado em seu trono, examinando você com curiosidade mórbida.\n")
    time.sleep(4)
    print(f"""
Velthurion : Conte-me, {player["nome"]}... como foi derrotar parte de mim mesmo?
          
Ele inclina a cabeça. "Não responda. Sei que você ainda não compreende

Velthurion : a verdadeira natureza deste lugar... mas terá sua chance.
    """)
    time.sleep(5)
    print("Com um gesto, um pergaminho antigo materializa-se no ar diante de você,\n"
          "pairando envolto em chamas negras. Ele desenrola-se lentamente,\n"
          "revelando uma pergunta que queima seus olhos:")
    time.sleep(4)
    print("""
O pergaminho mostrava:
O QUE VOCÊ MAIS TEME?
          
O pergaminho queima com energia arcana, aguardando sua resposta...
    """)
    time.sleep(5)
    print("\n1. Revelar seu verdadeiro medo (Coragem)")
    print("2. Inventar uma mentira (Astúcia)")
    print("3. Destruir o pergaminho (Determinação)")
    
    escolha = None
    while escolha not in ["1", "2", "3"]:
        escolha = input("Sua decisão (1-3): ").strip()
        if escolha not in ["1", "2", "3"]:
            print("Escolha inválida! Digite 1, 2 ou 3")

    # Processa a primeira escolha
    if escolha == "1":
        player["medo"] = input("\nDigite seu verdadeiro medo: ").strip()
        print(f"\nVelthurion sorri 'Ah... {player['medo']}. Interessante.'")
        time.sleep(3)
        print("\nVelthurion: Então você não aprendeu nada. (A masmorra começa a desmoronar!)\n")
        time.sleep(3)
        print("Velthurion invoca um Minotauro para combate\n")

        minotauro = {
            "nome": "Minotauro das Sombras",
            "classe": "Guerreiro",
            "vida": 100,
            "força": 39,
            "magia": 30,
            "defesa": 80,
            "habilidade": "Corrida da morte",
            "nivel": 7
        }
        input("Prepare-se para o combate! Pressione ENTER...\n")
        if not combate(player, [minotauro]):
            return False
    
    elif escolha == "2":
        print("\nVelthurion: Eu já sabia. Ele lança um feitiço que reduz sua vida em 20!")
        print(f"- 20 de Vida |Vida: {player['vida']}|")
        time.sleep(3)
        player["vida"] -= 20
        if player["vida"] <= 0:
            return False
    
    elif escolha == "3":
        print("\nA sala treme... algo pior que Velthurion desperta!")
        time.sleep(4)
        print("Um dragão das sombras surge do manto de Velthurion.\n")

        dragao = {
            "nome": "Dragão das Sombras",
            "classe": "Besta",
            "vida": 100,
            "força": 50,
            "magia": 30,
            "defesa": 80,
            "habilidade": "Corrida da morte",
            "nivel": 7
        }
        input("Prepare-se para o combate! Pressione ENTER...\n")
        if not combate(player, [dragao]):
            return False
        
    input("\nPressione ENTER para continuar")
    limpar_terminal()
    print("""
 O salão tremeu quando Velthurion ergueu a mão, interrompendo o combate. 
 Suas sombras recuaram, e o ar ficou pesado, como antes de uma tempestade.
    """)
    time.sleep(5)
    print("\nVelthurion : Você sobreviveu até aqui... mas agora vem o verdadeiro teste.")
    time.sleep(5)
    print("\n(Ele estalou os dedos.)")
    print("(E de repente, eu não estava mais na masmorra.)\n")
    time.sleep(5)
    print(""" 
Estava de volta àquela mesma cena do início—a rua empoeirada, a criança faminta, a maçã roubada. 
O mercador gritava, a criança tremia, e eu estava parado no meio, exatamente como antes.
    """)
    time.sleep(4)
    print("\n(Só que agora, Velthurion estava lá também, observando como um juiz silencioso.)")

    print("\n(A cena reiniciou.)")
    print("(A criança agarrou a maçã. O mercador rugiu.)\n")
    time.sleep(5)
    print("Velthurion sussurra em seu ouvido:")
    time.sleep(5)
    print("\nAgora, escolha com sabedoria. Esta decisão moldará seu destino.")
    time.sleep(5)
    print("\n1. Impor a justiça (Lei acima de tudo)")
    print("2. Proteger o fraco (Compaixão acima das regras)")
    print("3. Pagar o preço (Equilíbrio)")
    
    escolha_final = None
    while escolha_final not in ["1", "2", "3"]:
        escolha_final = input("\nSua decisão final (1-3): ").strip()
        if escolha_final not in ["1", "2", "3"]:
            print("Escolha inválida!")

    return escolha_final 