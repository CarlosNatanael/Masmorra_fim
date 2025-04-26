import sys
import os
import threading
import pygame
from winotify import Notification
from conquistas_imag.conquista import conquistas

# Função para corrigir o caminho
def get_caminho_arquivo(caminho_relativo):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, caminho_relativo)
    else:
        return os.path.join(os.path.abspath("."), caminho_relativo)

def tocar_som(caminho_som):
    pygame.mixer.init()
    pygame.mixer.music.load(caminho_som)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def mostrar_conquista(nome_conquista):
    dados = conquistas.get(nome_conquista)
    if not dados:
        print(f"Conquista '{nome_conquista}' não encontrada.")
        return

    # Corrige os caminhos
    icone_path = get_caminho_arquivo(dados["icone"])
    som_path = get_caminho_arquivo(dados["som"])

    # Toca o som paralelo
    threading.Thread(target=tocar_som, args=(som_path,)).start()

    # Mostra a notificação
    toast = Notification(
        app_id="Masmorra do Fim",
        title=dados["titulo"],
        msg=dados["descricao"],
        icon=icone_path
    )
    toast.show()

# Teste rápido
if __name__ == "__main__":
    mostrar_conquista("guardiao_lei")
