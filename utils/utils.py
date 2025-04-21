import os


def usar_itens(player):
    while True:
        print("\nItens disponíveis:")
        for i, (item, qtd) in enumerate(player["itens"].items(), 1):
            print(f"{i}. {item} (x{qtd})")
        print(f"{len(player['itens'])+1}. Voltar")
        
        escolha = input("Escolha o item ou volte: ").strip()
        
        if escolha == str(len(player["itens"])+1):
            return True
        
        try:
            escolha_num = int(escolha)-1
            item = list(player["itens"].keys())[escolha_num]
            
            if player["itens"][item] > 0:
                if item == "poção de cura":
                    player["vida"] = min(player["vida"] + 20, 100)
                    print(f"Você recuperou 20 de vida! ({player['vida']}/100)")
                player["itens"][item] -= 1
                input("Pressione ENTER para continuar...")
                return True
            else:
                print("Você não tem mais deste item!")
        except:
            print("Escolha inválida!")

def tem_chave(player):
    return player["itens"].get("chave de ébano", 0) > 0

def usar_chave(player):
    if tem_chave(player):
        player["itens"]["chave de ébano"] -= 1
        return True
    return False

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')