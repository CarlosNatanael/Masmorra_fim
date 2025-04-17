# pyinstaller --onefile --add-data "nivel1.py;." --add-data "nivel2.py;." --add-data "nivel3.py;." --add-data "nivel4.py;." --add-data "nivel5.py;." --add-data "combate.py;." --add-data "creditos.py;." --add-data "personagem.py;." --icon="icone.ico" --add-data="icone.ico;." --name "MasmorraDoFim" main.py

from personagem import escolher_classe
from nivel1 import nivel_um
from nivel2 import nivel_dois
from nivel3 import nivel_tres
from nivel4 import nivel_quatro
from creditos import creditos_finais
# from nivel5 import nivel_cinco
import os
import time

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_status_jogador(player):
    print(f"""\n
╔══════════════════════════════════════════╗
║         {player['nome']}, O {player['classe']:<15}        ║
║    Prepare-se para sua Jornada!          ║
╚══════════════════════════════════════════╝

┌───────────────────┬───────────────────┐
│      STATUS       │     ATRIBUTOS     │
├───────────────────┼───────────────────┤
│                   │ Vida:   {player['vida']:<5}     │
│ Classe: {player['classe']:<8}  │ Força:  {player['força']:<5}     │
│ Nível: {player['nivel']:<8}   │ Magia:  {player['magia']:<5}     │
│                   │ Defesa: {player['defesa']:<5}     │
├───────────────────┴───────────────────┤
│ Habilidade Especial: {player['habilidade']:<15}  │
└───────────────────────────────────────┘

[Pressione ENTER para embarcar nesta aventura...]
""")

def main():
    print("                               === Bem-vindo à Masmorra do Fim! ===\n")
    time.sleep(1)
    print("                               Jogo em desenvolvimento (Versão beta v3)\n")
    player = escolher_classe()
    limpar_terminal()
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
#   Nivel 1
    nivel_um(player)
    limpar_terminal()
#=====================
#   Status jogador nivel1
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
#   Nivel 2
    nivel_dois(player)
    limpar_terminal()
#=====================
#   Status jogador nivel2
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
#   Nivel 3
    nivel_tres(player)
    limpar_terminal()
#=====================
#   Status jogador nivel3
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
#   Nivel 4
    nivel_quatro(player)
    limpar_terminal()
#=====================
#   Status jogador nivel14
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
    creditos_finais(player)

if __name__ == "__main__":
    main()