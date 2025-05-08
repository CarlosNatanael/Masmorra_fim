from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound.sound1 import tocar_musica
from game_sound.sound1 import parar_musica
from utils.personagem import transformar_em_monarca
from utils.combate import combate
from utils.utils import limpar_terminal
import time
import random
import pygame

pygame.init()
pygame.mixer.init()

def nivel_destruicao_3(player):
    tocar_musica()
    print("Capítulo 6:  O Teatro das Máscaras Vazias")
    time.sleep(2)
    print("""
Quando a luz prateada se dissipou, me encontrei em uma plateia infinita. Cadeiras de veludo vermelho se estendiam até onde a vista alcançava, todas vazias. 
À minha frente, um palco iluminado por holofotes fantasmas, onde figuras sem rosto representavam uma peça sem sentido.
    """)
    player["itens"]["poção de cura"] +=1
    print("Você encontra uma poção de cura reluzente no corpo dos monstros derrotados!")
    print("(A poção foi adicionada ao seu inventário)\n")
    print("Inventario atual:")
    for item, qtd in player["itens"].items():
        print(f"- {item}: {qtd}")
    time.sleep(5)
    time.sleep(2)
    print("...uma plateia vazia e infinita. Cadeiras de veludo vermelho cobrem o horizonte.")
    print("Você descide olhar a sua bolsa de itens.\n")
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
    print("– Você... no trono de Eldramar.")
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
            print(f"| » Status atual: Monarca das Sombras\n")
            mostrar_conquista("estrela_sombras")
            print("Sua forma muda. Suas emoções desaparecem lentamente. Você se torna uma nova forma.\n")
            transformar_em_monarca(player)
            input("Você avança. Pressione ENTER para continuar...\n")
            parar_musica()
            return "sombra"


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
                mostrar_conquista("sombra_sorte_4")
                input("Você avança. Pressione ENTER para continuar...\n")
                parar_musica()
                return "humano"
            else:
                print("A máscara resiste. Você puxa com mais força... e sente sua carne vir junto.")
                time.sleep(3)
                print("Seu rosto se dissolve em tentáculos de tinta negra, escorrendo entre seus dedos.")
                print("O Diretor ri enquanto você se torna... apenas mais um figurante sem rosto.")
                player['vida'] = 0
                return False 

        elif escolha == "3":
            print("\nVocê se afasta do Diretor, sentindo um frio inexplicável vindo da cortina negra.")
            time.sleep(2)
            print("Ao se aproximar, percebe que a cortina não é tecido - é feita de sombras sólidas que se agitam como chamas congeladas.")
            time.sleep(3)
            print("Ao tocá-la, suas mãos afundam na escuridão como em água negra...")
            time.sleep(2)
    
            print("\nDe repente, você é puxado para dentro! O mundo gira e...")
            time.sleep(3)
            limpar_terminal()
    
            print("""\n
Num pequeno cubículo atrás do palco, um homem esquelético está acorrentado a uma escrivaninha.
Suas mãos ensanguentadas seguram uma pena de ferro, arranhando incessantemente pergaminhos.
            """)
            time.sleep(4)
    
            print("Ele levanta o rosto - ou o que resta dele - e você vê:")
            print("1. Seus próprios olhos refletidos")
            print("2. Olhos vazios como os do Diretor")
            print("3. Nada - apenas buracos negros")
            time.sleep(2)
    
            olhos = random.choice([1, 2, 3])
            if olhos == 1:
                print("\nSão SEUS olhos! O homem sorri com seus lábios costurados:")
            elif olhos == 2:
                print("\nOs mesmos olhos do Diretor! O homem rosna como uma fera:")
            else:
                print("\nSeu estômago embrulha ao ver o vazio onde deveriam estar os olhos. Ele sussurra:")
    
            print('"Ele me roubou... como roubou de você... o FIM é a única saída verdadeira."')
            time.sleep(3)
    
            print("\nVocê nota que:")
            print("1. As correntes estão enferrujadas")
            print("2. Há uma chave pendurada na parede")
            print("3. Suas mãos já estão segurando a pena")
            time.sleep(2)
    
            acao = input("O que faz? (1-3): ").strip()
            if acao in ["1", "2"]:
                print("\nAo libertar o homem, ele se dissolve em páginas de um livro antigo.")
                print("As palavras voam e se reorganizam no ar, formando um novo roteiro:")
                print('"O ÚLTIMO ATO: O DESTRUIR DO CRIADOR"')
            else:
                print("\nA pena queima sua mão! Sangue escorre no pergaminho, escrevendo sozinho:")
                print('"O PREÇO DA VERDADE: O FIM DA ILUSÃO"')
    
            time.sleep(4)
            limpar_terminal()
    
            print("\nO teatro inteiro treme quando você reaparece no palco, o roteiro original em chamas!")
            print('O Diretor grita: "NÃO! ESSE NÃO É O FINAL ESCRITO!"')
            time.sleep(3)
    
            diretor = {
                "nome": "O Diretor",
                "classe": "Mago",
                "vida": 120,
                "força": 57,
                "magia": 90,
                "defesa": 80,
                "habilidade": ["Troca de Papéis", "Grito de Plateia", "Final Forçado"],
                "nivel": 10,
                "xp": 250,
            }
    
            print("\nO palco se transforma em um campo de batalha surreal:")
            print("- Cenários caem como dominós")
            print("- Cordas de marionetes se tornam armadilhas")
            print("- O chão está coberto de páginas rasgadas")
            time.sleep(4)
    
            input("\nO show virou combate! Pressione ENTER...")
            if combate(player, [diretor]):
                print("\nO Diretor ajusta sua gravata: 'Sempre precisamos de um vilão...'")
                mostrar_conquista("fim_espetaculo")
            else:
                return False
    
            print("\nAo derrotar o Diretor, sua máscara se quebra revelando...")
            time.sleep(3)
            print("1. Seu próprio rosto")
            print("2. O rosto do velho escritor")
            print("3. Um vazio sem fim")
    
            revelacao = random.choice([1, 2, 3])
            if revelacao == 1:
                print("\nVocê era o Diretor o tempo todo. A masmorra ri.")
            elif revelacao == 2:
                print("\nEra você acorrentado. O ciclo recomeça.")
            else:
                print("\nNão há rosto. Não há história. Apenas o vazio.")
    
            player['xp'] += 300
            player['nivel'] += 1
            mostrar_conquista("sombra_sorte_5")
            input("Você avança. Pressione ENTER para continuar...\n")
            parar_musica()
            return "humano"

        else:
            print("Escolha inválida. Tente novamente.")