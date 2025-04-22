def mostrar_status_jogador(player):
    print(f"""\n
┌───────────────────┬───────────────────┐
│      STATUS       │     ATRIBUTOS     │
├───────────────────┼───────────────────┤
│                   │ Vida:   {player['vida']:<5}     │
│Nível: {player['nivel']:<8}    │ Força:  {player['força']:<5}     │
│XP: {player['xp']:<3}            │ Magia:  {player['magia']:<5}     │
│                   │ Defsa: {player['defesa']:<5}      │
┴───────────────────┴───────────────────┴
""")


if __name__ == "__main__":
    jogador_teste = {
        'vida': 10,
        'força': 12,
        'magia': 80,
        'defesa': 50,
        'nivel': 3,
        'xp': 27
    }
    mostrar_status_jogador(jogador_teste)
