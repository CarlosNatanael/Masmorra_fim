# pyinstaller --onefile --add-data "nivel1.py;." --add-data "nivel2.py;." --add-data "nivel3.py;." --add-data "nivel4.py;." --add-data "nivel5.py;." --add-data "utils/combate.py;utils" --add-data "utils/creditos.py;utils" --add-data "utils/personagem.py;utils" --add-data "utils/utils.py;utils" --add-data "utils/image.png;utils" --add-data "icone.ico;." --icon="icone.ico" --name "MasmorraDoFim" main.py


from utils.personagem import escolher_classe
from nivel1 import nivel_um
from nivel2 import nivel_dois
from nivel3 import nivel_tres
from nivel4 import nivel_quatro
from nivel5 import nivel_cinco
from utils.creditos import creditos_finais
from utils.utils import limpar_terminal
from nivel6_1 import nivel_verdade_1
from nivel6_2 import nivel_mentira_2
from nivel6_3 import nivel_destruicao_3
import time

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
    """)
    print("""
                                Jogo em desenvolvimento 
          
    Progamador:                                             [Masmorra do Fim - versão beta]
    Carlos Natanael
                                       
    - Inplementação de novos níveis
    - 8 níveis completos
    - Melhorias e atualizações de combate
        

                       Copyright (c) 2025 by Carlos Natanael 
    """)
    time.sleep(3)
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
    resultado_nivel5 = nivel_cinco(player)
    if resultado_nivel5:
        escolha_final = resultado_nivel5  
        if escolha_final  == "1":
            print("""
Você age como antes, seguindo as regras sem questionar.
                  
Velthurion sorri, mas não há calor em sua expressão.
"Ordem. Respeito às estruturas. Interessante... mas será que a masmorra precisa de mais um carcereiro?"
Ele ergue a mão, e o chão se abre sob seus pés.

Você cai... e acorda em um lugar novo:
            """)
            input("Pressione ENTER para continuar")
            limpar_terminal()
            if not nivel_verdade_1(player):
                game_over()
        elif escolha_final == "2":
            print("""
Você protege a criança, mesmo sabendo que está quebrando as regras.
                  
Velthurion ri, um som que ecoa como vidro quebrando.
"Ah, o herói. O justiceiro. Mas será que sua bondade sobreviverá quando você vir o que realmente habita nas sombras?"
Ele abre um portal negro com um gesto.

Você é sugado para dentro... e acorda em:
            """)
            input("Pressione ENTER para continuar")
            limpar_terminal()
            if not nivel_mentira_2(player):
                game_over()
        elif escolha_final == "3":
            print("""
Você resolve o conflito sem violência, mas sem ignorar a injustiça.
                  
Velthurion franze a testa, como se sua resposta fosse um enigma.
"Equilíbrio... mas equilíbrio pode ser apenas covardia disfarçada."
Ele abre um portal prateado, e você é puxado para dentro.
                  
Você acorda em:
            """)
            input("Pressione ENTER para continuar")
            limpar_terminal()
            if not nivel_destruicao_3(player):
                game_over()
        else:
            print("Combinação inválida de caminho!")
            game_over()

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