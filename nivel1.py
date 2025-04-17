import time
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def nivel_um(player):
    print("Capítulo 1: O Despertar no Desconhecido\n")
    time.sleep(5)
    print("\nEra uma noite chuvosa quando entrei na Biblioteca de Arcanthus, um lugar antigo e abandonado, conhecido apenas por estudiosos de ocultismo.")
    time.sleep(5)
    print("As prateleiras empoeiradas guardavam livros proibidos, manuscritos arcanos e relíquias de eras esquecidas.\n")
    print('Eu, um simples pesquisador de mitos antigos, procurava por um texto chamado "O Grimório dos Reinos Perdidos"')
    print("Um livro que supostamente continha segredos sobre dimensões paralelas. Depois de horas revirando estantes.")
    time.sleep(5)
    print("Encontrei-o escondido atrás de uma cortina de teias de aranha.")
    print("Sua capa era de couro negro, com runas vermelhas que pulsavam levemente ao toque. Ao abri-lo, uma página chamou minha atenção:")
    print('\n"Aqueles que lerem estas palavras sob a lua sangrenta serão julgados. O portal se abrirá, e o destino os aguardará além do véu."\n')
    time.sleep(5)
    print("Antes que eu pudesse reagir, as runas brilharam com intensidade, e o chão sob meus pés desapareceu.")
    print("Um vórtice de luz e sombras me engoliu, e o mundo ao meu redor se despedaçou em fragmentos de realidade.")
    time.sleep(5)
    print("Quando abri os olhos, estava deitado em um campo de flores azuis, sob um céu com dois sóis.")
    time.sleep(5)
    print('O ar cheirava a magia, e no horizonte, torres cristalinas brilhavam ao longe. Um sistema de mensagens apareceu diante de meus olhos, como se fosse parte de um jogo:\n')
    print("| » Bem-vindo, Viajante, ao Mundo de Aldurian!")
    print(f"| » Status atual: Humano ({player['classe']})")
    print("| » Objetivo: Encontre seu destino ou pereça nas terras esquecidas.\n")
    time.sleep(5)
    input("\nPressione ENTER para continuar")
    print("\nVocê desperta em um santuário antigo, com símbolos místicos por toda parte...")
    print("Uma névoa azulada dança ao seu redor. Um velho encapuzado se aproxima.")
    time.sleep(5)
    print(f"\nEldramar: Saudações, {player['nome']}. Eu sou Eldramar, o guardião do véu entre os mundos.")
    print("Eldramar: Você foi trazido a Aldurian por forças que nem mesmo eu compreendo por completo.")
    time.sleep(5)
    while True:
        print("\nO que você deseja fazer?")
        print("1. Fazer perguntas sobre Aldurian")
        print("2. Levantar-se e observar o local")
        print("3. Ficar em silêncio")

        escolha = input("Digite o número da sua ação: ")
        if escolha == "1":
            print("\nEldramar: Aldurian é um mundo fragmentado entre luz e trevas. Você terá um papel crucial aqui.")
        elif escolha == "2":
            print("\nVocê se levanta. As paredes do templo estão cobertas de inscrições antigas.")
        elif escolha == "3":
            print("\nVocê apenas observa em silêncio. Eldramar entende sua hesitação.")
            time.sleep(5)
            print(f"Eldramar: Entendo o seu silêncio {player['nome']} mas quero saber mais sobre sua personalidade\n")
            time.sleep(5)
            print("Eldramar: Você vê uma criança furtando uma maçã.")
            print("1. Repreende a criança e devolve a maçã ao dono.")
            print("2. Dá outra maçã à criança e segue seu caminho.")
            print("3. Usa a distração para furtar também.")

            escolha1 = input("Eldramar: O que faz?: ").lower()
            if escolha1 == "1":
                player["personalidade"] = "Justo"
            elif escolha1 == "2":
                player["personalidade"] = "Empático"
            elif escolha1 == "3":
                player["personalidade"] = "Caótico"
            else:
                print("Escolha inválida. Assumindo natureza misteriosa.")
                player["personalidade"] = "Enigmático"
                time.sleep(5)
            print(f"\nEldramar: Interessante... Vejo que você é {player['personalidade']}.\n")
            break
        else:
            print("Escolha inválida. Tente novamente.")

    print("\nVocê se pergunta em como Eldramar sabe o seu nome.\n")
    time.sleep(5)
    print(f"{player['nome']}: Como você sabe meu nome?")
    time.sleep(5)
    print("\n(O mago sorri, lento, como um gato diante de um rato.)\n")
    time.sleep(5)
    print("Eldramar: Você acha que foi um acidente? Que caiu aqui por... sorte?")
    time.sleep(5)
    print("\n(Ele dá um passo à frente, e as sombras ao seu redor parecem se esticar.)\n")
    time.sleep(5)
    print("Eldramar: Nomes têm poder, jovem. E o seu... ecoou através do Véu.")
    time.sleep(5)
    print(f"{player['nome']}: Isso não explica nada. Quem é você? O que quer?")
    time.sleep(5)
    print("\n(Eldramar ergue uma mão enrugada, e um globo de névoa escura se forma entre seus dedos, mostrando flashes do passado: a biblioteca, o grimório, o portal.)\n")
    time.sleep(5)
    print("Eldramar: Sou o último dos Vigias Eternos. Acompanhei o nascimento deste mundo, e talvez seu fim.")
    time.sleep(5)
    print("Eldramar: (O globo se desfaz, e seu sorriso some.) Agora resta saber se você é forte o bastante para descobrir por quê.")
    time.sleep(5)
    print(f"\n(Um silêncio pesado cai. {player['nome']} sente um frio na nuca.)\n")
    time.sleep(5)
    print(f"{player['nome']}: Isso é uma ameaça?")
    time.sleep(5)
    print("\n(O mago vira as costas, suas vestes arrastando-se como fumaça.)\n")
    time.sleep(5)
    print("Eldramar: É um fato. Mas não se preocupe... por enquanto. (Ele olha por cima do ombro, os olhos faiscando.) A masmorra fará pior.")
    time.sleep(5)
    input("\nPressione ENTER para continuar")
    print("\nEldramar: 'Antes de seguir adiante, responda ao seguinte enigma. Caso falhe, as criaturas da sombras virão cobrar o preço...'\n")
    time.sleep(5)
    print(f"(E antes que {player['nome']} possa responder, Eldramar se dissolve nas sombras, deixando apenas um riso ecoando nas paredes de pedra.)\n")
    time.sleep(5)
    print("Voz sussurrante: 'Sou algo que você usa todos os dias, mas não pode tocar ou segurar. Posso ser curto ou muito longo,e mudo a cada instante, sem parar.'")
    time.sleep(4)
    print("Voz sussurrante: 'O que sou eu?'")   
    resposta = input("Sua resposta: ").strip().lower()

    if "tempo" in resposta or "o tempo" in resposta:
        time.sleep(5)
        print(f"\nVoz sussurrante: 'Muito bem... Você poderá continuar sua jornada.'")
    else:
        time.sleep(5)
        print(f"\nVoz sussurrante: 'Errado... As sombras não perdoa a ignorância. Prepare-se para lutar!'\n")
        from combate import combate
        inimigos = [
            {"nome": "Sombra Goblin", "classe": "Guerreiro", "vida": 30, "força": 32, "defesa": 30, "nivel":1},
            {"nome": "Sombra Goblin", "classe": "Guerreiro", "vida": 35, "força": 36, "defesa": 30, "nivel":2}
        ]
        combate(player, inimigos)

    print(f"\nVoz sussurrante: 'Agora siga, {player['classe']}. Aldurian te aguarda.'")
    time.sleep(5)
    print("Você caminha por entre árvores milenares até avistar a entrada da Masmorra do Fim...\n")
    input("Pressione ENTER para continuar\n")
    limpar_terminal()