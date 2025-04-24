from utils.utils import limpar_terminal
import time
import os

def creditos_finais(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*60)
    print(" " * 18 + "🏆 FIM DA JORNADA 🏆")
    print("="*60)
    time.sleep(3)
    
    print(f"\nParabéns, {player['nome']}! Você sobreviveu à Masmorra do Fim.")
    print("As forças que protegiam Aldurian foram derrotadas por sua bravura.\n")
    time.sleep(4)

    print("Sua jornada será lembrada nas runas antigas...\n")
    time.sleep(3)

    print("="*60)
    print(" " * 24 + "🎬 CRÉDITOS 🎬")
    print("="*60)
    time.sleep(2)

    print("\nDesenvolvido por: Carlos Natanael")
    time.sleep(2)
    print("Programação: Carlos Natanael, Val")
    time.sleep(2)
    print("Desenvolvedor Tester: Arthur Yabuchi")
    time.sleep(2)
    print("Narrativa: Carlos Natanael")
    time.sleep(2)
    print("Assistência Criativa: Val")
    time.sleep(5)

    print("\n\nFerramentas Utilizadas:")
    print("- Linguagem Python 🐍")
    print("- Sistema Modular com Arquivos Separados")
    print("- ASCII Art para Ambientação")
    print("- Mecânica de Combate baseada em RPG Clássico")
    print("- Estilo Text-based Adventure\n")
    time.sleep(5)

    print("\nSe você curtiu, compartilhe com os amigos ou modifique e continue criando!\n")
    print("→ A Masmorra do Fim sempre renasce para novos heróis...\n")
    time.sleep(4)
    
    print("="*117)
    print("""

██    ██  █████  ██      ███████ ██    ██     ██████   ██████  ██████           ██  ██████   ██████   █████  ██████  
██    ██ ██   ██ ██      ██      ██    ██     ██   ██ ██    ██ ██   ██          ██ ██    ██ ██       ██   ██ ██   ██ 
██    ██ ███████ ██      █████   ██    ██     ██████  ██    ██ ██████           ██ ██    ██ ██   ███ ███████ ██████  
 ██  ██  ██   ██ ██      ██      ██    ██     ██      ██    ██ ██   ██     ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ 
  ████   ██   ██ ███████ ███████  ██████      ██       ██████  ██   ██      █████   ██████   ██████  ██   ██ ██   ██ 

    """)
    print("="*117)

    input("Pressione ENTER para encerrar o jogo...")
    limpar_terminal()
