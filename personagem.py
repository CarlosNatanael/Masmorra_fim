import random

def escolher_classe():
    nome = input("Digite o nome do seu personagem: ").strip()
    while not  nome:
        nome = input("Nome não pode estar vazio. Digite novamente: ").strip()
    print("\nEscolha uma classe para o seu personagem:")
    print("1. Mago\n2. Paladino\n3. Arqueiro\n4. Guerreiro")
    escolha = input("Digite o número da classe escolhida: ")

    base_player = {
        "nome": nome,
        "xp": 0,
        "nivel": 1,
        "xp_proximo_nivel": 100,
    }

    if escolha == "1":
        base_player.update({
            "classe": "Mago",
            "vida": random.randint(30, 40),
            "força": random.randint(10, 25),
            "magia": random.randint(40, 70),
            "defesa": random.randint(10, 20),
            "habilidade": "Bola de Fogo",
            "itens": {"poção de cura": 3}
        })
    elif escolha == "2":
        base_player.update({
            "classe": "Paladino",
            "vida": random.randint(50, 70),
            "força": random.randint(25, 30),
            "magia": random.randint(10, 25),
            "defesa": random.randint(25, 30),
            "habilidade": "Benção Divina",
            "itens": {"poção de cura": 2}
        })
    elif escolha == "3":
        base_player.update({
            "classe": "Arqueiro",
            "vida": random.randint(40, 60),
            "força": random.randint(15, 25),
            "magia": random.randint(10, 20),
            "defesa": random.randint(20, 30),
            "habilidade": "Tiro Certeiro",
            "itens": {"poção de cura": 3}
        })
    elif escolha == "4":
        base_player.update({
            "classe": "Guerreiro",
            "vida": random.randint(60, 80),
            "força": random.randint(25, 30),
            "magia": random.randint(5, 15),
            "defesa": random.randint(25, 30),
            "habilidade": "Decapitação",
            "itens": {"poção de cura": 3}
        })
    else:
        print("Escolha inválida, por favor, escolha novamente.")
        return escolher_classe()

    return base_player
