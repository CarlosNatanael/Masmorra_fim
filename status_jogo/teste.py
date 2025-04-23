import tkinter as tk
import random

# Dados do jogador
player = {
    "nome": "Cael",
    "classe": "Guerreiro",
    "nivel": 1,
    "vida": 100,
    "força": 20,
    "magia": 5,
    "defesa": 10,
    "xp": 0,
    "xp_proximo_nivel": 100,
    "habilidade": "Decapitação",
    "habilidade_usada": False,
    "itens": {"poção de cura": 2}
}

# Inimigos
inimigos = [
    {"nome": "Goblin", "nivel": 1, "vida": 40, "força": 10, "classe": "Monstro"},
    {"nome": "Esqueleto", "nivel": 2, "vida": 60, "força": 12, "classe": "Monstro"}
]

# Interface Tkinter
root = tk.Tk()
root.title("Masmorra do Fim - Combate")
root.geometry("600x400")

output = tk.Text(root, height=15, width=70)
output.pack()

def atualizar_interface():
    output.delete("1.0", tk.END)
    output.insert(tk.END, f"{player['nome']} - Vida: {player['vida']} | XP: {player['xp']}/{player['xp_proximo_nivel']}\n")
    for inimigo in inimigos:
        output.insert(tk.END, f"{inimigo['nome']} - Vida: {inimigo['vida']}\n")

def atacar():
    if not inimigos:
        output.insert(tk.END, "Todos os inimigos foram derrotados!\n")
        return

    inimigo = random.choice(inimigos)
    dano = max(0, player["força"] - random.randint(0, 3))
    inimigo["vida"] -= dano
    output.insert(tk.END, f"\nVocê atacou {inimigo['nome']} e causou {dano} de dano!\n")
    if inimigo["vida"] <= 0:
        output.insert(tk.END, f"{inimigo['nome']} foi derrotado!\n")
        inimigos.remove(inimigo)
    inimigo_ataca()
    atualizar_interface()

def habilidade():
    if player["habilidade_usada"]:
        output.insert(tk.END, "\nVocê já usou sua habilidade especial nesta batalha!\n")
        return

    dano = player["força"] + random.randint(10, 20)
    for inimigo in inimigos[:]:
        inimigo["vida"] -= dano
        output.insert(tk.END, f"{player['habilidade']} atingiu {inimigo['nome']} e causou {dano} de dano!\n")
        if inimigo["vida"] <= 0:
            output.insert(tk.END, f"{inimigo['nome']} foi derrotado!\n")
            inimigos.remove(inimigo)
    player["habilidade_usada"] = True
    inimigo_ataca()
    atualizar_interface()

def usar_item():
    if player["itens"]["poção de cura"] > 0:
        player["vida"] += 20
        player["itens"]["poção de cura"] -= 1
        output.insert(tk.END, "Você usou uma poção de cura e recuperou 20 de vida.\n")
    else:
        output.insert(tk.END, "Você não tem mais poções.\n")
    inimigo_ataca()
    atualizar_interface()

def inimigo_ataca():
    if inimigos:
        inimigo = random.choice(inimigos)
        dano = max(1, inimigo["força"] - (player["defesa"] // 2))
        player["vida"] -= dano
        output.insert(tk.END, f"{inimigo['nome']} atacou você e causou {dano} de dano!\n")
        if player["vida"] <= 0:
            output.insert(tk.END, "\n💀 Você foi derrotado! 💀\n")

# Botões de ação
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Atacar", command=atacar).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Habilidade Especial", command=habilidade).grid(row=0, column=1, padx=10)
tk.Button(frame, text="Usar Item", command=usar_item).grid(row=0, column=2, padx=10)

atualizar_interface()
root.mainloop()
