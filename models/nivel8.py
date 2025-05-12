from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound_py.sound8 import tocar_musica
from game_sound_py.sound8 import parar_musica
from utils.utils import limpar_terminal
from utils.combate import combate
from utils.utils import encontrar_bau
from rich import print
from rich import print as rprint
from rich.panel import Panel
import time
import random
import pygame

pygame.init()
pygame.mixer.init()

def nivel_oito(player):
    tocar_musica()
    rprint(Panel.fit("[bold yellow]Capítulo 8: O Coração da Masmorra[/]", style="blue"))
    time.sleep(5)
    print("Você sente o calor antes mesmo de enxergar...")
    time.sleep(3)
    # Chance de encontrar baús antes da batalha final
    if random.random() < 0.5:  # 50% de chance de encontrar 1-3 baús
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
    print("[bold red]Velthurion[/bold red]: Você chegou tarde demais para salvá-los.")
    time.sleep(4)

    print("\nO caldeirão cospe três lingotes no chão...")
    print("Eles se moldam nas figuras que você reconhece com horror:")
    time.sleep(5)
    print("'- O Diretor do Teatro: agora, uma marionete de nervos.'")
    print("'- O Lorde dos Espectros: um saco de pele vazio.'")
    print("'- O Anjo da Obediência: suas asas, uma prisão de ossos.'")
    time.sleep(7)

    print("\nVelthurion aponta para seu peito vazio.")
    print("[bold red]Velthurion[/bold red]: Seu coração será perfeito.")
    time.sleep(3)
    print("[bold red]Velthurion[/bold red]: Será rápido. Você nem sentirá.")

    # Batalha contra Velthurion
    Velthurion = {
        "nome": "Velthurion, o Artesão Infernal",
        "classe": "Demônio",
        "vida": 180,
        "força": 80,
        "magia": 90,
        "defesa": 80,
        "habilidade": "Lança chamas",
        "nivel": 11,
        "xp": 550
    }
    input("\nPressione ENTER para iniciar o combate final...\n")
    if combate(player, [Velthurion]):
        mostrar_conquista("coração_libertado_8")
    else:
        return False
    print("\nVelthurion cai. O vazio em seu peito implode silenciosamente.")
    print("As correntes se soltam. As almas choram em liberdade.")
    mostrar_conquista("coração_libertado_8")
    time.sleep(5)
    limpar_terminal()
    print("\nVocê descobre que o primeiro lingote criado ali... era Eldramar.")
    time.sleep(5)
    print("E que a Masmorra do Fim ainda guarda outros horrores além deste portal.")
    time.sleep(5)
    print("\nVelthurion soltou um rangido que poderia ter sido uma risada quando você mencionou Eldramar.")
    print("[bold red]Velthurion[/bold red]: Ah, o grande arquiteto... Suas engrenagens tremeram com sarcasmo. Ele só é poderoso enquanto a forja queima.")
    time.sleep(5)
    print("\n[bold red]Velthurion[/bold red]: Cada alma que eu martelo aqui vira pó de estrela... e ele bebe essa energia como um vampiro sedentento")
    time.sleep(5)
    print("""
A VERDADE SOBRE A MASMORRA
O Ciclo de Alimentação

[bold red]Velthurion[/bold red]: As almas derrotadas nos níveis anteriores eram matéria-prima

[bold red]Velthurion[/bold red]: O Teatro das Máscaras destilava emoções puras

[bold red]Velthurion[/bold red]: A Floresta dos Espectros extraía ódio cristalizado

[bold red]Velthurion[/bold red]: O Cárcere produzia lágrimas de desespero condensado
        """)
    time.sleep(5)
    print("[bold red]Velthurion[/bold red]: Ele está definhando agora que você interrompeu o suprimento")
    time.sleep(5)
    print("[bold red]Velthurion[/bold red]: (Velthurion cuspiu..) Mas cuidado... um predador faminto é mais perigoso que um saciado.")
    time.sleep(5)
    print("""
A Origem da Forja
Um vislumbre mostrou:

Uma cidade antiga sendo engolida pelo chão

Eldramar como um mago humano, forjando o primeiro contrato com algo nas profundezas

Velthurion sendo transformado no primeiro artesão, seu corpo se desfazendo em ferramentas
        """)
    time.sleep(5)
    print("[bold red]Velthurion[/bold red]: Ele virá pessoalmente agora\n")
    print("O demônio alertou, enquanto partes de seu corpo começavam a se desfazer\n")
    time.sleep(5)
    print("[bold red]Velthurion[/bold red]: A masmorra é a pele dele. As paredes são suas veias. E você... você acabou de cortar o suprimento de sangue.")
    time.sleep(5)
    print("""
Com um último estalo metálico, Velthurion desabou em uma pilha de ferramentas enferrujadas - sua maldição finalmente quebrada. 
    O silêncio que se seguiu foi pior que qualquer rugido.
        """)
    time.sleep(5)
    print("\nDentre os escombros, você encontra um baú revestido de ossos...")
    # Primeiro verifica se o baú aparece (30% de chance)
    if random.random() < 0.3:
        itens_especiais = [
            ("sangue de dragão", 0.6),    # 60% dos 30% (18% total)
            ("vigor do vulcão", 0.1),     # 10% dos 30% (3% total)
            ("sangue da montanha", 0.3)   # 30% dos 30% (9% total)
        ]
        itens, pesos = zip(*itens_especiais)
        item_especial = random.choices(itens, weights=pesos, k=1)[0]
        player["itens"][item_especial] += 1

        print(f"Você encontrou o item lendário: {item_especial}!")
        mostrar_conquista("artesao_da_sorte")
        input("\nPressione ENTER para continuar...\n")
        parar_musica()
        return True
    else:
        print("\nSeu coração para, seu corpo cai... e sua alma é tragada pela fornalha.")
        return False