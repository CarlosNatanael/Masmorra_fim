import sys
import os
import threading
import pygame
from winotify import Notification
from conquistas_imag.conquista import conquistas

# Apenas inicialize o mixer uma vez, de preferência no módulo principal

def get_caminho_arquivo(caminho_relativo):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, caminho_relativo)
    else:
        return os.path.join(os.path.abspath("."), caminho_relativo)

def tocar_som(caminho_som):
    som = pygame.mixer.Sound(caminho_som)
    som.set_volume(0.7)
    som.play()

def mostrar_conquista(nome_conquista):
    dados = conquistas.get(nome_conquista)
    if not dados:
        print(f"Conquista '{nome_conquista}' não encontrada.")
        return

    icone_path = get_caminho_arquivo(dados["icone"])
    som_path = get_caminho_arquivo(dados["som"])

    # Toca o som paralelo sem parar a música
    threading.Thread(target=tocar_som, args=(som_path,), daemon=True).start()

    # Mostra a notificação
    toast = Notification(
        app_id="Masmorra do Fim",
        title=dados["titulo"],
        msg=dados["descricao"],
        icon=icone_path
    )
    toast.show()