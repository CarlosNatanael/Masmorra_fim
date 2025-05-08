from utils.combate import combate
from conquistas_imag.sistema_conquistas import mostrar_conquista
import time
import random
import os

def mostrar_status_jogador(player):
    print(f"""
┌───────────────────┬───────────────────┐
│      STATUS       │     ATRIBUTOS     │
├───────────────────┼───────────────────┤
│                   │ Vida:   {player['vida']:<5}     │
│Nível: {player['nivel']:<8}    │ Força:  {player['força']:<5}     │
│XP: {player['xp']:<3}            │ Magia:  {player['magia']:<5}     │
│                   │ Defsa: {player['defesa']:<5}      │
┴───────────────────┴───────────────────┴
""")

def usar_itens(player, pode_usar_chave=True):
    while True:
        mostrar_status_jogador(player)
        print("\nItens disponíveis:")
        for i, (item, qtd) in enumerate(player["itens"].items(), 1):
            print(f"{i}. {item} (x{qtd})")
        print(f"{len(player['itens'])+1}. Continuar adiante")
        
        escolha = input("Escolha o item ou volte: ").strip()
        
        if escolha == str(len(player["itens"])+1):
            return True
        
        try:
            escolha_num = int(escolha)-1
            item = list(player["itens"].keys())[escolha_num]
            
            if player["itens"][item] > 0:
                if item.lower() == "chave de ébano":
                    if not pode_usar_chave:
                        print("\nVocê não pode usar a Chave de Ébano agora!")
                        input("Pressione ENTER para continuar...")
                        continue

                elif item.lower() == "poção de cura":
                    player["vida"] = (player["vida"] + 20)
                    print(f"\nVocê recuperou 20 de vida! ({player['vida']})")
                    player["itens"][item] -= 1
                    input("\nPressione ENTER para continuar...")
                    return True

                else:
                    print("\nEsse item ainda não tem uso definido.")
                    input("\nPressione ENTER para continuar...")
                    return True

            else:
                print("Você não tem mais deste item!")
                input("\nPressione ENTER para continuar...")

        except:
            print("Escolha inválida!")
            input("Pressione ENTER para continuar...")


def tem_chave(player):
    return player["itens"].get("chave de ébano", 0) > 0

def usar_chave(player):
    itens = player.get("itens", {})
    if itens.get("chave de ébano", 0) > 0:
        itens["chave de ébano"] -= 1
        if itens["chave de ébano"] <= 0:
            del itens["chave de ébano"]
        return True
    return False

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def gerar_itens_aleatorios():
    itens_possiveis = ["poção de cura", "poção de força", "poção de defesa"]
    
    itens = [random.choice(itens_possiveis)]
    
    # Chance de itens adicionais (30% para 2 itens, 10% para 3 itens)
    if random.random() < 0.3:
        itens.append(random.choice(itens_possiveis))
    if random.random() < 0.1:
        itens.append(random.choice(itens_possiveis))
    
    return itens

def encontrar_bau(player):
    # 20% de chance de ser um baú mímico
    if random.random() < 0.2:
        print("\nVocê encontra um baú ornamentado... mas algo parece estranho!")
        time.sleep(2)
        print("De repente, o baú se transforma em uma criatura monstruosa!")
        time.sleep(2)
        
        mimico = {
            "nome": "Baú Mímico",
            "classe": "Monstro",
            "vida": 40 + player["nivel"] * 5,
            "força": 30 + player["nivel"] * 3,
            "defesa": 60,
            "magia": 0,
            "habilidade": "Engolir",
            "nivel": player["nivel"] + 2,
            "xp": 50
        }
        
        if combate(player, [mimico]):
            print("\nO mímico se dissolve, revelando itens roubados de outras vítimas!")
            itens = gerar_itens_aleatorios()
            for item in itens:
                player["itens"][item] = player["itens"].get(item, 0) + 1
                print(f"Você encontrou: {item}!")
            mostrar_conquista("devorador_de_mimicos")
        else:
            return False
    else:
        print("\nVocê encontrou um baú antigo!")
        time.sleep(2)
        print("Ao abri-lo, encontra alguns itens úteis...")
        mostrar_conquista("mestre_dos_baús")
        itens = gerar_itens_aleatorios()
        for item in itens:
            player["itens"][item] = player["itens"].get(item, 0) + 1
            print(f"Você encontrou: {item}!")
    
    return True