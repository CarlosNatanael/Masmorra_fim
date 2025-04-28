import pygame
import os
import sys

def resource_path(relative_path):
    """Retorna o caminho absoluto do recurso, funciona no PyInstaller e no dev."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def tocar_musica():
    pygame.mixer.init()
    caminho_musica = resource_path("game_sound/game-over.mp3")
    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.set_volume(0.3)  # 30% do volume
    pygame.mixer.music.play(-1)  # Loop infinito

def parar_musica():
    pygame.mixer.music.stop()

# Quando começa o nível 8
tocar_musica()

# (aqui seu jogo roda normalmente)

# Quando o nível 8 termina
parar_musica()
