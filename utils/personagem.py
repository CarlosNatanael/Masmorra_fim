import random

def escolher_classe():
    nome = input("Digite o nome do seu personagem: ").strip()
    while not nome:
        nome = input("Nome não pode estar vazio. Digite novamente: ").strip()
    print("\nEscolha uma classe para o seu personagem:")
    print("1. Mago\n2. Paladino\n3. Arqueiro\n4. Guerreiro")
    escolha = input("Digite o número da classe escolhida: ")

    # Primeiro criamos o dicionário base
    base_player = {
        "nome": nome,
        "xp": 0,
        "nivel": 1,
        "xp_proximo_nivel": 100,
        "itens": {
            "poção de cura": 3,
        }
    }

    if escolha == "1":
        base_player.update({
            "classe": "Mago",
            "vida": random.randint(50, 60),
            "força": random.randint(26, 40),
            "magia": random.randint(40, 70),
            "defesa": random.randint(30, 40),
            "habilidade": "Bola de Fogo",
            "arma": "Cajado"
        })
    elif escolha == "2":
        base_player.update({
            "classe": "Paladino",
            "vida": random.randint(60, 80),
            "força": random.randint(30, 40),
            "magia": random.randint(20, 25),
            "defesa": random.randint(30, 40),
            "habilidade": "Benção Divina",
            "arma": "Espada"
        })
        base_player["itens"]["poção de cura"] = 2
    elif escolha == "3":
        base_player.update({
            "classe": "Arqueiro",
            "vida": random.randint(40, 60),
            "força": random.randint(25, 35),
            "magia": random.randint(10, 20),
            "defesa": random.randint(30, 40),
            "habilidade": "Tiro Certeiro",
            "arma": "Arco"
        })
    elif escolha == "4":
        base_player.update({
            "classe": "Guerreiro",
            "vida": random.randint(60, 80),
            "força": random.randint(30, 40),
            "magia": random.randint(5, 15),
            "defesa": random.randint(30, 40),
            "habilidade": "Decapitação",
            "arma": "Machado"
        })
    else:
        print("Escolha inválida, por favor, escolha novamente.")
        return escolher_classe()

    return base_player