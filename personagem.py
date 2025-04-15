import random

def escolher_classe():
    nome = input("Digite o nome do seu personagem: ")

    print("\nEscolha uma classe para o seu personagem:")
    print("1. Mago\n2. Paladino\n3. Arqueiro\n4. Guerreiro")
    escolha = input("Digite o número da classe escolhida: ")

    if escolha == "1":
        return {
            "nome": nome,
            "classe": "Mago",
            "vida": random.randint(30, 50),
            "força": random.randint(5, 15),
            "magia": random.randint(70, 90),
            "defesa": random.randint(10, 20),
            "habilidade": "Bola de Fogo",
            "itens": {"poção de cura": 3}
        }
    elif escolha == "2":
        return {
            "nome": nome,
            "classe": "Paladino",
            "vida": random.randint(80, 100),
            "força": random.randint(50, 70),
            "magia": random.randint(40, 60),
            "defesa": random.randint(60, 80),
            "habilidade": "Benção Divina",
            "itens": {"poção de cura": 2}
        }
    elif escolha == "3":
        return {
            "nome": nome,
            "classe": "Arqueiro",
            "vida": random.randint(50, 70),
            "força": random.randint(30, 50),
            "magia": random.randint(10, 20),
            "defesa": random.randint(20, 30),
            "habilidade": "Tiro Certeiro",
            "itens": {"poção de cura": 3}
        }
    elif escolha == "4":
        return {
            "nome": nome,
            "classe": "Guerreiro",
            "vida": random.randint(70, 90),
            "força": random.randint(60, 80),
            "magia": random.randint(5, 15),
            "defesa": random.randint(50, 70),
            "habilidade": "Decapitação",
            "itens": {"poção de cura": 1}
        }
    else:
        print("Escolha inválida, por favor, escolha novamente.")
        return escolher_classe()