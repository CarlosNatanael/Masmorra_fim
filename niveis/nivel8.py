from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound.sound1 import tocar_musica
from game_sound.sound1 import parar_musica
from utils.utils import limpar_terminal
from utils.combate import combate
import time
import random
import pygame

pygame.init()
pygame.mixer.init()

def gerar_itens_aleatorios():
    itens_possiveis = ["poção de cura", "poção de força", "poção de defesa"]
    
    itens = [random.choice(itens_possiveis)]
    
    # Chance de itens adicionais (30% para 2 itens, 10% para 3 itens)
    if random.random() < 0.3:
        itens.append(random.choice(itens_possiveis))
    if random.random() < 0.1:
        itens.append(random.choice(itens_possiveis))
    
    return itens

def encontrar_bau(player):
    # 20% de chance de ser um baú mímico
    if random.random() < 0.2:
        print("\nVocê encontra um baú ornamentado... mas algo parece estranho!")
        time.sleep(2)
        print("De repente, o baú se transforma em uma criatura monstruosa!")
        time.sleep(2)
        
        mimico = {
            "nome": "Baú Mímico",
            "classe": "Monstro",
            "vida": 40 + player["nivel"] * 5,
            "força": 30 + player["nivel"] * 3,
            "defesa": 60,
            "magia": 0,
            "habilidade": "Engolir",
            "nivel": player["nivel"] + 2,
            "xp": 50
        }
        
        if combate(player, [mimico]):
            print("\nO mímico se dissolve, revelando itens roubados de outras vítimas!")
            itens = gerar_itens_aleatorios()
            for item in itens:
                player["itens"][item] = player["itens"].get(item, 0) + 1
                print(f"Você encontrou: {item}!")
            mostrar_conquista("devorador_de_mimicos")
            
        else:
            return False
    else:
        print("\nVocê encontrou um baú antigo!")
        time.sleep(2)
        print("Ao abri-lo, encontra alguns itens úteis...")
        mostrar_conquista("mestre_dos_baús")
        itens = gerar_itens_aleatorios()
        for item in itens:
            player["itens"][item] = player["itens"].get(item, 0) + 1
            print(f"Você encontrou: {item}!")
    
    return True

def nivel_oito(player):
    tocar_musica()
    print("Capítulo 8: O Coração da Masmorra\n")
    time.sleep(5)
    print("Você sente o calor antes mesmo de enxergar...")
    time.sleep(3)

    # Chance de encontrar baús antes da batalha final
    if random.random() < 0.6:  # 60% de chance de encontrar 1-3 baús
        num_baus = random.randint(1, 3)
        print(f"\nEnquanto avança, você encontra {num_baus} baús suspeitos...")
        
        for _ in range(num_baus):
            if not encontrar_bau(player):
                return False  # Se o jogador morrer para um mímico

    print("\nUm sopro de fornalha queima seus cílios enquanto seus olhos tentam se ajustar à escuridão rubra.")
    time.sleep(4)
    print("\nEntão você vê: a Forja das Almas.")
    time.sleep(5)
    print("\nNão é uma construção — é um órgão vivo.")
    print("Ferro negro, ossos retorcidos, fumaça de carne queimada.")
    print("O Martelo cai sozinho, espinhas humanas entrelaçadas no cabo, esmagando almas em lingotes sussurrantes.")
    time.sleep(7)

    print("\nAs Correntes se movem como serpentes, arrastando memórias para dentro das chamas.")
    print("O caldeirão borbulha. Mãos prateadas tentam escapar.")
    time.sleep(6)

    print("\nNo centro disso tudo, trabalha Velthurion — o Artesão Infernal.")
    time.sleep(4)

    print("\nEle não se vira. Seu braço se transforma em um martelo de carne e aço.")
    print("Sua verdadeira forma é um pesadelo: braços metamórficos, peito vazio sugando luz, pernas de engrenagem.")
    time.sleep(7)

    print("\nSua voz ecoa de todas as direções:")
    print("Velthurion : Você chegou tarde demais para salvá-los.")
    time.sleep(4)

    print("\nO caldeirão cospe três lingotes no chão...")
    print("Eles se moldam nas figuras que você reconhece com horror:")
    time.sleep(5)
    print("- O Diretor do Teatro: agora, uma marionete de nervos.")
    print("- O Lorde dos Espectros: um saco de pele vazio.")
    print("- O Anjo da Obediência: suas asas, uma prisão de ossos.")
    time.sleep(7)

    print("\nVelthurion aponta para seu peito vazio.")
    print("Velthurion : Seu coração será perfeito.")
    time.sleep(3)
    print("Velthurion : Será rápido. Você nem sentirá.")
    input("\nPressione ENTER para iniciar o combate final...\n")

    # Batalha contra Velthurion
    inimigo = [{
        "nome": "Velthurion, o Artesão Infernal",
        "classe": "Demônio",
        "vida": 180,
        "força": 70,
        "magia": 90,
        "defesa": 80,
        "habilidade": "Lança chamas",
        "nivel": 11
    }]

    if combate(player, inimigo):
        limpar_terminal()
        print("\nVelthurion cai. O vazio em seu peito implode silenciosamente.")
        print("As correntes se soltam. As almas choram em liberdade.")
        mostrar_conquista("coração_libertado_8")
        time.sleep(5)
        print("\nVocê descobre que o primeiro lingote criado ali... era Eldramar.")
        time.sleep(5)
        print("E que a Masmorra do Fim ainda guarda outros horrores além deste portal.")
        time.sleep(5)
        print("\nVelthurion soltou um rangido que poderia ter sido uma risada quando você mencionou Eldramar.")
        print("Velthurion : Ah, o grande arquiteto... Suas engrenagens tremeram com sarcasmo. Ele só é poderoso enquanto a forja queima.")
        time.sleep(5)
        print("\nVelthurion : Cada alma que eu martelo aqui vira pó de estrela... e ele bebe essa energia como um vampiro sedentento")
        time.sleep(5)
        print("""
A VERDADE SOBRE A MASMORRA
O Ciclo de Alimentação

Velthurion : As almas derrotadas nos níveis anteriores eram matéria-prima

Velthurion : O Teatro das Máscaras destilava emoções puras

Velthurion : A Floresta dos Espectros extraía ódio cristalizado

Velthurion : O Cárcere produzia lágrimas de desespero condensado
        """)
        time.sleep(5)
        print("Velthurion : Ele está definhando agora que você interrompeu o suprimento")
        time.sleep(5)
        print("Velthurion : (Velthurion cuspiu..) Mas cuidado... um predador faminto é mais perigoso que um saciado.")
        time.sleep(5)
        print("""
A Origem da Forja
Um vislumbre mostrou:

Uma cidade antiga sendo engolida pelo chão

Eldramar como um mago humano, forjando o primeiro contrato com algo nas profundezas

Velthurion sendo transformado no primeiro artesão, seu corpo se desfazendo em ferramentas
        """)
        time.sleep(5)
        print("Velthurion : Ele virá pessoalmente agora\n")
        print("O demônio alertou, enquanto partes de seu corpo começavam a se desfazer\n")
        time.sleep(5)
        print("Velthurion : A masmorra é a pele dele. As paredes são suas veias. E você... você acabou de cortar o suprimento de sangue.")
        time.sleep(5)
        print("""
Com um último estalo metálico, Velthurion desabou em uma pilha de ferramentas enferrujadas - sua maldição finalmente quebrada. 
    O silêncio que se seguiu foi pior que qualquer rugido.
        """)
        time.sleep(5)
        print("\nDentre os escombros, você encontra um baú revestido de ossos...")
        itens_especiais = ["poção de cura", "poção de força", "poção de defesa"]
        item_especial = random.choice(itens_especiais)
        player["itens"][item_especial] += 2
        print(f"Você encontrou o item lendário: {item_especial}!")
        mostrar_conquista("artesao_da_sorte")

        input("\nPressione ENTER para continuar...\n")
        parar_musica()
        return True
    else:
        print("\nSeu coração para, seu corpo cai... e sua alma é tragada pela fornalha.")
        return False
