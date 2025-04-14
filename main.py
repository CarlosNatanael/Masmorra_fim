from personagem import escolher_classe
from nivel1 import nivel_um
from nivel2 import nivel_dois
from nivel3 import nivel_tres
from nivel4 import nivel_quatro
from nivel5 import nivel_cinco

def main():
    print("Bem vindo á Masmorra do Fim!")
    jogador = escolher_classe()

    if nivel_um(jogador):
        if nivel_dois(jogador):
            if nivel_tres(jogador):
                if nivel_quatro(jogador):
                    nivel_cinco(jogador)

if __name__ == "__main__":
    main()