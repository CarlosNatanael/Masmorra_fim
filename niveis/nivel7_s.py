from utils.utils import limpar_terminal
from utils.combate import combate
import time

def nivel_7_sombra(player):
    print("\n=== CAPÍTULO 7: O PRIMEIRO DECRETO ===")
    print("Como novo Monarca das Sombras, você deve consolidar seu poder...\n")
    time.sleep(3)
    
    print("Os últimos guardiões da luz se levantam contra você!")
    resistencia = {
        "nome": "Guardiões da Luz",
        "classe": "Paladinos",
        "vida": 200,
        "força": 70,
        "magia": 90,
        "defesa": 80,
        "habilidade": "Purificação",
        "nivel": player["nivel"] + 3,
        "xp": 350,
        "imunidades": ["Trevas"]
    }
    
    # Buff no jogador por ser sombrio
    player["força"] += 20
    player["magia"] += 30
    
    input("\nEsmague a resistência! Pressione ENTER...")
    resultado = combate(player, [resistencia])
    
    # Restaura atributos modificados
    player["força"] -= 20
    player["magia"] -= 30
    
    return resultado