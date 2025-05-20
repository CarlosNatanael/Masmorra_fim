import sys
import os
import threading
import pygame
import json
from winotify import Notification
from conquistas_imag.conquista import conquistas

# Variável global para armazenar conquistas desbloqueadas
conquistas_desbloqueadas = set()

# Nome do arquivo de save
SAVE_FILE = "conquistas_save.json"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def carregar_conquistas():
    """Carrega as conquistas salvas do arquivo"""
    global conquistas_desbloqueadas
    try:
        with open(resource_path(SAVE_FILE), 'r') as f:
            dados = json.load(f)
            if isinstance(dados, list):
                conquistas_desbloqueadas = set(dados)
    except (FileNotFoundError, json.JSONDecodeError):
        # Arquivo não existe ou está corrompido - começa fresh
        conquistas_desbloqueadas = set()

def salvar_conquistas():
    """Salva as conquistas desbloqueadas no arquivo"""
    try:
        with open(resource_path(SAVE_FILE), 'w') as f:
            json.dump(list(conquistas_desbloqueadas), f)
    except Exception as e:
        print(f"Erro ao salvar conquistas: {e}")

def tocar_som(caminho_som):
    try:
        pygame.mixer.init()
        som = pygame.mixer.Sound(caminho_som)
        som.set_volume(0.7)
        som.play()
        while pygame.mixer.get_busy():
            pygame.time.delay(100)
    except Exception as e:
        print(f"Erro ao tocar som: {e}")

def mostrar_conquista(nome_conquista):
    """Mostra a notificação da conquista e salva no arquivo"""
    global conquistas_desbloqueadas
    
    dados = conquistas.get(nome_conquista)
    if not dados:
        print(f"Conquista '{nome_conquista}' não encontrada.")
        return

    # Adiciona à lista de conquistas
    if nome_conquista not in conquistas_desbloqueadas:
        conquistas_desbloqueadas.add(nome_conquista)
        salvar_conquistas()  # Salva imediatamente

    try:
        icone_path = resource_path(dados["icone"])
        som_path = resource_path(dados["som"])

        if not os.path.exists(icone_path):
            print(f"Arquivo de ícone não encontrado: {icone_path}")
        if not os.path.exists(som_path):
            print(f"Arquivo de som não encontrado: {som_path}")

        threading.Thread(
            target=tocar_som,
            args=(som_path,),
            daemon=True
        ).start()

        toast = Notification(
            app_id="Masmorra do Fim",
            title=dados["titulo"],
            msg=dados["descricao"],
            icon=icone_path
        )
        toast.show()

    except Exception as e:
        print(f"Erro ao mostrar conquista: {e}")

def get_progresso_conquistas():
    """Retorna o progresso no formato 'X/56'"""
    return f"{len(conquistas_desbloqueadas)}/{len(conquistas)}"

def resetar_conquistas():
    """Reseta todas as conquistas (para debug)"""
    global conquistas_desbloqueadas
    conquistas_desbloqueadas = set()
    try:
        os.remove(resource_path(SAVE_FILE))
    except FileNotFoundError:
        pass

# Carrega as conquistas ao importar o módulo
carregar_conquistas()