import random
import time

def introducao_sala_de_espelhos():
    print("\n--- Nivel 2: O Salão de Espelhos ---")
    time.sleep(3)
    quebra_cabeca()

    print("Você avança pelo corredor e se vê em um vasto salão coberto de espelhos.")
    time.sleep(3)
    print("Cada espelho refelte não apenas a sua imagem, mas também as partes mais sombrias do seu ser.")
    time.sleep(2)
    print("\n Ao entrar, ouve uma risada familiar e vê uma imagem distorcida de ci mesmo, chamando para um duelo")
    time.sleep(3)

def quebra_cabeca():
    time.sleep(3)
    print("\nVocê encontrou uma tabua antiga com a seguinte escrita.")
    print("Você precisa resolver o enigma refletindo a luz corretamente nos espelhos para abrir a passagem.\n")
    time.sleep(2)
    print("1. Inclinar o espelho para a esquerda")
    print("2. Inclinar o espelho para a direita")
    print("3. Girar o espelho para cima")
    print("4. Girar o espelho para baixo")

    resposta_correta = "2"
    tentativa = input("\nEscolha a opção correta para reflitir a luz e abrir a passagem: ")

    if tentativa == resposta_correta:
        print("\nVocê refletiu a luz corretamente e a passagem se abre!")
        time.sleep(2)
    else:
        print("\nVocê errou! Tente novamente.")
        return quebra_cabeca()
    
def combate_clone(player):
    print("\n Você esta em combate com Clone Sombrio")
    time.sleep(2)
    clone = player.copy()  # Cria um clone com as mesmas características do jogador
    clone["nome"] = "Clone Sombrio"
    clone["vida"] = player["vida"]
    clone["força"] = player["força"]
    clone["magia"] = player["magia"]
    clone["defesa"] = player["defesa"]

    print(f"\n{player['nome']} enfrenta seu Clone Sombrio!")
    while player["vida"] > 0 and clone["vida"] > 0:
        print(f"\n{player['nome']}: Vida = {player['vida']}, Força = {player['força']}, Magia = {player['magia']}, Defesa = {player['defesa']}")
        print(f"{clone['nome']}: Vida = {clone['vida']}, Força = {clone['força']}, Magia = {clone['magia']}, Defesa = {clone['defesa']}")

        print("Escolha sua ação:")
        print("1. Atacar")
        print("2. Usar item")
        print("3. Usar habilidade especial")

        acao = input("Digite o número da ação escolhida: ")

        if acao == "1":
            # Ataca o clone
            dano = max(0, player["força"] - random.randint(5, 10))
            clone["vida"] -= dano
            print(f"Você atacou {clone['nome']} causando {dano} de dano!")
            if clone["vida"] <= 0:
                print(f"{clone['nome']} foi derrotado!")
                break
        elif acao == "2":
            print(f"Você usou sua habilidade: {player['habilidade']}")
            # Implementação das habilidades especiais de cada classe
            if player["classe"] == "Mago":
                dano_magia = random.randint(20, 40)
                clone["vida"] -= dano_magia
                print(f"Bola de Fogo acertou {clone['nome']} causando {dano_magia} de dano!")
            elif player["classe"] == "Paladino":
                cura = random.randint(20, 40)
                player["vida"] += cura
                print(f"Benção divina curou você em {cura} pontos de vida!")
            elif player["classe"] == "Arqueiro":
                dano_tiro = random.randint(30, 50)
                clone["vida"] -= dano_tiro
                print(f"Tiro Certeiro acertou {clone['nome']} causando {dano_tiro} de dano!")
            elif player["classe"] == "Guerreiro":
                dano_decaptacao = random.randint(40, 60)
                clone["vida"] -= dano_decaptacao
                print(f"Decapitação atingiu {clone['nome']} causando {dano_decaptacao} de dano!")
            if clone["vida"] <= 0:
                print(f"{clone['nome']} foi derrotado!")
                break
        elif acao == "3":
            if player["itens"]["poção de cura"] > 0:
                cura = random.randint(30, 50)
                player["vida"] += cura
                player["itens"]["poção de cura"] -= 1
                print(f"Você usou uma poção de cura e recuperou {cura} pontos de vida!")
            else:
                print("Você não tem mais poções de cura!")
        else:
            print("Ação inválida! Escolha uma ação válida.")
            continue

        # Ataque do clone no jogador
        dano_clone = max(0, clone["força"] - player["defesa"])
        player["vida"] -= dano_clone
        print(f"\n{clone['nome']} atacou você causando {dano_clone} de dano!")

        if player["vida"] <= 0:
            print("\nVocê foi derrotado pelo seu clone! Game over!")
            break

def conclusao_nivel():
    print("\n--- Conclusão do Nível ---")
    time.sleep(2)
    print("\nVocê venceu o Salão dos Espelhos e se provou digno de continuar sua jornada.")
    print("Com o clone derrotado, você se sente mais forte e determinado a enfrentar os desafios à frente.")
    print("\nVocê recebe uma recompensa: \n- Espelho Mágico (Usado para refletir ataques mágicos)")
    print("\nPrepare-se para o próximo nível!")

# Função principal para o Nível 2
def nivel_2(player):
    introducao_sala_de_espelhos()
    combate_clone(player)
    if player["vida"] > 0:
        conclusao_nivel()
    else:
        print("\nVocê não sobreviveu aos desafios do Salão dos Espelhos.")

# Função para iniciar o jogo a partir do nível 2


# Inicia o jogo diretamente no nível 2
if __name__ == "__main__":
    nivel_2()