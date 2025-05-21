import sys
import os
import threading
import pygame
import json
from winotify import Notification
from conquistas_imag.conquista import conquistas

# Variável global para armazenar conquistas desbloqueadas
conquistas_desbloqueadas = set()

def get_app_path():
    """Retorna o caminho correto para salvar arquivos"""
    if getattr(sys, 'frozen', False):
        # Se estiver rodando como executável
        return os.path.dirname(sys.executable)
    else:
        # Se estiver rodando em desenvolvimento
        return os.path.dirname(os.path.abspath(__file__))

# Caminho do arquivo de save (na mesma pasta do executável ou do script)
SAVE_FILE = os.path.join(get_app_path(), 'conquistas_save.json')

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def carregar_conquistas():
    """Carrega as conquistas salvas do arquivo"""
    global conquistas_desbloqueadas
    try:
        # Verifica se o arquivo existe no caminho do executável
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, 'r') as f:
                dados = json.load(f)
                if isinstance(dados, list):
                    conquistas_desbloqueadas = set(dados)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar conquistas: {e}")
        conquistas_desbloqueadas = set()

def salvar_conquistas():
    """Salva as conquistas desbloqueadas no arquivo"""
    try:
        # Garante que o diretório existe
        os.makedirs(os.path.dirname(SAVE_FILE), exist_ok=True)
        
        with open(SAVE_FILE, 'w') as f:
            json.dump(list(conquistas_desbloqueadas), f)
    except Exception as e:
        print(f"Erro ao salvar conquistas: {e}")

def tocar_som(caminho_som):
    try:
        pygame.mixer.init()
        som = pygame.mixer.Sound(resource_path(caminho_som))
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

def verificar_conquista_mestre():
    if len(conquistas_desbloqueadas) == len(conquistas) - 1:  # -1 para não contar a própria conquista mestre
        mostrar_conquista("mestre_completo")

def get_progresso_conquistas():
    """Retorna o progresso e verifica se conquistou tudo"""
    total = len(conquistas) - 1  # Exclui a conquista mestre da contagem
    desbloqueadas = len(conquistas_desbloqueadas)
    
    # Se tem todas (exceto a mestre), adiciona a mestre
    if desbloqueadas >= total and "mestre_completo" not in conquistas_desbloqueadas:
        verificar_conquista_mestre()
    
    return f"{desbloqueadas}/{total}"

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

__all__ = ['mostrar_conquista', 'get_progresso_conquistas', 'conquistas_desbloqueadas', 'conquistas']