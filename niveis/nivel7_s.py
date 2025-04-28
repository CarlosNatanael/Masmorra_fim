from conquistas_imag.sistema_conquistas import mostrar_conquista
from game_sound.sound import tocar_musica
from game_sound.sound import parar_musica
from utils.combate import combate
import time

def nivel_7_sombra(player):
    tocar_musica()
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
        "nivel": 10,
        "xp": 350,
        "imunidades": ["Trevas"]
    }

    print("A escuridão se contorce ao seu redor, fortalecendo seus músculos, ampliando sua mente.")
    print("Você sente o poder do eclipse fluindo por suas veias.\n")
    time.sleep(2)

    input("Está na hora. Pressione ENTER para esmagar a resistência...")

    if combate(player, [resistencia]):
        mostrar_conquista("quebrador_juramentos")
    else:
        return False

    print("\nAltherion cai de joelhos, a luz de sua armadura se fragmenta como vidro ao vento.\n")
    time.sleep(2)
    print("As sombras entoam um hino fúnebre... e o cetro negro flutua até sua mão.")
    print("Você ergue o Primeiro Decreto:")
    print("\n— Que a verdade seja moldada pela escuridão —\n")
    time.sleep(5)
    print("\nAltherion: (voz trêmula, mas firme) Então este é o seu decreto... Que os ecos da luz o acompanhem até o fim, Monarca.")
    time.sleep(4)
    tocar_musica()
    print("\nAltherion: Eldramar... Ele não forjou esta masmorra. Não é seu criador. É apenas o servo que mantém a fornalha acesa.")
    time.sleep(5)
    print("\nAltherion: E você... (respiração falha) Você não é o herói desta história. Você é o braseiro... o centro do sacrifício.")
    time.sleep(5)
    print("\nAltherion: Cada passo que deu aqui alimentou o fogo. A masmorra não testa — ela consome. Ela molda os escolhidos em armas, ou os reduz a cinzas.")
    time.sleep(5)
    print("\nAltherion: Todos os que caminharam antes de ti tornaram-se parte da fundação... almas diluídas no Éter da Forja.")
    time.sleep(5)
    print("\nAltherion: Mas ouça... há uma rachadura na eternidade. A forja precisa de almas... mas não suporta o fulgor da luz verdadeira.")
    time.sleep(5)
    print("\nAltherion: Destrua o núcleo... leve a luz onde ela jamais tocou... e talvez, só talvez, você verá Eldramar arder em sua própria mentira.")
    time.sleep(5)
    print("\nAltherion começa a desintegrar em fragmentos de cristal dourado, e sua voz enfraquece.")
    print("\nAltherion: (últimas palavras) Corra, tolo... antes que o fogo perceba que você já vê através da fumaça.\n")
    time.sleep(5)
    print("A Cidade dos Espinhos Negros se curva em silêncio, e o eclipse se torna eterno.")
    mostrar_conquista("eclipse_eterno")
    time.sleep(5)
    print("\nVocê cai. A luz retorna... mas o mundo jamais será o mesmo.")
    time.sleep(5)
    print("\nAltherion desaparece nas cinzas do eclipse, levando consigo a última centelha da velha ordem.\n")
    time.sleep(5)
    print("Fim de uma linhagem... e o início do seu reinado.\n")
    time.sleep(5)
    print("Você abre portal: seu caminho leva agora à Forja das Almas.\n")
    time.sleep(5)
    input("Pressione ENTER para continuar\n")
    parar_musica()
    return True