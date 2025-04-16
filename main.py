from personagem import escolher_classe
from nivel1 import nivel_um
from nivel2 import nivel_dois
from nivel3 import nivel_tres
# from nivel4 import nivel_quatro
# from nivel5 import nivel_cinco
import os
import time

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("                               === Bem-vindo à Masmorra do Fim! ===\n")
    time.sleep(5)
    print("                               Jogo em desenvolvimento (Versão beta)\n")
    player = escolher_classe()
    limpar_terminal()
    print(f"\n                        {player['nome']} O {player['classe']}, prepare-se para sua jornada...\n")
    time.sleep(4)
    limpar_terminal()

    nivel_um(player)
    limpar_terminal()
    nivel_dois(player)
    limpar_terminal()
    nivel_tres(player)
    limpar_terminal()

if __name__ == "__main__":
    main()