import random

def escolher_classe():
    nome = input("Digite o nome do seu personagem: ").strip()
    while not nome:
        nome = input("Nome não pode estar vazio. Digite novamente: ").strip()
    print("\nEscolha uma classe para o seu personagem:")
    print("1. Mago\n2. Guerreiro\n3. Paladino\n4. Arqueiro")
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
            "vida": random.randint(40, 50),
            "força": random.randint(30, 40),
            "magia": random.randint(36, 46),
            "defesa": random.randint(30, 40),
            "habilidade": "Bola de Fogo",
            "arma": "Cajado"
        })
    elif escolha == "2":
        base_player.update({
            "classe": "Guerreiro",
            "vida": random.randint(50, 60),
            "força": random.randint(35, 45),
            "magia": random.randint(20, 20),
            "defesa": random.randint(35, 45),
            "habilidade": "Decapitação",
            "arma": "Machado"
        })
    elif escolha == "3":
        base_player.update({
            "classe": "Paladino",
            "vida": random.randint(50, 60),
            "força": random.randint(35, 45),
            "magia": random.randint(35, 40),
            "defesa": random.randint(36, 46),
            "habilidade": "Benção Divina",
            "arma": "Espada"
        })
        base_player["itens"]["poção de cura"] = 2
    elif escolha == "4":
        base_player.update({
            "classe": "Arqueiro",
            "vida": random.randint(45, 55),
            "força": random.randint(35, 45),
            "magia": random.randint(20, 20),
            "defesa": random.randint(35, 40),
            "habilidade": "Tiro Certeiro",
            "arma": "Arco"
        })

    return base_player

def transformar_em_monarca(player):
    # Salva apenas o nome e itens básicos
    nome = player["nome"]
    itens = {"poção de cura": 3}  # Itens básicos para o Monarca
    
    # Define os novos atributos básicos
    novo_player = {
        "nome": nome,
        "classe": "Monarca das Sombras",
        "nivel": 1,
        "xp": 0,
        "xp_proximo_nivel": 100,
        "vida": random.randint(60, 70),
        "força": random.randint(60, 70),
        "magia": random.randint(60, 80),
        "defesa": random.randint(70, 80),
        "habilidade": "Domínio das Sombras",
        "arma": "Espada negra",
        "itens": itens,
        "monarca_sombra": True  # Flag especial
    }
    
    # Atualiza o player original com os novos valores
    player.clear()
    player.update(novo_player)
    
    print("\nSua forma muda completamente. Todas as memórias anteriores se dissipam...")
    print("| » Você renasceu como Monarca das Sombras (Nível 1)")
    print(f"| Status básicos: Vida {player['vida']}, Força {player['força']}, Magia {player['magia']}, Defesa {player['defesa']}\n")
    return player