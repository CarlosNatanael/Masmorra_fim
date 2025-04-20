# pyinstaller --onefile --add-data "nivel1.py;." --add-data "nivel2.py;." --add-data "nivel3.py;." --add-data "nivel4.py;." --add-data "nivel5.py;." --add-data "utils/combate.py;utils" --add-data "utils/creditos.py;utils" --add-data "utils/personagem.py;utils" --add-data "utils/utils.py;utils" --add-data "utils/image.png;utils" --add-data "icone.ico;." --icon="icone.ico" --name "MasmorraDoFim" main.py


from utils.personagem import escolher_classe
from nivel1 import nivel_um
from nivel2 import nivel_dois
from nivel3 import nivel_tres
from nivel4 import nivel_quatro
from nivel5 import nivel_cinco
from utils.creditos import creditos_finais
import os

def game_over():
    print("""\n
╔══════════════════════════════════════════╗
║                GAME OVER                 ║
╠══════════════════════════════════════════╣
║   Sua jornada termina aqui...            ║
║   Mas suas ações serão lembradas.        ║
║                                          ║
║   Pressione ENTER para sair              ║
╚══════════════════════════════════════════╝
""")
    input()
    limpar_terminal()
    exit()

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
│Classe: {player['classe']:<8}   │  Força:  {player['força']:<5}    │
│Nível: {player['nivel']:<8}    │ Magia:  {player['magia']:<5}     │
│XP: {player['xp']:<3}            │ Defesa: {player['defesa']:<5}     │
├───────────────────┴───────────────────┤
│ Habilidade Especial: {player['habilidade']:<15}  │
└───────────────────────────────────────┘

[Pressione ENTER para embarcar nesta aventura...]
""")

def main():
    print("""
                                 ┳┳┓                 ┓    ┏┓•   
                                 ┃┃┃┏┓┏┏┳┓┏┓┏┓┏┓┏┓  ┏┫┏┓  ┣ ┓┏┳┓
                                 ┛ ┗┗┻┛┛┗┗┗┛┛ ┛ ┗┻  ┗┻┗┛  ┻ ┗┛┗┗
             
                                         -..--.--.+------.                                          
                                      -........-.-.......-++-                                       
                                  --.+-........---........--.++.                                    
                                -...-...-+#######+++-.........+++-                                  
                               .-.....-.++++#+++++###++........+-++                                 
                              --...--+++#++++++##++#++#-.......----.                                
                             ..-.-+.+++#++++++#++++#####+--....-+..+-                               
                            .+.-.+.+++#++#++##+++#######++.....-+-..-+                              
                          .--.....++++++++++#++++########+-....--.--..+-                            
                         -.-++..+.#++#++++++++++#########+---..--.+-...-+                           
                       .-..--..--.#+##+++++#++#+##########+--.....#-.-..--                          
                       -...--..---#+##++#++#+++###########+--.--.+-+-...++ .-+                      
                       -........--#+#++++++#++++.        #+-..-.-+---.... --.-#.                    
                       -+--.....+.-+##++++               +--.--.-+.......-+...+-.                   
                    .--...-++..-+..+--.                 .+--.+..+-.---++...-+---.-                  
                   ---......-++++-..                                    .--------                    



                                Jogo em desenvolvimento 
          
    Progamador:                                             [Masmorra do Fim - versão beta]
    Carlos Natanael
                                       
    - Novo sistema de combate
    - 5 níveis completos
    - Melhorias de balanceamento
        

                       Copyright (c) 2025 by Carlos Natanael     
    """)
    input("\n[Pressione ENTER para embarcar nesta aventura...]\n")
    limpar_terminal()
    player = escolher_classe()
    limpar_terminal()
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
#   Nivel 1
    if not nivel_um(player):
        game_over()
        return
    limpar_terminal()
#=====================
#   Status jogador nivel1
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
#   Nivel 2
    if not nivel_dois(player):
        game_over()
        return
    limpar_terminal()
#=====================
#   Status jogador nivel2
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
#   Nivel 3
    if not nivel_tres(player):
        game_over()
        return
    limpar_terminal()
#=====================
#   Status jogador nivel3
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
#   Nivel 4
    if not nivel_quatro(player):
        game_over()
        return
    limpar_terminal()
#=====================
#   Status jogador nivel14
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
#   Nivel 5
    if not nivel_cinco(player):
        game_over()
        return
    limpar_terminal()
#=====================
#   Status jogador nivel15
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
    creditos_finais(player)

if __name__ == "__main__":
    main()