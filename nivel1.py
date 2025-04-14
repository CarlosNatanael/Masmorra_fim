import random
import time
from PIL import Image  # type: ignore

# Caminho da imagem que será exibida na introdução
caminho_imagem = r"C:\Users\SUPORTE 03\Desktop\EU\Eu (Carlos)\Cod_Python\MASMORRA DO FIM\Default_A_serene_and_mystical_illustration_of_the_Mundo_de_Aud_2.jpg"

try:
    # Tenta abrir a imagem e exibir
    imagem = Image.open(caminho_imagem)
except FileNotFoundError:
    print(f"Erro: O arquivo no caminho '{caminho_imagem}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao abrir a imagem: {e}")

def introducao():
    # Exibe a introdução do jogo com pausas para efeito dramático
    print("\n--- Masmorra do Fim ---")
    time.sleep(2)
    print("\nVocê é um jovem estudante universitário, levando uma vida normal no nosso mundo.")
    time.sleep(3)
    print("Em um dia como qualquer outro, algo estranho acontece. Um livro misterioso cai de uma prateleira da biblioteca...")
    time.sleep(4)
    print("Seus olhos encontram suas páginas, e uma força invisível te arrasta para dentro de suas histórias")
    time.sleep(4)
    print("\n--- Transição para o Mundo de Audurian ---")
    time.sleep(2)
    imagem.show()
    print("\nAo acordar, você se vê em um local desconhecido, repleto de sombras e ruínas.")
    time.sleep(3)
    print("\nEsse é o mundo de Audurian, um lugar onde magia e monstros existem.")
    time.sleep(3)
    print("A voz de um guardião antigo ecoa na sua mente...")
    time.sleep(2)
    print("\nGuardião: 'Bem-vindo à Masmorra do Fim, viajante de outro mundo.")
    time.sleep(2)
    print("Arcturus: Meu nome é Arcturus Thorne. E qual é o seu jovem misterioso ?")
    time.sleep(3)
    name = input("Digite o seu nome: ")
    print(f"Arcturus: Ah então seu nome é {name}")
    time.sleep(2)
    print("\nVocê repara no Mago, e percebe que ele tem uma presença imponente, com uma longa barba prateada e olhos que parecem ver além do presente.")
    print("Sua voz é suave, mas ressoa com autoridade.")
    time.sleep(4)
    print("\nArcturus olha para você decima para baixo com um olhar de dúvida")
    time.sleep(4)
    print(f"Arcturus: O que trás você a essa Masmorra jovem {name} ?")
    print(f"{name}: ....")
    time.sleep(3)

def escolher_res():
    # Pergunta o motivo do jogador para entrar na masmorra
    print("\n--- Sua Jornada Começa Agora ---")
    time.sleep(2)
    print("\nEscolha uma resposta:")
    print("1. Voltar para casa")
    print("2. Fama, riqueza e mulheres")
    print("3. Ser Rei da Masmorra")

    escolha1 = input("\nDigite o número da sua resposta: ")
    if escolha1 == "1":
        print("\nArcturus: Para retornar ao seu lar, você deve vencer os desafios da masmorra e enfrentar o guardião que detém o segredo.")
        print("Arcturus: Siga em frente e descubra os misterios dessa masmorra !!")
        print("Após Arcturus sumir inesperadamente você segue em frente na masmorra")
        time.sleep(4)
    elif escolha1 == "2":
        print("\nArcturus: Já que você busca Fama e riqueza, você deve vencer os desafios da masmorra e enfrentar o guardião que detém o segredo.")
        print("Arcturus: Siga em frente e descubra os misterios dessa masmorra !!")
        print("Após Arcturus sumir inesperadamente você segue em frente na masmorra")
        time.sleep(4)
    elif escolha1 == "3":
        print("\nArcturus: Vejo que busca algo que nem mesmo eu imaginaria, você deve vencer os desafios da masmorra e enfrentar o guardião que detém o segredo.")
        print("Arcturus: Siga em frente e descubra os misterios dessa masmorra !!")
        print("Após Arcturus sumir inesperadamente você segue em frente na masmorra")
        time.sleep(4)
    else:
        print("Escolha inválida, por favor, escolha novamente.")
        return escolher_res()

def escolher_classe():
    # Pergunta o nome do personagem e qual classe ele deseja escolher
    nome = input("Digite o nome do seu personagem: ")

    print("\nEscolha uma classe para o seu personagem:")
    print("1. Mago")
    print("2. Paladino")
    print("3. Arqueiro")
    print("4. Guerreiro")

    escolha = input("Digite o número da classe escolhida: ")

    if escolha == "1":
        return {
            "nome": nome,
            "classe": "Mago",
            "vida": random.randint(50, 60),
            "força": random.randint(10, 20),
            "magia": random.randint(70, 90),
            "defesa": random.randint(20, 30),
            "habilidade": "Bola de Fogo",
            "itens": {"poção de cura": 3}
        }
    elif escolha == "2":
        return {
            "nome": nome,
            "classe": "Paladino",
            "vida": random.randint(80, 110),
            "força": random.randint(50, 70),
            "magia": random.randint(30, 50),
            "defesa": random.randint(60, 80),
            "habilidade": "Benção divina",
            "itens": {"poção de cura": 2}
        }
    elif escolha == "3":
        return {
            "nome": nome,
            "classe": "Arqueiro",
            "vida": random.randint(60, 70),
            "força": random.randint(20, 30),
            "magia": random.randint(20, 30),
            "defesa": random.randint(30, 40),
            "habilidade": "Tiro Certeiro",
            "itens": {"poção de cura": 3}
        }
    elif escolha == "4":
        return {
            "nome": nome,
            "classe": "Guerreiro",
            "vida": random.randint(70, 90),
            "força": random.randint(70, 80),
            "magia": random.randint(20, 30),
            "defesa": random.randint(40, 60),
            "habilidade": "Decapitação",
            "itens": {"poção de cura": 1}
        }
    else:
        print("Escolha inválida, por favor, escolha novamente.")
        return escolher_classe()

# Define a lista de inimigos Goblins para o combate
goblins = [
    {"nome": "Goblin nv:1", "vida": random.randint(20, 30), "força": random.randint(10, 15)},
    {"nome": "Goblin nv:2", "vida": random.randint(30, 40), "força": random.randint(15, 20)},
]

def combate(player, inimigos):
    # Realiza o combate entre o jogador e os goblins
    print("Após errar a resposta abre uma segunda porta que estava escondida e saem dois goblins !")
    time.sleep(4)
    print("\nVocê está em combate com os goblins!")
    while inimigos and player["vida"] > 0:
        print(f"\n{player['nome']} (Classe: {player['classe']}): Vida = {player['vida']}")
        for i, inimigo in enumerate(inimigos):
            print(f"{i + 1}. {inimigo['nome']} - Vida = {inimigo['vida']}")

        print("Escolha sua ação:")
        print("1. Atacar")
        print("2. Usar item")
        print("3. Usar habilidade especial")

        acao = input("Digite o número da ação escolhida: ")

        if acao == "1":
            # Escolhe qual inimigo atacar
            escolha = int(input("Escolha o inimigo para atacar (número): ")) - 1
            inimigo = inimigos[escolha]
            dano = max(0, player["força"] - random.randint(0, 3))
            inimigo["vida"] -= dano
            print(f"Você atacou {inimigo['nome']} e causou {dano} de dano")

            if inimigo["vida"] <= 0:
                print(f"{inimigo['nome']} foi derrotado!")
                inimigos.pop(escolha)
        elif acao == "2":
            # Usa uma poção de cura
            item = input("Escolha o item para usar: poção de cura\n").strip().lower()
            if item == "poção de cura" and player["itens"]["poção de cura"] > 0:
                player["vida"] += 20
                player["itens"]["poção de cura"] -= 1
                print("Você usou a poção de cura e recuperou 20 de vida.")
            else:
                print("Você não possui esse item ou está sem itens.")
        
        elif acao == "3":
            # Usa a habilidade especial
            habilidade_especial(player, inimigos)

        else:
            print("Ação inválida. Tente novamente.")
            continue

        # Ataque dos Goblins
        if inimigos:
            goblin = random.choice(inimigos)
            dano_goblin = max(0, goblin["força"] - player["defesa"])
            player["vida"] -= dano_goblin
            print(f"\n{goblin['nome']} atacou você causando {dano_goblin} de dano!")

        if player["vida"] <= 0:
            print("\nVocê foi derrotado! Game over!")
            break
        
    print("Você derrotou todos os goblins!")
    return True

def habilidade_especial(player, inimigos):
    # Realiza o ataque especial do jogador
    print(f"\n{player['nome']} usa {player['habilidade']}!")
    if player["classe"] == "Mago":
        dano = player["magia"] + random.randint(10, 20)
        for inimigo in inimigos:
            inimigo["vida"] -= dano
            print(f"Você lançou uma Bola de Fogo em {inimigo['nome']} e causou {dano} de dano")
    elif player["classe"] == "Paladino":
        player["vida"] += 30
        print("Você usou Benção divina e recuperou 30 de vida")
    elif player["classe"] == "Arqueiro":
        inimigo = random.choice(inimigos)
        dano = player["força"] + random.randint(5, 10)
        inimigo["vida"] -= dano
        print(f"Você usou Tiro Certeiro em {inimigo['nome']} e causou {dano} de dano")
    elif player["classe"] == "Guerreiro":
        inimigo = random.choice(inimigos)
        dano = player["força"] + random.randint(10, 15)
        inimigo["vida"] -= dano
        print(f"Você usou Decapitação em {inimigo['nome']} e causou {dano} de dano")

def enigma_do_portao():
    print("\n--- Nível 1: A Entrada Misteriosa ---")
    time.sleep(3)
    print("\nVocê encontrou uma porta trancada com um enigma inscrito.")
    time.sleep(2)
    print("Enigma: 'Para abrir esta porta, responda o que eu sou: Mais leve que o ar, mas que muitos monstros afogo, sou invisível, mas me sentes a soprar.'")

    resposta = input("Digite sua resposta: ").strip().lower()

    if resposta == "o vento" or resposta == "vento":
        print("A porta se abre lentamente com um rangido sinistro. Você pode avançar!")
        return True
    else:
        print("Resposta incorreta. A porta permanece trancada.")
        return False

def primeiro_nivel(player):
    # Define o primeiro nível do jogo
    sucesso = enigma_do_portao()
    if not sucesso:
        return combate(player, goblins)
    return True

def iniciar_nivel_1():
    introducao()
    escolher_res()
    player = escolher_classe()
    sucesso_primeiro_nivel = primeiro_nivel(player)

    if sucesso_primeiro_nivel:
        print("\nParabéns, você passou pelo primeiro nível!")
    else:
        print("\nTente novamente...")

if __name__ == "__main__":
    iniciar_nivel_1()