import pygame

def tocar_musica():
    pygame.mixer.init()
    pygame.mixer.music.load("game_sound/sound_game.mp3")
    pygame.mixer.music.set_volume(0.3) #30% do audio
    pygame.mixer.music.play(-1)  # Loop infinito

def parar_musica():
    pygame.mixer.music.stop()

# Quando começa o nível 8
tocar_musica()

# (aqui seu jogo roda normalmente)

# Quando o nível 8 termina
parar_musica()
