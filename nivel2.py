import random
import time
from combate import combate

def nivel_dois(player):
    print("\n--- Nível 2: O Salão dos Espelhos ---")
    time.sleep(2)
    print("Você entra em uma sala repleta de espelhos altos e antigos.")
    print("Enquanto caminha, você começa a ver reflexos distorcidos... versões corrompidas de si mesmo.")
    time.sleep(3)

    print("\nNo centro do salão há três espelhos com inscrições abaixo:")
    print("1. 'A verdade nem sempre é vista com os olhos.'")
    print("2. 'A imagem que vês é quem você é.'")
    print("3. 'O reflexo invertido é o caminho certo.'")

    escolha = input("Qual espelho você toca? (1/2/3): ").strip()
    while escolha not in ["1", "2", "3"]:
        escolha = input("Escolha inválida. Tente novamente (1/2/3): ").strip()

    if escolha == "3":
        print("\nVocê escolheu sabiamente. Um caminho se abre através do espelho.")
    else:
        print("\nUm clone distorcido de você salta do espelho!")
        clone = {
            "nome": f"Clone Corrompido de {player['nome']}",
            "classe": player["classe"],
            "vida": player["vida"],
            "força": player["força"],
            "magia": player["magia"],
            "defesa": player["defesa"],
            "habilidade": player["habilidade"],
        }
        if not combate(player, [clone]):
            return False

    print("\nVocê atravessa o espelho correto e avança para o próximo nível.")
    return True