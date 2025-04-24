from utils.combate import combate
import time

def nivel_7_sombra(player):
    print("Capítulo 7: O Primeiro Decreto\n")
    time.sleep(2)
    print("A Cidade dos Espinhos Negros silencia.")
    time.sleep(2)
    print("Você caminha até o trono vazio, feito de espelhos quebrados e ossos de reis esquecidos.")
    time.sleep(3)
    
    print("\nAs sombras ao seu redor sussurram em uníssono:")
    print("\"Um novo Monarca ergue-se sob o eclipse...\"")
    time.sleep(3)
    print("E cabe a ele proclamar o Primeiro Decreto.\n")
    time.sleep(3)
    
    print("Mas antes que possa tocar o cetro negro, o chão treme.")
    print("Torres desabam. A luz penetra pelas rachaduras da realidade.")
    time.sleep(3)
    
    print("\nDo alto do firmamento, descem os Guardiões da Luz — os últimos defensores da Masmorra.")
    print("Eles vieram cumprir o Último Decreto: 'Que toda sombra seja extinta.'")
    time.sleep(3)
    
    print("\nLiderados por um Paladino Ancestral com armadura feita de cristal solar, eles brandem a última chama do Éter.")
    print("Seu nome ecoa nos céus: **Altherion, o Guardião da Aurora**.\n")
    time.sleep(3)
    print("Altherion: Vejo que se aliou a ele ser das Trevas, se aliou ao Mago Eldramar.")
    print("Altherion: Para sua infelicidade não permitirei que consigo o decreto do Monarca.")
    time.sleep(3)
    resistencia = {
        "nome": "Altherion Guardiões da Luz",
        "classe": "Paladinos Solares",
        "vida": 200,
        "força": 70,
        "magia": 90,
        "defesa": 80,
        "habilidade": "Purificação",
        "nivel": player["nivel"] + 3,
        "xp": 350,
        "imunidades": ["Trevas"]
    }

    print("A escuridão se contorce ao seu redor, fortalecendo seus músculos, ampliando sua mente.")
    print("Você sente o poder do eclipse fluindo por suas veias.\n")
    time.sleep(2)

    input("Está na hora. Pressione ENTER para esmagar a resistência...")

    if not combate(player, [resistencia]):
        return False

    print("\nAltherion cai de joelhos, e sua luz se apaga pela última vez.")
    time.sleep(2)
    print("As sombras entoam um hino sombrio... e o cetro negro voa até sua mão.")
    print("Você ergue o Primeiro Decreto:")
    print("\n— Que a verdade seja moldada pela escuridão —\n")
    time.sleep(5)
    print("nAltherion : (gargalhada rouca) Você quer mesmo saber a verdade? Então ouça bem, Monarca...")
    print("nAltherion : Eldramar não é o dono desta masmorra - ele é apenas o cozinheiro do banquete.\n")
    time.sleep(5)
    print("nAltherion : E você... (tosse convulsiva) você é o prato principal.")
    print("nAltherion : Cada passo que dá aqui não é progresso - é apenas o fogo da forja crescendo mais forte.")
    time.sleep(5)
    print("nAltherion : Todos que vieram antes de você... (ergue mãos trêmulas) viraram combustível.")
    print("nAltherion : Mas há uma brecha... (voz se torna um sussurro) A forja precisa de almas, mas não suporta a luz de sua própria chama.")
    time.sleep(5)
    print("nAltherion : Destrua o núcleo... (pele começa a descascar) e talvez... talvez você queime Eldramar com seu próprio fogo.")
    print("\nApós isso Altherion começa a desaparecer e lhe deixa uma ultima mensagem....")
    time.sleep(5)
    print("nAltherion : (últimas palavras) Corra, tolo. Antes que ele sinta que você sabe demais...\n")
    print("A Cidade dos Espinhos Negros se curva, e o eclipse nunca mais se desfaz.\n")
    print("\nVocê cai. A luz retorna... mas o mundo nunca será o mesmo.")
    print("Altherion desaparece nas cinzas do eclipse, levando consigo a última esperança.")
    print("Fim de uma linhagem que jamais deveria ter existido...\n")
    print("Você cria um portal para a Forja das Almas...")
    input("\nPressione ENTER para continuar\n")
    return True
