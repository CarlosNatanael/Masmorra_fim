import time
from utils.utils import limpar_terminal
from utils.combate import combate



def nivel_cinco(player):
    print("Nível 5: A Sala do Guardião\n")
    time.sleep(5)
    print(""" 
O portal se fecha atrás de você com um estrondo que ecoa como um trovão agonizante.
O ar está carregado com o cheiro de ossos calcinados e magia antiga. À sua frente,
ergue-se um templo circular onde as leis da realidade parecem dobrar-se sob uma vontade perversa.
    """)
    time.sleep(5)
    
    print("Chamas azuis dançam no ar, congeladas no tempo,\n"
          "iluminando grotescamente o trono central - uma monstruosidade\n"
          "construída com ossos de criaturas que você sequer consegue nomear.\n")
    time.sleep(5)
    
    print(""" 
E então você o vê. Eldramar. 

O velho misterioso que você encontrou no início agora se revela em sua verdadeira forma:
Um colosso de três metros de altura, com pele tão pálida que parece translúcida,
vestes negras que se fundem com as sombras ao seu redor. Quando ele abre os olhos,
você vê apenas um abismo - dois poços sem fundo que sugam sua coragem.
    """)
    time.sleep(6)
    
    print(f'\n"Ah... {player["nome"]}." Sua voz ecoa dentro do seu crânio.\n'
          '"Ou devo chamá-lo de... intruso? Sobrevivente? Ou talvez...\n'
          'apenas mais um tolo que acredita ser especial?"\n')
    time.sleep(5)
    print('Eldramar ergue uma mão esquelética e sussurra: "Mostre-me do que é capaz."\n'
          'O chão se abre e uma figura emerge das profundezas - uma massa de pura escuridão\n'
          'que toma a forma de um guerreiro ancestral, seus olhos queimando com fogo negro.\n')
    time.sleep(5)
    monstro = {
        "nome": "Servo das Sombras",
        "classe": "Guerreiro",
        "vida": 80,
        "força": 45,
        "defesa": 50,
        "habilidade": "Lâmina do Abismo",
        "nivel": 5,
    }

    print("Eldramar riu e o mundo se despedaçou!\n")
    time.sleep(4)
    input("\nPrepare-se para o combate! Pressione ENTER...\n")
    if not combate(player, [monstro]):
        return False
    
    print('\n"Bom... muito bom." Eldramar se levanta do trono, seu manto de sombras se arrastando.\n'
          '"Mas isso foi apenas um aquecimento.\n')
    time.sleep(5)
    print('Eldramar ri enquanto seu corpo começa a se dividir.\n'
          'Você realmente acredita que pode desafiar\n'
          'aquele que teceu os fios do seu destino desde o início?"\n')
    time.sleep(5)

    cloneEld = {
        "nome": "Eldramar",
        "classe": "Mago Supremo",
        "vida": 100,
        "força": 55,
        "magia": 100,
        "defesa": 70,
        "habilidade": "Bola sombria",
        "nivel": 8,
        "xp": 200

    }
    input("\nPrepare-se para enfrentar seu pior pesadelo! Pressione ENTER...\n")
    if not combate(player, [cloneEld]):
        return False
    
    print("Sangrando e exausto, você se arrasta até o centro do salão.\n"
          "Eldramar está sentado em seu trono, examinando você com curiosidade mórbida.\n")
    time.sleep(4)
    
    print(f'\n"Conte-me, {player["nome"]}... como foi derrotar parte de mim mesmo?"\n'
          'Ele inclina a cabeça. "Não responda. Sei que você ainda não compreende\n'
          'a verdadeira natureza deste lugar... mas terá sua chance."\n')
    time.sleep(5)
    
    print("Com um gesto, um pergaminho antigo materializa-se no ar diante de você,\n"
          "pairando envolto em chamas negras. Ele desenrola-se lentamente,\n"
          "revelando uma pergunta que queima seus olhos:\n")
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
    
    escolha = input("Sua decisão (1-3): ").strip()
    while True:
        if escolha == "1":
            player["medo"] = input("Digite seu verdadeiro medo: ").strip()
            print(f"\nEldramar : sorri 'Ah... {player['medo']}. Interessante.'")
            time.sleep(3)
            print("Eldramar: Então você não aprendeu nada. (A masmorra começa a desmoronar!)")
            time.sleep(3)
            print("Eldramar invoca um Minotauro para combate\n")

            minotauro = {
                "nome": "Minotauro das Sombras",
                "classe": "Guerreiro",
                "vida": 100,
                "força": 65,
                "magia": 30,
                "defesa": 80,
                "habilidade": "Corrida da morte",
                "nivel": 7
            }
            input("Prepare-se para o combate! Pressione ENTER...\n")
            if not combate(player, [minotauro]):
                return False
        
        elif escolha == "2":
            print("\nEldramar : Eu já sabia. Ele lança um feitiço que reduz sua vida em 20!")
            time.sleep(3)
            player["vida"] -= 20
            if player["vida"] <= 0:
                return False
            return "feitico"
        elif escolha == "3":
            print("\nA sala treme... algo pior que Eldramar desperta!")
            time.sleep(4)
            print("Um dragão das sombras surge do manto de eldramar.")

            dragao = {
                "nome": "Dragão ",
                "classe": "Guerreiro",
                "vida": 100,
                "força": 65,
                "magia": 30,
                "defesa": 80,
                "habilidade": "Corrida da morte",
                "nivel": 7
            }
            input("Prepare-se para o combate! Pressione ENTER...\n")
            if not combate(player, [dragao]):
                return False
        else:
            print("Escolha inválida! Digite 1, 2 ou 3")
            return False
        
    
def fase_final(playe, caminho)    :
    limpar_terminal()
    print("""
O salão tremeu quando Eldramar ergueu a mão, interrompendo o combate. 
Suas sombras recuaram, e o ar ficou pesado, como antes de uma tempestade.
        """)
    time.sleep(5)
    print("\nEldramar : Você sobreviveu até aqui... mas agora vem o verdadeiro teste.")
    print("(Ele estalou os dedos.)")
    print("(E de repente, eu não estava mais na masmorra.)")
    print(""" 
Estava de volta àquela mesma cena do início—a rua empoeirada, a criança faminta, a maçã roubada. 
O mercador gritava, a criança tremia, e eu estava parado no meio, exatamente como antes.
        """)
    time.sleep(4)
    print("\n(Só que agora, Eldramar estava lá também, observando como um juiz silencioso.)\n")

    print("\n(A cena reiniciou.)")
    print("(A criança agarrou a maçã. O mercador rugiu.)\n")
    time.sleep(5)
    print("Eldramar sussurra em seu ouvido:")
    print("\"Agora, escolha com sabedoria. Esta decisão moldará seu destino.\"")
    
    print("\n1. Impor a justiça (Lei acima de tudo)")
    print("2. Proteger o fraco (Compaixão acima das regras)")
    print("3. Pagar o preço (Equilíbrio)")
    
    while True:
        escolha_final = input("\nSua decisão final (1-3): ").strip()
        
        if escolha_final in ["1", "2", "3"]:
                # Retorna o caminho escolhido para o nível 6 específico
            return f"{caminho}_{escolha_final}" 
        print("Escolha inválida!")

