from utils.combate import combate
import time
import random

def nivel_destruicao_3(player):
    print("Capítulo 6:  O Teatro das Máscaras Vazias")
    time.sleep(2)
    print("""
Quando a luz prateada se dissipou, me encontrei em uma plateia infinita. Cadeiras de veludo vermelho se estendiam até onde a vista alcançava, todas vazias. 
À minha frente, um palco iluminado por holofotes fantasmas, onde figuras sem rosto representavam uma peça sem sentido.
    """)
    time.sleep(2)
    print("...uma plateia vazia e infinita. Cadeiras de veludo vermelho cobrem o horizonte.")
    from utils.utils import usar_itens
    if not usar_itens(player):
        return False
    time.sleep(5)
    print("\nNo centro, um palco iluminado onde figuras sem rosto encenam sua vida.")
    time.sleep(3)
    print("\n\"ATENÇÃO PARA O NOVO PARTICIPANTE!\"")
    print("""
A voz ecoou como um megafone antigo. No centro do palco, um homem alto com trajes de diretor
mas com um rosto completamente liso - gesticulava em minha direção.
    """)
    print("Os atores sem rosto começaram a se multiplicar, cada um representando versões diferentes de mim:")
    print("– Uma criança oferecendo uma maçã... você aceitando.")
    print("– Sua queda na masmorra.")
    print("– Você... no trono de Velthurion.")
    time.sleep(4)
    print("\nO Diretor se aproxima com um roteiro encadernado em algo que parece... pele.")
    print("Ele oferece três caminhos:")
    while True:
        print("""
1 - Assinar o roteiro
2 - Rasgar a máscara do seu rosto 
3 - Investigar a cortina negra no fundo do palco
""")
        escolha = input("Qual sua escolha? ").strip()

        if escolha == "1":
            print("\nVocê assina o roteiro. Um calor preenche seu corpo. Você sente... poder.\n")
            print(f"| » Status atual: Monarca das Sombra ({player['classe']})\n")
            print("Mas algo se perde. Seu nome... seu propósito... começa a sumir.")
            player['força'] += 5
            player['magia'] += 5
            player['xp'] += 10
            print("⚠️ Sua identidade está fragmentada. Cuidado.\n")
            break

        elif escolha == "2":
            print("\nCom um grito primal, você agarra a máscara que cobria seu verdadeiro eu.")
            time.sleep(2)
            print("Há um momento de silêncio absoluto... então...")
            time.sleep(3)
            
            if random.random() < 0.5:
                print("CRACK! A máscara se parte, revelando seu rosto verdadeiro!")
                time.sleep(2)
                print("O teatro inteiro começa a desmoronar, luzes explodindo, platéia gritando.")
                print("Você CORRE em direção à saída enquanto o mundo artificial se desfaz!\n")
                player['xp'] += 60
                player['força'] += 5
                break
            else:
                print("A máscara resiste. Você puxa com mais força... e sente sua carne vir junto.")
                time.sleep(3)
                print("Seu rosto se dissolve em tentáculos de tinta negra, escorrendo entre seus dedos.")
                print("O Diretor ri enquanto você se torna... apenas mais um figurante sem rosto.")
                player['vida'] = 0
                return False 

        elif escolha == "3":
            print("\nVocê corre até a cortina negra. Atrás dela...")
            time.sleep(2)
            print("...há um homem velho, acorrentado, com penas e tinta nas mãos. O verdadeiro autor.")
            time.sleep(2)
            print("Ele sussurra: \"O Diretor nos escraviza. Rasgue o roteiro, liberte o palco.\"")
            time.sleep(2)
            print("\n(Você rasga o roteiro.)\n")
            time.sleep(2)
            print("Diretor: O SHOW DEVE CONTINUAR!, gritou o Diretor, enquanto o teatro começava a desmoronar.\n")
            diretor = {
            "nome": "Diretor",
            "classe": "Mago",
            "vida": 100,
            "força": 70,
            "defesa": 80,
            "habilidade": "Troca de Papéis",
            "nivel": 9,
            "xp": 200
            }
            input("\nPrepare-se para enfrentar O Diretor! Pressione ENTER...\n")
            if not combate(player, [diretor]):
                return 
            print("O teatro inteiro era apenas mais uma camada da masmorra... e o Diretor, apenas mais um prisioneiro como eu.")
            break

        else:
            print("Escolha inválida. Tente novamente.")
    
    input("Você avança. Pressione ENTER para continuar...\n")
    return True