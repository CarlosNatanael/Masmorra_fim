from utils.combate import combate
import time

def nivel_7_humano(player):
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
    time.sleep(5)
    print("A única regra escrita nas pedras:")
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
        print(f"\n{player['nome']}: (cauteloso) Você... está vivo?")
        time.sleep(5)
        print("Colecionador de Nomes: Vivo? Morto? São só palavras, e palavras... são minha mercadoria. (estende a mão, palma para cima) Você quer um mapa? Eu vendo.")
        time.sleep(5)
        print(f"\n{player['nome']}: Que tipo de pagamento você aceita?")
        print("Colecionador de Nomes: Nomes, é claro. O primeiro que você recebeu. O da sua avó? Do seu primeiro amor? Do seu pior inimigo? Cada um abre um caminho diferente...")
        print(f"\n{player['nome']}: E se eu me recusar?")
        print("""

Colecionador de Nomes: (inclina a cabeça) "Então você ficará mais leve a cada passo. Primeiro esquecerá rostos. Depois, lugares. 
Até que seu próprio reflexo não te reconheça." (balança a lamparina, onde luzes dançam como vagalumes presos) "Já aconteceu com outros."

(Os Afogados Secos emitem um som coletivo, como ossos rangendo.)

        """)
    elif escolha == "2":
        print("\nVocê segue a diante nas catacumbas...")
        time.sleep(5)
        print("De repente, uma sombra toma forma: O Colecionador de Nomes....")
        time.sleep(5)
        colecionador2 = {
            "nome": "Colecionador de Nomes",
            "classe": "Arqueiro",
            "vida": 150,
            "força": 60,
            "defesa": 70,
            "magia": 80,
            "habilidade": "Memorias Mortas",
            "nivel": 10,
            "xp": 300
        }
        input("\nPrepare-se para enfrentar O Colecionador de Nomes! Pressione ENTER...\n")
        if not combate(player,[colecionador2]):
            return False
        print("\nO Colecionador cai de joelhos, seus olhos costurados começam a sangrar fios de sombra.")
        time.sleep(5)
        print("Colecionador: (gargalhada rouca) Você quer mesmo saber a verdade? Então ouça bem, condenado...")
        print("Colecionador: Eldramar não é o dono desta masmorra - ele é apenas o cozinheiro do banquete.\n")
        time.sleep(5)
        print("Colecionador: E você... (tosse convulsiva) você é o prato principal.")
        print("Colecionador: Cada passo que dá aqui não é progresso - é apenas o fogo da forja crescendo mais forte.")
        time.sleep(5)
        print("Colecionador: Todos que vieram antes de você... (ergue mãos trêmulas) viraram combustível.")
        print("Colecionador: Mas há uma brecha... (voz se torna um sussurro) A forja precisa de almas, mas não suporta a luz de sua própria chama.")
        time.sleep(5)
        print("Colecionador: Destrua o núcleo... (pele começa a descascar) e talvez... talvez você queime Eldramar com seu próprio fogo.")
        print("\nSua pele começa a se fundir com as paredes úmidas, ossos estalando como gravetos secos.")
        time.sleep(5)
        print("Colecionador: (últimas palavras) Corra, tolo. Antes que ele sinta que você sabe demais...\n")
        time.sleep(5)
        print("O eco de sua risada final desaparece nos túneis...\n")
        time.sleep(5)

        player["vida"] += 20
        player["força"] += 20
        player["magia"] += 20

        print("Torres desabam. A luz penetra pelas rachaduras das catacumbas.")
        time.sleep(3)
        print("\nDo alto do firmamento, descem os Guardiões da Luz — os últimos defensores da Masmorra.")
        print("Eles vieram cumprir o Último Decreto: 'Dar a benção ao escolhido'")
        time.sleep(3)
        print("\nLiderados por um Paladino Ancestral com armadura feita de cristal solar, eles brandem a última chama do Éter.")
        print("Seu nome ecoa nos céus: **Altherion, o Guardião da Aurora**.\n")
        print(f"Altherion : Jovem {player['nome']} fique com a minha benção para poder derrotar o Mago Eldramar")
        print("Altherion junta as maõs e perto do peito e faz um feixe de luz e lança em você\n")
        print("| » Benção adiquirida: Sunshine\n")
        print(f"| Força aumentada para {player['força']} (+20)")
        print(f"| Vida aumentada para {player['vida']} (+20)")
        print(f"| Magia aumentada para {player['magia']} (+20)")
        time.sleep(5)
        print(f"""
Após isso Altherion começa a desaparecer e lhe deixa uma ultima mensagem....
    
    "Sobreviva jovem {player('classe')}"
              """)
        time.sleep(5)
        input("Pressione ENTER para continuar\n")
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
        print(f"{player['nome']}: (para o 3º Afogado) Vocês estão secos. Como podem beber?")
        time.sleep(5)
        print("""
Colecionador: (intervém, brusco) "Não desperdice tempo com eles. São só ecos de quem tentou burlar as regras." (ergue um frasco com um líquido turvo) "Uma memória por um mapa. Esse é o único negócio real aqui."
        """)
        time.sleep(5)
        print("2º Afogado: (urgente) Ele quer seu passado para alimentar as paredes! Elas crescem com lembranças!")
        time.sleep(5)
        print("(Nesse momento, o Personagem nota: as paredes das catacumbas pulsam, como se tivessem veias sob a pedra.)")

        print("O Colecionador ao ver que você não aceita a proposta ele lhe empurra as catacumbas")
        time.sleep(5)
        print("Ao avançar nas catacumbas você se depara com o Colecionador")
        time.sleep(2)
        colecionador = {
            "nome": "Colecionador de Nomes",
            "classe": "Arqueiro",
            "vida": 100,
            "força": 35,
            "defesa": 70,
            "magia": 80,
            "habilidade": "Memorias Mortas",
            "nivel": 9,
            "xp": 200
        }
        input("\nPrepare-se para enfrentar O Colecionador de Nomes! Pressione ENTER...\n")
        if not combate(player,[colecionador]):
            return False
        print("\nO Colecionador cai de joelhos, seus olhos costurados começam a sangrar fios de sombra.")
        time.sleep(5)
        print("Colecionador: (gargalhada rouca) Você quer mesmo saber a verdade? Então ouça bem, condenado...")
        print("Colecionador: Eldramar não é o dono desta masmorra - ele é apenas o cozinheiro do banquete.\n")
        time.sleep(5)
        print("Colecionador: E você... (tosse convulsiva) você é o prato principal.")
        print("Colecionador: Cada passo que dá aqui não é progresso - é apenas o fogo da forja crescendo mais forte.")
        time.sleep(5)
        print("Colecionador: Todos que vieram antes de você... (ergue mãos trêmulas) viraram combustível.")
        print("Colecionador: Mas há uma brecha... (voz se torna um sussurro) A forja precisa de almas, mas não suporta a luz de sua própria chama.")
        time.sleep(5)
        print("Colecionador: Destrua o núcleo... (pele começa a descascar) e talvez... talvez você queime Eldramar com seu próprio fogo.")
        print("\nSua pele começa a se fundir com as paredes úmidas, ossos estalando como gravetos secos.")
        time.sleep(5)
        print("Colecionador: (últimas palavras) Corra, tolo. Antes que ele sinta que você sabe demais...\n")
        time.sleep(5)
        print("O eco de sua risada final desaparece nos túneis...\n")
        time.sleep(5)

        player["vida"] += 20
        player["força"] += 20
        player["magia"] += 20

        print("Torres desabam. A luz penetra pelas rachaduras das catacumbas.")
        time.sleep(3)
        print("\nDo alto do firmamento, descem os Guardiões da Luz — os últimos defensores da Masmorra.")
        print("Eles vieram cumprir o Último Decreto: 'Dar a benção ao escolhido'")
        time.sleep(3)
        print("\nLiderados por um Paladino Ancestral com armadura feita de cristal solar, eles brandem a última chama do Éter.")
        print("Seu nome ecoa nos céus: **Altherion, o Guardião da Aurora**.\n")
        print(f"Altherion : Jovem {player['nome']} fique com a minha benção para poder derrotar o Mago Eldramar")
        print("Altherion junta as maõs e perto do peito e faz um feixe de luz e lança em você\n")
        print("| » Benção adiquirida: Sunshine\n")
        print(f"| Força aumentada para {player['força']} (+20)")
        print(f"| Vida aumentada para {player['vida']} (+20)")
        print(f"| Magia aumentada para {player['magia']} (+20)")
        time.sleep(5)
        print(f"""
Após isso Altherion começa a desaparecer e lhe deixa uma ultima mensagem....
    
    "Sobreviva jovem {player('classe')}"
              """)
        time.sleep(5)
        input("Pressione ENTER para continuar\n")
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
            "defesa": 70,
            "magia": 80,
            "habilidade": "Memorias Mortas",
            "nivel": 10,
            "xp": 300
        }
        input("\nPrepare-se para enfrentar O Colecionador de Nomes! Pressione ENTER...\n")
        if not combate(player,[colecionador2]):
            return False
        print("\nO Colecionador cai de joelhos, seus olhos costurados começam a sangrar fios de sombra.")
        time.sleep(5)
        print("Colecionador: (gargalhada rouca) Você quer mesmo saber a verdade? Então ouça bem, condenado...")
        print("Colecionador: Eldramar não é o dono desta masmorra - ele é apenas o cozinheiro do banquete.\n")
        time.sleep(5)
        print("Colecionador: E você... (tosse convulsiva) você é o prato principal.")
        time.sleep(5)
        print("Colecionador: Cada passo que dá aqui não é progresso - é apenas o fogo da forja crescendo mais forte.")
        time.sleep(5)
        print("Colecionador: Todos que vieram antes de você... (ergue mãos trêmulas) viraram combustível.")
        time.sleep(5)
        print("Colecionador: Mas há uma brecha... (voz se torna um sussurro) A forja precisa de almas, mas não suporta a luz de sua própria chama.")
        time.sleep(5)
        print("Colecionador: Destrua o núcleo... (pele começa a descascar) e talvez... talvez você queime Eldramar com seu próprio fogo.")
        print("\nSua pele começa a se fundir com as paredes úmidas, ossos estalando como gravetos secos.")
        time.sleep(5)
        print("Colecionador: (últimas palavras) Corra, tolo. Antes que ele sinta que você sabe demais...\n")
        time.sleep(5)
        print("O eco de sua risada final desaparece nos túneis...\n")
        time.sleep(5)

        player["vida"] += 20
        player["força"] += 20
        player["magia"] += 20

        print("Torres desabam. A luz penetra pelas rachaduras das catacumbas.")
        time.sleep(3)
        print("\nDo alto do firmamento, descem os Guardiões da Luz — os últimos defensores da Masmorra.")
        time.sleep(5)
        print("Eles vieram cumprir o Último Decreto: 'Dar a benção ao escolhido'")
        time.sleep(3)
        print("\nLiderados por um Paladino Ancestral com armadura feita de cristal solar, eles brandem a última chama do Éter.")
        time.sleep(5)
        print("Seu nome ecoa nos céus: **Altherion, o Guardião da Aurora**.\n")
        time.sleep(5)
        print(f"Altherion : Jovem {player["nome"]} fique com a minha benção para poder derrotar o Mago Eldramar")
        time.sleep(5)
        print("Altherion junta as maõs e perto do peito e faz um feixe de luz e lança em você\n")
        time.sleep(5)
        print("| » Benção adiquirida: Sunshine\n")
        print(f"| Força aumentada para {player["força"]} (+20)")
        print(f"| Vida aumentada para {player["vida"]} (+20)")
        print(f"| Magia aumentada para {player["magia"]} (+20)")
        time.sleep(5)
        print(f"""
Após isso Altherion começa a desaparecer e lhe deixa uma ultima mensagem....
    
    "Sobreviva jovem {player("classe")}"
              """)
        time.sleep(5)
        input("Pressione ENTER para continuar\n")
        return True