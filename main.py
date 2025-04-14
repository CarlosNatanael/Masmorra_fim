import time
from personagem import escolher_classe
from combate import combate

def main():
    print("🎮 Bem-vindo à Masmorra do Fim!")
    player = escolher_classe()

    time.sleep(1)
    print(f"\n{player['nome']} o {player['classe']} foi criado com sucesso!")
    print(f"Atributos: Vida {player['vida']} | Força {player['força']} | Magia {player['magia']} | Defesa {player['defesa']}")
    time.sleep(2)

    # Combate teste (ou real depois do nivel1)
    goblins = [
        {"nome": "Goblin nv:1", "vida": 25, "força": 12},
        {"nome": "Goblin nv:2", "vida": 35, "força": 17},
    ]

    resultado = combate(player, goblins)
    if not resultado:
        print("☠️ Sua jornada termina aqui.")
        return

    print("\n✅ Combate vencido com sucesso!")
    # nivel1(player)

if __name__ == "__main__":
    main()
