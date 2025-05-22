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

def get_progresso_conquistas(player_class=None):
    """Retorna o progresso incluindo conquistas de classe"""
    total = len(conquistas) - 1  # Exclui a conquista mestre
    desbloqueadas = len(conquistas_desbloqueadas)
    
    # Verifica conquista de classe se fornecida
    if player_class and player_class.lower() in CLASS_FINALE_ACHIEVEMENTS:
        class_achievement = CLASS_FINALE_ACHIEVEMENTS[player_class.lower()]["id"]
        if class_achievement not in conquistas_desbloqueadas:
            total += 1
    
    # Verifica conquista mestre
    if desbloqueadas >= total and "mestre_completo" not in conquistas_desbloqueadas:
        verificar_conquista_mestre()
    
    return f"{desbloqueadas}/{total}"

def mostrar_progresso(player):
    classe = player.get("classe", "")
    if player.get("monarca_sombra", False):
        classe = "Monarca das Sombras"
    
    total = len([a for a in conquistas.values() if not a.get("hidden", False)])
    desbloqueadas = len([a for a in conquistas_desbloqueadas if not conquistas.get(a, {}).get("hidden", False)])
    
    # Verifica conquista de classe pendente
    if classe in CLASS_FINALE_ACHIEVEMENTS:
        class_achievement = CLASS_FINALE_ACHIEVEMENTS[classe]["id"]
        if class_achievement not in conquistas_desbloqueadas:
            total += 1
    
    return f"Conquistas: {desbloqueadas}/{total}"

def resetar_conquistas():
    """Reseta todas as conquistas (para debug)"""
    global conquistas_desbloqueadas
    conquistas_desbloqueadas = set()
    try:
        os.remove(resource_path(SAVE_FILE))
    except FileNotFoundError:
        pass

# Conquistas específicas por classe (adicione ao dicionário conquistas)
CLASS_FINALE_ACHIEVEMENTS = {
    "Mago": {
        "id": "finale_mago",
        "titulo": "Archimago Supremo",
        "descricao": "Completou a masmorra dominando os segredos arcanos com sabedoria e poder.",
        "icone": "conquistas_imag/mago.png",
        "som": "sound/beep3-98810.mp3",
        "dificuldade": "Mago"
    },
    "Guerreiro": {
        "id": "finale_guerreiro",
        "titulo": "Lenda do Aço",
        "descricao": "Venceu com força bruta e honra, provando que a espada é a verdadeira magia.",
        "icone": "conquistas_imag/guerreiro.png",
        "som": "sound/beep3-98810.mp3",
        "dificuldade": "Guerreiro"
    },
    "Paladino": {
        "id": "finale_paladino",
        "titulo": "Cruzado Divino",
        "descricao": "Levou a luz dos deuses às profundezas, purificando a escuridão.",
        "icone": "conquistas_imag/paladino.png",
        "som": "sound/beep3-98810.mp3",
        "dificuldade": "Paladino"
    },
    "Arqueiro": {
        "id": "finale_arqueiro",
        "titulo": "Flecha do Destino",
        "descricao": "Cada flecha foi um verso na epopeia de sua vitória precisa e calculada.",
        "icone": "conquistas_imag/arqueiro.png",
        "som": "sound/beep3-98810.mp3",
        "dificuldade": "Arqueiro"
    },
    "Monarca das Sombras": {
        "id": "finale_monarca",
        "titulo": "Rei das Trevas",
        "descricao": "Abraçou as sombras e ascendeu ao trono de Eldramar como novo monarca.",
        "icone": "conquistas_imag/monarca.png",
        "som": "sound/beep3-98810.mp3",
        "dificuldade": "Lendário"
    },
    "Dev_admin": {
        "id": "finale_dev",
        "titulo": "O Debugador Divino",
        "descricao": "Usou poderes além da compreensão mortal para vencer a masmorra.",
        "icone": "conquistas_imag/dev_admin.png",
        "som": "sound/beep3-98810.mp3",
        "dificuldade": "Divino",
        "hidden": True  # Conquista secreta
    }
}

# Adicione ao dicionário principal de conquistas
for achievement in CLASS_FINALE_ACHIEVEMENTS.values():
    if achievement["id"] not in conquistas:
        conquistas[achievement["id"]] = {
            "nivel": 10,
            "titulo": achievement["titulo"],
            "descricao": achievement["descricao"],
            "icone": achievement["icone"],
            "som": achievement["som"],
            "dificuldade": achievement.get("dificuldade", "Normal"),
            "hidden": achievement.get("hidden", False)
        }

def verificar_final_classe(player_data):
    """
    Verifica e desbloqueia a conquista específica para a classe que completou o jogo
    Inclui tratamento especial para Monarca das Sombras
    """
    classe = player_data.get("classe", "")
    
    # Verificação especial para Monarca
    if player_data.get("monarca_sombra", False) and classe != "Monarca das Sombras":
        classe = "Monarca das Sombras"
    
    if classe in CLASS_FINALE_ACHIEVEMENTS:
        achievement_id = CLASS_FINALE_ACHIEVEMENTS[classe]["id"]
        
        # Verifica se já não tem a conquista
        if achievement_id not in conquistas_desbloqueadas:
            mostrar_conquista(achievement_id)
            
            # Verifica conquista especial para Monarca verdadeiro
            if classe == "Monarca das Sombras" and not player_data.get("transformado", False):
                mostrar_conquista("coroa_trevas")  # Conquista adicional para Monarcas naturais

def mostrar_conquista(nome_conquista):
    """Mostra a notificação com estilos diferentes por tipo de conquista"""
    dados = conquistas.get(nome_conquista)
    if not dados:
        return

    # Configurações especiais por tipo de conquista
    if nome_conquista.startswith("finale_"):
        # Efeitos para conquistas de classe final
        estilo = {
            "bg_color": (20, 20, 40) if "Monarca" not in dados["titulo"] else (40, 10, 30),
            "border_color": (100, 210, 110) if "Monarca" not in dados["titulo"] else (160, 50, 150),
            "title_color": (140, 240, 150) if "Monarca" not in dados["titulo"] else (220, 100, 210),
            "duration": "long",
            "sound": dados["som"]
        }
        
        if nome_conquista == "finale_dev":
            estilo.update({
                "bg_color": (30, 5, 40),
                "border_color": (200, 0, 200),
                "title_color": (255, 50, 255)
            })
    else:
        # Configuração padrão para outras conquistas
        estilo = {
            "bg_color": (30, 30, 40),
            "border_color": (100, 210, 110),
            "title_color": (140, 240, 150),
            "duration": "short",
            "sound": dados["som"]
        }

    # Tocar som em thread separada
    threading.Thread(
        target=tocar_som_estilizado,
        args=(estilo["sound"], estilo.get("volume", 0.7)),
        daemon=True
    ).start()

    # Criar notificação
    toast = Notification(
        app_id="Masmorra do Fim",
        title=dados["titulo"],
        msg=dados["descricao"],
        icon=resource_path(dados["icone"]),
        duration=estilo["duration"]
    )
    
    toast.show()
    conquistas_desbloqueadas.add(nome_conquista)
    salvar_conquistas()

def tocar_som_estilizado(caminho, volume=0.7):
    """Toca o som com tratamento especial para diferentes tipos"""
    try:
        pygame.mixer.init()
        som = pygame.mixer.Sound(resource_path(caminho))
        som.set_volume(volume)
        som.play()
        
        # Mantém o thread vivo enquanto o som toca
        while pygame.mixer.get_busy():
            pygame.time.delay(100)
    except Exception as e:
        print(f"Erro ao tocar som: {e}")

# Carrega as conquistas ao importar o módulo
carregar_conquistas()

__all__ = ['mostrar_conquista', 'get_progresso_conquistas', 'conquistas_desbloqueadas', 'conquistas']