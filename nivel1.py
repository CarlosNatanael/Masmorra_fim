import time
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def nivel_um(player):
    print("\nEra uma noite chuvosa quando entrei na Biblioteca de Arcanthus, um lugar antigo e abandonado, conhecido apenas por estudiosos de ocultismo.")
    time.sleep(2)
    print("As prateleiras empoeiradas guardavam livros proibidos, manuscritos arcanos e relíquias de eras esquecidas.\n")
    print('Eu, um simples pesquisador de mitos antigos, procurava por um texto chamado "O Grimório dos Reinos Perdidos"')
    print("Um livro que supostamente continha segredos sobre dimensões paralelas. Depois de horas revirando estantes.")
    time.sleep(2)
    print("Encontrei-o escondido atrás de uma cortina de teias de aranha.")
    print("Sua capa era de couro negro, com runas vermelhas que pulsavam levemente ao toque. Ao abri-lo, uma página chamou minha atenção:")
    print('\n"Aqueles que lerem estas palavras sob a lua sangrenta serão julgados. O portal se abrirá, e o destino os aguardará além do véu."\n')
    time.sleep(2)
    print("Antes que eu pudesse reagir, as runas brilharam com intensidade, e o chão sob meus pés desapareceu.")
    print("Um vórtice de luz e sombras me engoliu, e o mundo ao meu redor se despedaçou em fragmentos de realidade.")
    time.sleep(3)
    print("Quando abri os olhos, estava deitado em um campo de flores azuis, sob um céu com dois sóis.")
    time.sleep(1)
    print('O ar cheirava a magia, e no horizonte, torres cristalinas brilhavam ao longe. Um sistema de mensagens apareceu diante de meus olhos, como se fosse parte de um jogo:')
    print("| » Bem-vindo, Viajante, ao Mundo de Aldurian!")
    print(f"| » Status atual: Humano ({player['classe']})")
    print("| » Objetivo: Encontre seu destino ou pereça nas terras esquecidas.\n")
    time.sleep(3)
    print("\nVocê desperta em um santuário antigo, com símbolos místicos por toda parte...")
    print("Uma névoa azulada dança ao seu redor. Um velho encapuzado se aproxima.")
    time.sleep(1)
    print(f"\n🧙‍♂️Eldramar: 'Saudações, {player['nome']}. Eu sou Eldramar, o guardião do véu entre os mundos.'")
    print("🧙‍♂️Eldramar: 'Você foi trazido a Aldurian por forças que nem mesmo eu compreendo por completo.'")
    time.sleep(1)
    while True:
        print("\nO que você deseja fazer?")
        print("1. Fazer perguntas sobre Aldurian")
        print("2. Perguntar quem é Eldramar")
        print("3. Levantar-se e observar o local")
        print("4. Ficar em silêncio")

        escolha = input("Digite o número da sua ação: ")
        if escolha == "1":
            print("\n🧙‍♂️Eldramar: 'Aldurian é um mundo fragmentado entre luz e trevas. Você terá um papel crucial aqui.'")
        elif escolha == "2":
            print("\n🧙‍♂️Eldramar: 'Sou o último dos Vigias Eternos. Acompanhei o nascimento deste mundo, e talvez seu fim.'")
            print(f"🧙‍♂️Eldramar: 'Mas primeiro... preciso entender um pouco sobre você {player['nome']}.'\n")
            time.sleep(1)
            print("🧙‍♂️Eldramar: 'Responda com sinceridade...'\n")
            time.sleep(1)
            print("🧙‍♂️Eldramar: Você vê uma criança furtando uma maçã.")
            print("1. Repreende a criança e devolve a maçã ao dono.")
            print("2. Dá outra maçã à criança e segue seu caminho.")
            print("3. Usa a distração para furtar também.")

            escolha1 = input("🧙‍♂️Eldramar: O que faz?: (1/2/3) ").lower()
            if escolha1 == "1":
                player["personalidade"] = "Justo"
            elif escolha1 == "2":
                player["personalidade"] = "Empático"
            elif escolha1 == "3":
                player["personalidade"] = "Caótico"
            else:
                print("Escolha inválida. Assumindo natureza misteriosa.")
                player["personalidade"] = "Enigmático"
                time.sleep(1)
            print(f"\n🧙‍♂️Eldramar: 'Interessante... Vejo que você é {player['personalidade']}.'\n")
            break
        elif escolha == "3":
            print("\nVocê se levanta. As paredes do templo estão cobertas de inscrições antigas.")
        elif escolha == "4":
            print("\nVocê apenas observa em silêncio. Eldramar entende sua hesitação.")
            time.sleep(1)
            print(f"🧙‍♂️Eldramar: 'Entendo o seu silêncio {player['nome']} mas quero saber mais sobre sua personalidade'\n")
            time.sleep(1)
            print("🧙‍♂️Eldramar: Você vê uma criança furtando uma maçã.")
            print("1. Repreende a criança e devolve a maçã ao dono.")
            print("2. Dá outra maçã à criança e segue seu caminho.")
            print("3. Usa a distração para furtar também.")

            escolha1 = input("🧙‍♂️Eldramar: O que faz?: ").lower()
            if escolha1 == "1":
                player["personalidade"] = "Justo"
            elif escolha1 == "2":
                player["personalidade"] = "Empático"
            elif escolha1 == "3":
                player["personalidade"] = "Caótico"
            else:
                print("Escolha inválida. Assumindo natureza misteriosa.")
                player["personalidade"] = "Enigmático"
                time.sleep(1)
            print(f"\n🧙‍♂️Eldramar: 'Interessante... Vejo que você é {player['personalidade']}.'\n")
            break
        else:
            print("Escolha inválida. Tente novamente.")

    
    time.sleep(1)
    print("🧙‍♂️Eldramar: 'Antes de seguir adiante, responda ao seguinte enigma. Caso falhe, as criaturas da floresta virão cobrar o preço...'\n")
    time.sleep(1)
    print("Enigma: 'Sou mais leve que uma pena, mas nem o homem mais forte consegue me segurar por muito tempo. O que sou?'")
    resposta = input("Sua resposta: ").strip().lower()

    if "respiração" in resposta or "fôlego" in resposta:
        time.sleep(1)
        print("\n🧙‍♂️Eldramar: 'Muito bem... Você poderá continuar sua jornada.'")
    else:
        time.sleep(1)
        print("\n🧙‍♂️Eldramar: 'Errado... A natureza não perdoa a ignorância. Prepare-se para lutar!'")
        from combate import combate
        inimigos = [
            {"nome": "Goblin nv:1", "vida": 30, "força": 10, "defesa": 25},
            {"nome": "Goblin nv:2", "vida": 35, "força": 15, "defesa": 30}
        ]
        combate(player, inimigos)

    print(f"\n🧙‍♂️Eldramar: 'Agora siga, {player['classe']}. Aldurian te aguarda.'")
    time.sleep(1)
    print("Você caminha por entre árvores milenares até avistar a entrada da Masmorra do Fim...\n")
    time.sleep(3)
    limpar_terminal()