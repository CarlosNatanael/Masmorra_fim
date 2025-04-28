import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Combate RPG - Masmorra do Fim")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (40, 40, 40)
VERMELHO = (200, 0, 0)
VERDE = (0, 200, 0)

# Fonte
fonte = pygame.font.Font(None, 32)

# Variáveis do Console
mensagens = []
entrada = ""
combate_ativo = False

# Jogador e Inimigo
player_max_hp = 100
player_hp = 100
inimigo_max_hp = 60
inimigo_hp = 60

clock = pygame.time.Clock()

def desenhar_console():
    tela.fill(CINZA)

    # Área de mensagens
    y = 150
    for msg in mensagens[-10:]:
        texto = fonte.render(msg, True, BRANCO)
        tela.blit(texto, (20, y))
        y += 30

    # Entrada de texto
    pygame.draw.rect(tela, PRETO, (20, altura - 50, largura - 40, 30))
    texto_entrada = fonte.render(entrada, True, BRANCO)
    tela.blit(texto_entrada, (25, altura - 47))

    # Desenhar barras de vida
    desenhar_barras()

def desenhar_barras():
    # Barra do jogador
    pygame.draw.rect(tela, VERMELHO, (20, 20, 300, 25))  # Barra vazia
    largura_hp = int(300 * (player_hp / player_max_hp))
    pygame.draw.rect(tela, VERDE, (20, 20, largura_hp, 25))  # Barra preenchida
    texto_jogador = fonte.render(f"Você - HP: {player_hp}/{player_max_hp}", True, BRANCO)
    tela.blit(texto_jogador, (330, 20))

    # Barra do inimigo
    pygame.draw.rect(tela, VERMELHO, (20, 60, 300, 25))  # Barra vazia
    largura_hp_inimigo = int(300 * (inimigo_hp / inimigo_max_hp))
    pygame.draw.rect(tela, VERDE, (20, 60, largura_hp_inimigo, 25))  # Barra preenchida
    texto_inimigo = fonte.render(f"Goblin - HP: {inimigo_hp}/{inimigo_max_hp}", True, BRANCO)
    tela.blit(texto_inimigo, (330, 60))

def iniciar_combate():
    mensagens.append("⚔️ Um Goblin Salteador apareceu!")
    mensagens.append(f"🏹 Goblin HP: {inimigo_hp}")
    mensagens.append(f"🛡️ Seu HP: {player_hp}")
    mensagens.append("Ações: [A]tacar [D]efender [I]tem [F]ugir")

def processar_acao(acao):
    global player_hp, inimigo_hp, combate_ativo

    if acao.upper() == "A":
        dano = random.randint(12, 22)
        inimigo_hp -= dano
        mensagens.append(f"💥 Você acertou o Goblin e causou {dano} de dano!")

        if inimigo_hp <= 0:
            mensagens.append("🏆 Você derrotou o Goblin!")
            combate_ativo = False
            return

        inimigo_ataque()

    elif acao.upper() == "D":
        mensagens.append("🛡️ Você se colocou em postura defensiva!")
        dano = random.randint(5, 10) // 2
        player_hp -= dano
        mensagens.append(f"⚡ Goblin atacou, mas você defendeu! Sofreu apenas {dano} de dano.")

    elif acao.upper() == "I":
        mensagens.append("✨ Você usou uma Poção de Cura!")
        cura = random.randint(20, 30)
        player_hp = min(player_max_hp, player_hp + cura)
        mensagens.append(f"❤️ Você recuperou {cura} de HP!")
        inimigo_ataque()

    elif acao.upper() == "F":
        if random.random() < 0.4:
            mensagens.append("🏃 Você fugiu com sucesso!")
            combate_ativo = False
        else:
            mensagens.append("❌ Falha ao tentar fugir!")
            inimigo_ataque()

    else:
        mensagens.append("❓ Comando inválido! Use [A], [D], [I] ou [F].")

def inimigo_ataque():
    global player_hp
    dano = random.randint(8, 16)
    player_hp -= dano
    mensagens.append(f"💢 Goblin desferiu um golpe e causou {dano} de dano!")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                if combate_ativo:
                    processar_acao(entrada)
                else:
                    mensagens.append("⚡ Combate finalizado.")
                entrada = ""
            elif evento.key == pygame.K_BACKSPACE:
                entrada = entrada[:-1]
            else:
                entrada += evento.unicode

    if not combate_ativo:
        iniciar_combate()
        combate_ativo = True

    desenhar_console()
    pygame.display.flip()
    clock.tick(60)
