from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound_py.sound7 import tocar_musica
from game_sound_py.sound7 import parar_musica
from utils.combate import combate
from utils.utils import limpar_terminal
import time
import pygame

pygame.init()
pygame.mixer.init()

def nivel_7_humano(player):
    tocar_musica()
    print("Capítulo 7: As Catacumbas da Luz Moribunda\n")
    time.sleep(5)
    print("Em vez de cair, fui expulso - como um caroço de fruta cuspido. Aterrissei em:")
    time.sleep(5)   
    print("\nUm labirinto de túneis onde tochas azuis queimavam eternamente...mas iluminavam nada.")
    print("As paredes respiravam, e os corredores se rearranjavam quando eu virava as costas.")
    time.sleep(5)
    print("\nEntre sombras azuis e ecos distantes, você encontra:")
    time.sleep(5)
    print("""
Em uma encruzilhada de túneis, sentado em um banco de pedra, um velho de olhos costurados com fio negro balançava uma lamparina de vidro rachado. 

À sua frente, três cadáveres ressecados, com lábios retraídos em sorrisos eternos, estavam enfileirados como bonecos macabros.
    """)
    print("Você descide olhar a sua bolsa de itens.\n")
    from utils.utils import usar_itens
    if not usar_itens(player):
        return False
    time.sleep(5)
    print("\nA única regra escrita nas pedras:")
    print("\"Nunca toque nas paredes — elas lembram.\"")
    time.sleep(5)
    print("\nEscolha como explorar o labirinto:\n")
    print("1. Falar com o Colecionador de Nomes")
    print("2. Seguir a própria voz pelos corredores")
    
    while True:
        escolha = input("Digite o número da sua escolha (1 ou 2): ")
        if escolha in ["1", "2"]:
            break
        print("Opção inválida! Por favor, digite 1 ou 2.")

    if escolha == "1":
        print(f"\n{player["nome"]}: (cauteloso) Você... está vivo?")
        time.sleep(5)
        print("Colecionador de Nomes: Vivo? Morto? São só palavras, e palavras... são minha mercadoria. (estende a mão, palma para cima) Você quer um mapa? Eu vendo.")
        time.sleep(5)
        print(f"\n{player["nome"]}: Que tipo de pagamento você aceita?")
        time.sleep(5)
        print("Colecionador de Nomes: Nomes, é claro. O primeiro que você recebeu. O da sua avó? Do seu primeiro amor? Do seu pior inimigo? Cada um abre um caminho diferente...")
        time.sleep(5)
        print(f"\n{player["nome"]}: E se eu me recusar?")
        print("""
Colecionador de Nomes: (inclina a cabeça) "Então você ficará mais leve a cada passo. Primeiro esquecerá rostos. Depois, lugares. 
Até que seu próprio reflexo não te reconheça." (balança a lamparina, onde luzes dançam como vagalumes presos) "Já aconteceu com outros."

(Os Afogados Secos emitem um som coletivo, como ossos rangendo.)
        """)
        time.sleep(5)
    elif escolha == "2":
        print("Você segue a diante nas catacumbas...")
        time.sleep(5)
        print("De repente, uma sombra toma forma: O Colecionador de Nomes....")
        time.sleep(5)
        colecionador2 = {
            "nome": "Colecionador de Nomes",
            "classe": "Arqueiro",
            "vida": 150,
            "força": 60,
            "defesa": 80,
            "magia": 80,
            "habilidade": "Memorias Mortas",
            "nivel": 10,
            "xp": 300
        }
        input("\nPrepare-se para enfrentar O Colecionador de Nomes! Pressione ENTER...\n")
        if combate(player,[colecionador2]):
            mostrar_conquista("silenciador_eco")
        else:
            return False
        print("\nO Colecionador cai de joelhos, seus olhos costurados começam a sangrar fios de sombra.\n")
        time.sleep(5)
        print("Colecionador: (gargalhada rouca) Você quer mesmo saber a verdade? Então ouça bem, condenado...")
        print("Colecionador: Eldramar não é o dono desta masmorra - ele é apenas o cozinheiro do banquete.\n")
        time.sleep(5)
        print("Colecionador: E você... (tosse convulsiva) você é o prato principal.\n")
        time.sleep(5)
        print("Colecionador: Cada passo que dá aqui não é progresso - é apenas o fogo da forja crescendo mais forte.")
        time.sleep(5)
        print("\nColecionador: Todos que vieram antes de você... (ergue mãos trêmulas) viraram combustível.\n")
        time.sleep(5)
        print("Colecionador: Mas há uma brecha... (voz se torna um sussurro) A forja precisa de almas, mas não suporta a luz de sua própria chama.")
        time.sleep(5)
        print("\nColecionador: Destrua o núcleo... (pele começa a descascar) e talvez... talvez você queime Eldramar com seu próprio fogo.")
        print("\nSua pele começa a se fundir com as paredes úmidas, ossos estalando como gravetos secos.")
        time.sleep(5)
        print("Colecionador: (últimas palavras) Corra, tolo. Antes que ele sinta que você sabe demais...\n")
        time.sleep(5)
        print("O eco da sua última risada desvanece pelas entranhas da masmorra...n")
        time.sleep(5)

        player["vida"] += 20
        player["força"] += 20
        player["magia"] += 20
        limpar_terminal()

        print("\nAs catacumbas tremem. Torres desabam.. A luz penetra pelas rachaduras das catacumbas.")
        time.sleep(3)
        print("Fendas de luz atravessam as rachaduras do mundo abaixo — como se o próprio céu sangrasse esperança.\n")
        time.sleep(5)
        print("Das alturas, eles descem.")
        time.sleep(3)
        print("\nOs Guardiões da Luz, os últimos sentinelas da velha ordem, envoltos em mantos dourados.")
        print("\nVieram cumprir o Último Decreto:")
        time.sleep(5)
        print("\"Conceder a bênção ao Escolhido.\"")
        time.sleep(5)
        print("""
À frente do grupo, uma figura imponente reluz como o sol da alvorada.
Sua armadura, feita de cristal solar, refrata a luz em espirais sagradas.
Na mão, a última chama do Éter.
        """)
        time.sleep(5)
        print("Seu nome ecoa como trovão nos corredores da eternidade:\n")
        time.sleep(4)
        print("\"Altherion, o Guardião da Aurora\"\n")
        print("Altherion (com voz grave e serena):")
        print(f"Altherion : Jovem {player["nome"]} fique com a minha benção para poder derrotar o Mago Eldramar")
        time.sleep(5)
        print("Altherion : A escuridão não será vencida apenas com espadas.")
        print("Altherion : Ela teme aquilo que não pode corromper: a esperança.\n")
        time.sleep(5)
        print("Altherion Ele junta as mãos sobre o peito. Uma esfera de luz pura começa a pulsar entre seus dedos.\n")
        time.sleep(5)
        print("Altherion : Leve minha bênção, Filho da Luz... Com ela, derrube Eldramar e devolva equilíbrio ao que resta do mundo.\n")
        time.sleep(5)
        print("Com um gesto solene, ele eleva a luz aos céus e, num movimento suave, a lança em sua direção.")
        time.sleep(5)
        print("""
A energia atravessa o ar como uma estrela cadente invertida.
              
Ao tocar seu peito, a luz se funde ao seu coração — e por um instante, você sente o peso de mil auroras.
        """)
        time.sleep(5)
        print("| » Benção adiquirida: Sunshine\n")
        mostrar_conquista("sagrado_recipiente")
        print(f"| → Força aumentada para {player["força"]} (+20)")
        print(f"| → Vida aumentada para {player["vida"]} (+20)")
        print(f"| → Magia aumentada para {player["magia"]} (+20)")
        time.sleep(5)
        print("\nA luz queima suavemente sob sua pele. Não como fogo... mas como uma lembrança de quem você já foi.")
        print("Altherion, agora envolto em partículas douradas, começa a desaparecer — como poeira de estrela dissolvendo-se no tempo.")
        print(f"""
Ele lhe lança um último olhar, repleto de pesar e esperança.
    
    "Sobreviva jovem {player["classe"]} da Luz"
              """)
        time.sleep(5)
        print("Logo após as palavras de Altherion se apagarem no ar, os Guardiões da Luz unem suas espadas, ")
        time.sleep(5)
        print("lanças e cajados — todos apontando para as entranhas do labirinto.\n")
        time.sleep(5)
        print("| » Os Guardiões da Luz canalizam um ataque celestial...")
        time.sleep(5)
        print("\nUm estrondo rasga as profundezas.")
        time.sleep(5)
        print("""
Feixes de pura luz etérea disparam contra as paredes vivas das catacumbas, rachando pedra, memória e sombra.
O labirinto geme — como se acordasse de um pesadelo eterno — e desmorona em direção ao vazio.
        """)
        time.sleep(4)
        print("""
Quando a poeira assenta, diante de você, um novo caminho se revela. 
    Uma escadaria de ossos polidos e runas esquecidas, descendo... para o último desafio.      
        """)
        input("Pressione ENTER para continuar\n")
        parar_musica()
        return True
    
    print("\nEscolha como explorar o labirinto:\n")
    print("1. Falar com o os Afogados Secos")
    print("2. Seguir a própria voz pelos corredores")
    
    while True:
        escolha1 = input("Digite o número da sua escolha (1 ou 2): ")
        if escolha1 in ["1", "2"]:
            break
        print("Opção inválida! Por favor, digite 1 ou 2.")
    
    if escolha1 == "1":
        print("\n(Os três cadáveres se viram em sincronia, olhos vazios brilhando com um líquido negro.)")
        time.sleep(5)
        print("1º Afogado: (voz de água parada) Ele mente... o preço é maior do que diz...")
        time.sleep(5)
        print(""" 
2º Afogado: (sussurro de vento em caverna) Nós... damos conselhos. De graça. (abre a boca, e um escorpião de carvão sai correndo pela língua ressecada)
        """)
        time.sleep(5)
        print("""
3º Afogado: (tom infantil) "Mas você tem que nos dar água! Só um gole! A gente promete não te puxar para o fundo!"
        """)
        time.sleep(5)
        print(f"{player["nome"]}: (para o 3º Afogado) Vocês estão secos. Como podem beber?")
        time.sleep(5)
        print("""
Colecionador: (intervém, brusco) "Não desperdice tempo com eles. São só ecos de quem tentou burlar as regras." (ergue um frasco com um líquido turvo) "Uma memória por um mapa. Esse é o único negócio real aqui."
        """)
        time.sleep(5)
        print("2º Afogado: (urgente) Ele quer seu passado para alimentar as paredes! Elas crescem com lembranças!\n")
        time.sleep(5)
        print(f"(Nesse momento, {player["nome"]} nota: as paredes das catacumbas pulsam, como se tivessem veias sob a pedra.)")
        print("O Colecionador ao ver que você não aceita a proposta ele lhe empurra as catacumbas")
        time.sleep(5)
        print("\nAo avançar nas catacumbas você se depara com o Colecionador")
        time.sleep(6)
        colecionador = {
            "nome": "Colecionador de Nomes",
            "classe": "Arqueiro",
            "vida": 110,
            "força": 56,
            "defesa": 60,
            "magia": 80,
            "habilidade": "Memorias Mortas",
            "nivel": 9,
            "xp": 200
        }
        input("\nPrepare-se para enfrentar O Colecionador de Nomes! Pressione ENTER...\n")
        if combate(player,[colecionador]):
            mostrar_conquista("silenciador_eco")
        else:
            return False
        print("\nO Colecionador cai de joelhos, seus olhos costurados começam a sangrar fios de sombra.\n")
        time.sleep(5)
        print("Colecionador: (gargalhada rouca) Você quer mesmo saber a verdade? Então ouça bem, condenado...")
        print("Colecionador: Eldramar não é o dono desta masmorra - ele é apenas o cozinheiro do banquete.\n")
        time.sleep(5)
        print("Colecionador: E você... (tosse convulsiva) você é o prato principal.\n")
        time.sleep(5)
        print("Colecionador: Cada passo que dá aqui não é progresso - é apenas o fogo da forja crescendo mais forte.")
        time.sleep(5)
        print("\nColecionador: Todos que vieram antes de você... (ergue mãos trêmulas) viraram combustível.\n")
        time.sleep(5)
        print("Colecionador: Mas há uma brecha... (voz se torna um sussurro) A forja precisa de almas, mas não suporta a luz de sua própria chama.")
        time.sleep(5)
        print("\nColecionador: Destrua o núcleo... (pele começa a descascar) e talvez... talvez você queime Eldramar com seu próprio fogo.")
        print("\nSua pele começa a se fundir com as paredes úmidas, ossos estalando como gravetos secos.")
        time.sleep(5)
        print("Colecionador: (últimas palavras) Corra, tolo. Antes que ele sinta que você sabe demais...\n")
        time.sleep(5)
        print("O eco da sua última risada desvanece pelas entranhas da masmorra...n")
        time.sleep(5)

        player["vida"] += 20
        player["força"] += 20
        player["magia"] += 20
        limpar_terminal()

        print("\nAs catacumbas tremem. Torres desabam.. A luz penetra pelas rachaduras das catacumbas.")
        time.sleep(3)
        print("Fendas de luz atravessam as rachaduras do mundo abaixo — como se o próprio céu sangrasse esperança.\n")
        time.sleep(5)
        print("Das alturas, eles descem.")
        time.sleep(3)
        print("\nOs Guardiões da Luz, os últimos sentinelas da velha ordem, envoltos em mantos dourados.")
        print("\nVieram cumprir o Último Decreto:")
        time.sleep(5)
        print("\"Conceder a bênção ao Escolhido.\"")
        time.sleep(5)
        print("""
À frente do grupo, uma figura imponente reluz como o sol da alvorada.
Sua armadura, feita de cristal solar, refrata a luz em espirais sagradas.
Na mão, a última chama do Éter.
        """)
        time.sleep(5)
        print("Seu nome ecoa como trovão nos corredores da eternidade:\n")
        time.sleep(4)
        print("\"Altherion, o Guardião da Aurora\"\n")
        print("Altherion (com voz grave e serena):")
        print(f"Altherion : Jovem {player["nome"]} fique com a minha benção para poder derrotar o Mago Eldramar")
        time.sleep(5)
        print("Altherion : A escuridão não será vencida apenas com espadas.")
        print("Altherion : Ela teme aquilo que não pode corromper: a esperança.\n")
        time.sleep(5)
        print("Altherion Ele junta as mãos sobre o peito. Uma esfera de luz pura começa a pulsar entre seus dedos.\n")
        time.sleep(5)
        print("Altherion : Leve minha bênção, Filho da Luz... Com ela, derrube Eldramar e devolva equilíbrio ao que resta do mundo.\n")
        time.sleep(5)
        print("Com um gesto solene, ele eleva a luz aos céus e, num movimento suave, a lança em sua direção.")
        time.sleep(5)
        print("""
A energia atravessa o ar como uma estrela cadente invertida.
              
Ao tocar seu peito, a luz se funde ao seu coração — e por um instante, você sente o peso de mil auroras.
        """)
        time.sleep(5)
        print("| » Benção adiquirida: Sunshine\n")
        mostrar_conquista("sagrado_recipiente")
        print(f"| → Força aumentada para {player["força"]} (+20)")
        print(f"| → Vida aumentada para {player["vida"]} (+20)")
        print(f"| → Magia aumentada para {player["magia"]} (+20)")
        time.sleep(5)
        print("\nA luz queima suavemente sob sua pele. Não como fogo... mas como uma lembrança de quem você já foi.")
        print("Altherion, agora envolto em partículas douradas, começa a desaparecer — como poeira de estrela dissolvendo-se no tempo.")
        print(f"""
Ele lhe lança um último olhar, repleto de pesar e esperança.
    
    "Sobreviva jovem {player["classe"]} da Luz"
              """)
        time.sleep(5)
        print("Logo após as palavras de Altherion se apagarem no ar, os Guardiões da Luz unem suas espadas, ")
        time.sleep(5)
        print("lanças e cajados — todos apontando para as entranhas do labirinto.\n")
        time.sleep(5)
        print("| » Os Guardiões da Luz canalizam um ataque celestial...")
        time.sleep(5)
        print("\nUm estrondo rasga as profundezas.")
        time.sleep(5)
        print("""
Feixes de pura luz etérea disparam contra as paredes vivas das catacumbas, rachando pedra, memória e sombra.
O labirinto geme — como se acordasse de um pesadelo eterno — e desmorona em direção ao vazio.
        """)
        time.sleep(4)
        print("""
Quando a poeira assenta, diante de você, um novo caminho se revela. 
    Uma escadaria de ossos polidos e runas esquecidas, descendo... para o último desafio.      
        """)
        input("Pressione ENTER para continuar\n")
        parar_musica()
        return True
        
    elif escolha1 == "2":
        print("\nVocê segue a diante nas catacumbas...")
        time.sleep(5)
        print("De repente, uma sombra toma forma: O Colecionador de Nomes....")
        time.sleep(5)
        colecionador2 = {
            "nome": "Colecionador de Nomes",
            "classe": "Arqueiro",
            "vida": 150,
            "força": 60,
            "defesa": 80,
            "magia": 80,
            "habilidade": "Memorias Mortas",
            "nivel": 10,
            "xp": 300
        }
        input("\nPrepare-se para enfrentar O Colecionador de Nomes! Pressione ENTER...\n")
        if combate(player,[colecionador2]):
            mostrar_conquista("silenciador_eco")
        else:
            return False
        print("\nO Colecionador cai de joelhos, seus olhos costurados começam a sangrar fios de sombra.\n")
        time.sleep(5)
        print("Colecionador: (gargalhada rouca) Você quer mesmo saber a verdade? Então ouça bem, condenado...")
        print("Colecionador: Eldramar não é o dono desta masmorra - ele é apenas o cozinheiro do banquete.\n")
        time.sleep(5)
        print("Colecionador: E você... (tosse convulsiva) você é o prato principal.\n")
        time.sleep(5)
        print("Colecionador: Cada passo que dá aqui não é progresso - é apenas o fogo da forja crescendo mais forte.")
        time.sleep(5)
        print("\nColecionador: Todos que vieram antes de você... (ergue mãos trêmulas) viraram combustível.\n")
        time.sleep(5)
        print("Colecionador: Mas há uma brecha... (voz se torna um sussurro) A forja precisa de almas, mas não suporta a luz de sua própria chama.")
        time.sleep(5)
        print("\nColecionador: Destrua o núcleo... (pele começa a descascar) e talvez... talvez você queime Eldramar com seu próprio fogo.")
        print("\nSua pele começa a se fundir com as paredes úmidas, ossos estalando como gravetos secos.")
        time.sleep(5)
        print("Colecionador: (últimas palavras) Corra, tolo. Antes que ele sinta que você sabe demais...\n")
        time.sleep(5)
        print("O eco da sua última risada desvanece pelas entranhas da masmorra...")
        time.sleep(5)

        player["vida"] += 20
        player["força"] += 20
        player["magia"] += 20
        limpar_terminal()

        print("\nAs catacumbas tremem. Torres desabam.. A luz penetra pelas rachaduras das catacumbas.")
        time.sleep(3)
        print("Fendas de luz atravessam as rachaduras do mundo abaixo — como se o próprio céu sangrasse esperança.\n")
        time.sleep(5)
        print("Das alturas, eles descem.")
        time.sleep(3)
        print("\nOs Guardiões da Luz, os últimos sentinelas da velha ordem, envoltos em mantos dourados.")
        print("\nVieram cumprir o Último Decreto:")
        time.sleep(5)
        print("\"Conceder a bênção ao Escolhido.\"")
        time.sleep(5)
        print("""
À frente do grupo, uma figura imponente reluz como o sol da alvorada.
Sua armadura, feita de cristal solar, refrata a luz em espirais sagradas.
Na mão, a última chama do Éter.
        """)
        time.sleep(5)
        print("Seu nome ecoa como trovão nos corredores da eternidade:\n")
        time.sleep(4)
        print("\"Altherion, o Guardião da Aurora\"\n")
        print("Altherion (com voz grave e serena):")
        print(f"Altherion : Jovem {player["nome"]} fique com a minha benção para poder derrotar o Mago Eldramar")
        time.sleep(5)
        print("Altherion : A escuridão não será vencida apenas com espadas.")
        print("Altherion : Ela teme aquilo que não pode corromper: a esperança.\n")
        time.sleep(5)
        print("Altherion Ele junta as mãos sobre o peito. Uma esfera de luz pura começa a pulsar entre seus dedos.\n")
        time.sleep(5)
        print("Altherion : Leve minha bênção, Filho da Luz... Com ela, derrube Eldramar e devolva equilíbrio ao que resta do mundo.\n")
        time.sleep(5)
        print("Com um gesto solene, ele eleva a luz aos céus e, num movimento suave, a lança em sua direção.")
        time.sleep(5)
        print("""
A energia atravessa o ar como uma estrela cadente invertida.
              
Ao tocar seu peito, a luz se funde ao seu coração — e por um instante, você sente o peso de mil auroras.
        """)
        time.sleep(5)
        print("| » Benção adiquirida: Sunshine\n")
        mostrar_conquista("sagrado_recipiente")
        print(f"| → Força aumentada para {player["força"]} (+20)")
        print(f"| → Vida aumentada para {player["vida"]} (+20)")
        print(f"| → Magia aumentada para {player["magia"]} (+20)")
        time.sleep(5)
        print("\nA luz queima suavemente sob sua pele. Não como fogo... mas como uma lembrança de quem você já foi.")
        print("Altherion, agora envolto em partículas douradas, começa a desaparecer — como poeira de estrela dissolvendo-se no tempo.")
        print(f"""
Ele lhe lança um último olhar, repleto de pesar e esperança.
    
    "Sobreviva jovem {player["classe"]} da Luz"
              """)
        time.sleep(5)
        print("Logo após as palavras de Altherion se apagarem no ar, os Guardiões da Luz unem suas espadas, ")
        time.sleep(5)
        print("lanças e cajados — todos apontando para as entranhas do labirinto.\n")
        time.sleep(5)
        print("| » Os Guardiões da Luz canalizam um ataque celestial...")
        time.sleep(5)
        print("\nUm estrondo rasga as profundezas.")
        time.sleep(5)
        print("""
Feixes de pura luz etérea disparam contra as paredes vivas das catacumbas, rachando pedra, memória e sombra.
O labirinto geme — como se acordasse de um pesadelo eterno — e desmorona em direção ao vazio.
        """)
        time.sleep(4)
        print("""
Quando a poeira assenta, diante de você, um novo caminho se revela. 
    Uma escadaria de ossos polidos e runas esquecidas, descendo... para o último desafio.      
        """)
        input("Pressione ENTER para continuar\n")
        parar_musica()
        return True