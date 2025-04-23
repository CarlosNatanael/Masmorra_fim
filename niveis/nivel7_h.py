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
    time.sleep(5)
    escolha = input("Digite o número da sua escolha: ", ["1", "2"])

    if escolha == "1":
        print(f"\n{player["nome"]}: (cauteloso) Você... está vivo?")
        time.sleep(5)
        print("Colecionador de Nomes: Vivo? Morto? São só palavras, e palavras... são minha mercadoria. (estende a mão, palma para cima) Você quer um mapa? Eu vendo.")
        time.sleep(5)
        print(f"\n{player["nome"]}: Que tipo de pagamento você aceita?")
        print("Colecionador de Nomes: Nomes, é claro. O primeiro que você recebeu. O da sua avó? Do seu primeiro amor? Do seu pior inimigo? Cada um abre um caminho diferente...")
        print(f"\n{player["nome"]}: E se eu me recusar?")
        print("""

Colecionador de Nomes: (inclina a cabeça) "Então você ficará mais leve a cada passo. Primeiro esquecerá rostos. Depois, lugares. 
Até que seu próprio reflexo não te reconheça." (balança a lamparina, onde luzes dançam como vagalumes presos) "Já aconteceu com outros."

(Os Afogados Secos emitem um som coletivo, como ossos rangendo.)

        """)
    elif escolha == "2":
        print("\nVocê segue sua própria voz em ecos distantes.")
        time.sleep(5)
        print("De repente, uma sombra toma forma: um fragmento seu, esquecido pelo tempo.")
        time.sleep(5)
        combate(player, "Eco Distorcido", 35, 9)
    
    print("\nEscolha como explorar o labirinto:\n")
    print("1. Falar com o os Afogados Secos")
    print("2. Seguir a própria voz pelos corredores")
    time.sleep(5)
    escolha1 = input("Digite o número da sua escolha: ", ["1", "2"])
    
    if escolha1 == "1":
        print("\nOs cadáveres bebem uma gota de sua água com reverência.")
        time.sleep(5)
        print("Um deles murmura: 'A chave está atrás da sua imagem, mas nunca olhe de frente para ela.'")
        time.sleep(5)
        print("Você se prepara melhor para os enigmas futuros.")
        time.sleep(5)
    elif escolha1 == "2":
        print("\nVocê segue sua própria voz em ecos distantes.")
        time.sleep(5)
        print("De repente, uma sombra toma forma: um fragmento seu, esquecido pelo tempo.")
        time.sleep(5)
        combate(player, "Eco Distorcido", 35, 9)

    print("\nNo sétimo dia, você encontra uma escada espiral descendo lentamente.")
    print("No fundo, uma porta de osso esculpida com seu rosto — jovem de um lado, envelhecido do outro.")
    print("Ela está entreaberta. Algo lá dentro... cheira como sua casa.")