from utils.combate import combate

def nivel_mentira_2(player):
    print("""
    A Floresta dos Espectros Famintos
    
    Árvores sussurram segredos obscuros. O chão pulsa
    como se estivesse vivo. Você não está sozinho aqui...
    """, 5)
    
    # Encontro com o Lorde dos Desesperados
    print("\nLorde: 'Ofereço poder ilimitado... por um pedaço de sua alma.'")
    escolha = input("Aceitar? (s/n): ").lower()
    
    if escolha == "n":
        lorde = {
            "nome": "Lorde dos Desesperados",
            "vida": 150,
            "força": 70,
            "defesa": 50
        }
        return combate(player, [lorde])
    else:
        player["força"] += 30
        player["vida"] = 1
        print("\nVocê sente um vazio na alma... mas um poder sem limites!", 3)
        return True