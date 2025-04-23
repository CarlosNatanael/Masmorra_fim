from utils.utils import limpar_terminal
from utils.combate import combate
import time

def nivel_7_humano(player):
    print("\n=== CAPÍTULO 7: O ÚLTIMO BASTIÃO ===")
    print("Você mantém sua humanidade, mas a masmorra ainda não acabou...\n")
    time.sleep(3)
    
    print("O verdadeiro Velthurion aparece, em sua forma final!")
    chefe = {
        "nome": "Velthurion - Forma Verdadeira",
        "classe": "Mago Supremo",
        "vida": 180,
        "força": 60,
        "magia": 120,
        "defesa": 70,
        "habilidade": "Aniquilação Arcana",
        "nivel": player["nivel"] + 3,
        "xp": 300
    }
    
    input("\nPrepare-se para o combate final! Pressione ENTER...")
    return combate(player, [chefe])