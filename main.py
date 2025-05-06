# pyinstaller masmorra.spec

from niveis.nivel1 import nivel_um
from niveis.nivel2 import nivel_dois
from niveis.nivel3 import nivel_tres
from niveis.nivel4 import nivel_quatro
from niveis.nivel5 import nivel_cinco
from niveis.nivel6_1 import nivel_verdade_1
from niveis.nivel6_2 import nivel_mentira_2
from niveis.nivel6_3 import nivel_destruicao_3
from niveis.nivel7_h import nivel_7_humano
from niveis.nivel7_s import nivel_7_sombra
from niveis.nivel8 import nivel_oito
from niveis.nivel9 import nivel_nove
from utils.personagem import escolher_classe
from utils.creditos import creditos_finais
from utils.utils import limpar_terminal
from game_sound.menu_sound  import tocar_musica
from game_sound.menu_sound  import parar_musica
import time
import pygame

pygame.init()
pygame.mixer.init()

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
    
    nome = player['nome']
    classe = player['classe'][:15]  # Limita a 15 caracteres
    habilidade = player['habilidade'][:25]  # Limita a 25 caracteres

    topo = f"{nome}, {classe}"
    largura_total = 42
    centro = topo.center(largura_total)
    tocar_musica()
    print("╔" + "═" * largura_total + "╗")
    print(f"║{centro}║")
    print("║" + "    Prepare-se para sua Jornada!    ".center(largura_total) + "║")
    print("╚" + "═" * largura_total + "╝")

    print("┌" + "─" * 19 + "┬" + "─" * 19 + "┐")
    print("│      STATUS       │     ATRIBUTOS     │")
    print("├" + "─" * 19 + "┼" + "─" * 19 + "┤")
    print(f"│{'':19}│ Vida:   {player['vida']:<5}     │")
    print(f"│Classe: {player['classe']:<11}│ Força:  {player['força']:<5}     │")
    print(f"│Nível: {player['nivel']:<12}│ Magia:  {player['magia']:<5}     │")
    print(f"│XP: {player['xp']:<15}│ Defesa: {player['defesa']:<5}     │")
    print("├" + "─" * 39 + "┤")
    print(f"│ Habilidade Especial: {habilidade:<16} │")
    print("└" + "─" * 39 + "┘")
    print("\n[Pressione ENTER para embarcar nesta aventura...]\n")
    parar_musica()

def main():
    tocar_musica()
    limpar_terminal()
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
          
    Progamador/Desenvolvimento:                                             [Masmorra do Fim - versão beta]
    Carlos Natanael
          
    Desenvolvedor Tester:
    Arthur Yabuchi
                                       
    - Bugs nivel 8 resolvido                      - Adição de novas poções
    - Sistema de musica e conquistas OK           - Nivel 9 completo...
    - Balanceamento  de player                    - Realizado todas as correções de bugs
        

                       Copyright (c) 2025 by Carlos Natanael 
    """)
    time.sleep(3)
    input("\n[Pressione ENTER para embarcar nesta aventura...]\n")
    limpar_terminal()
    player = escolher_classe()
    limpar_terminal()
    mostrar_status_jogador(player)
    input()
    parar_musica()
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
#   Status jogador nivel4
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
#   Nivel 5
    resultado_nivel5 = nivel_cinco(player)

    if resultado_nivel5 is False:
        game_over()
        return
    if resultado_nivel5:
        escolha_final = resultado_nivel5
#===================================================================
#   Nivel 6_1
        if escolha_final  == "1":
            print("""
Você age como antes, seguindo as regras sem questionar.
                  
Eldramar sorri, mas não há calor em sua expressão.
"Ordem. Respeito às estruturas. Interessante... mas será que a masmorra precisa de mais um carcereiro?"
Ele ergue a mão, e o chão se abre sob seus pés.

Você cai... e acorda em um lugar novo:
            """)
            input("Pressione ENTER para continuar")
            limpar_terminal()
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
#===================================================================
#   Nivel 6_2
        elif escolha_final == "2":
            print("""
Você protege a criança, mesmo sabendo que está quebrando as regras.
                  
Eldramar ri, um som que ecoa como vidro quebrando.
"Ah, o herói. O justiceiro. Mas será que sua bondade sobreviverá quando você vir o que realmente habita nas sombras?"
Ele abre um portal negro com um gesto.

Você é sugado para dentro... e acorda em:
            """)
            input("Pressione ENTER para continuar")
            limpar_terminal()
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
#===================================================================
#   Nivel 6_3
        elif escolha_final == "3":
            print("""
Você resolve o conflito sem violência, mas sem ignorar a injustiça.
                  
Eldramar franze a testa, como se sua resposta fosse um enigma.
"Equilíbrio... mas equilíbrio pode ser apenas covardia disfarçada."
Ele abre um portal prateado, e você é puxado para dentro.
                  
Você acorda em:
            """)
            input("Pressione ENTER para continuar")
            limpar_terminal()
            mostrar_status_jogador(player)
            input()
            limpar_terminal()
        else:
            game_over()
            limpar_terminal()
            return

    resultado_nivel6 = None
    if escolha_final == "1":
        resultado_nivel6 = nivel_verdade_1(player)
    elif escolha_final == "2":
        resultado_nivel6 = nivel_mentira_2(player)
    elif escolha_final == "3":
        resultado_nivel6 = nivel_destruicao_3(player)

    if resultado_nivel6 is False:
        game_over()
        return
    limpar_terminal()
#=====================
#    Status jogador nivel6
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#==============================
# Nivel 7 Humano
    if resultado_nivel6 == "humano":
        print("\nA luz ainda brilha em você, mas o desafio final aguarda...")
        input("\nPressione ENTER para continuar...")
        limpar_terminal()
        if not nivel_7_humano(player):
            game_over()
            return
#==============================
# Nivel 7 Sombra
    elif resultado_nivel6 == "sombra":
        print("\nAs trevas sussurram seus novos poderes... a masmorra obedece!")
        input("\nPressione ENTER para continuar...")
        limpar_terminal()
        if not nivel_7_sombra(player):
            game_over()
            return
#==============================
#    Status jogador nivel7
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#==============================
#   Nivel 8
    if not nivel_oito(player):
        game_over()
        return
    limpar_terminal()
#=====================
#   Status jogador nivel8
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
#   Nivel 9
    if not nivel_nove(player):
        game_over()
        return
    limpar_terminal()
#=====================
#   Status jogador nivel9
    mostrar_status_jogador(player)
    input()
    limpar_terminal()
#=====================
    creditos_finais(player)

if __name__ == "__main__":
    main()