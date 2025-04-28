import pygame

def tocar_musica():
    pygame.mixer.init()
    pygame.mixer.music.load("game_sound/game-over.mp3")
    pygame.mixer.music.play(-1)  # Loop infinito

def parar_musica():
    pygame.mixer.music.stop()

# Quando começa o nível 8
tocar_musica()

# (aqui seu jogo roda normalmente)

# Quando o nível 8 termina
parar_musica()
