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

    print("""
       ______
      / ____/___  ____ ___  ____ _____  _____
     / / __/ __ \\/ __ `__ \\/ __ `/ __ \\/ ___/
    / /_/ / /_/ / / / / / / /_/ / / / (__  ) 
    \\____/\\____/_/ /_/ /_/\\__,_/_/ /_/____/  
    """)
    time.sleep(3)

    print("\nDesenvolvido por: Carlos Natanael")
    print("Programação: Carlos Natanael, Val")
    print("Narrativa: Carlos Natanael")
    print("Assistência Criativa: Val")
    time.sleep(5)

    print("\n\nFerramentas Utilizadas:")
    print("- Linguagem Python 🐍")
    print("- Sistema Modular com Arquivos Separados")
    print("- ASCII Art para Ambientação")
    print("- Mecânica de Combate baseada em RPG Clássico")
    print("- Estilo Text-based Adventure\n")
    time.sleep(5)

    print("="*60)
    print(" " * 14 + "🌟 Obrigado por jogar! 🌟")
    print("="*60)
    print("\nSe você curtiu, compartilhe com os amigos ou modifique e continue criando!\n")
    print("→ A Masmorra do Fim sempre renasce para novos heróis...\n")
    time.sleep(4)
    
    input("Pressione ENTER para encerrar o jogo...")
