import sys
import os
import threading
import pygame
from winotify import Notification
from conquistas_imag.conquista import conquistas

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def tocar_som(caminho_som):
    try:
        pygame.mixer.init()
        som = pygame.mixer.Sound(caminho_som)
        som.set_volume(0.7)
        som.play()
        while pygame.mixer.get_busy():  # Espera o som terminar
            pygame.time.delay(100)
    except Exception as e:
        print(f"Erro ao tocar som: {e}")

def mostrar_conquista(nome_conquista):
    dados = conquistas.get(nome_conquista)
    if not dados:
        print(f"Conquista '{nome_conquista}' não encontrada.")
        return

    try:
        # Obtém caminhos absolutos
        icone_path = resource_path(dados["icone"])
        som_path = resource_path(dados["som"])

        # Verifica se arquivos existem
        if not os.path.exists(icone_path):
            print(f"Arquivo de ícone não encontrado: {icone_path}")
        if not os.path.exists(som_path):
            print(f"Arquivo de som não encontrado: {som_path}")

        # Thread para tocar som
        threading.Thread(
            target=tocar_som,
            args=(som_path,),
            daemon=True
        ).start()

        # Notificação
        toast = Notification(
            app_id="Masmorra do Fim",
            title=dados["titulo"],
            msg=dados["descricao"],
            icon=icone_path
        )
        toast.show()

    except Exception as e:
        print(f"Erro ao mostrar conquista: {e}")