from utils.combate import combate

def nivel_destruicao_3(player):
    print("""
    O Teatro das Máscaras Vazias
    
    Atores sem rosto repetem peças infinitas. Você percebe
    que eles estão encenando... sua própria vida!
    """, 5)
    
    print("\nDiretor: 'Tome seu lugar no palco. Torne-se Eldramar nesta tragédia.'")
    escolha = input("Aceitar o papel? (s/n): ").lower()
    
    if escolha == "n":
        diretor = {
            "nome": "O Diretor",
            "vida": 100,
            "força": 40,
            "defesa": 80,
            "habilidade": "Troca de Papéis"
        }
        return combate(player, [diretor])
    else:
        print("\nVocê se torna parte da peça eterna...", 3)
        return False  # Final ruim