# #main.py

# import pygame
# import sys
# from character_selection import character_selection_loop
# from functions import spawn_obstacle, update_obstacle, draw_text

# # Inicialização
# pygame.init()

# # Tela
# WIDTH, HEIGHT = 1000, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Jogo do Desvio com Obstáculo Girando")

# # Relógio
# clock = pygame.time.Clock()
# FPS = 60

# # Cores
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)

# # Fonte
# font = pygame.font.SysFont(None, 40)

# # ==== TELA DE SELEÇÃO DE PERSONAGEM ====
# selected_character = character_selection_loop()

# # Carrega imagens com base na escolha do personagem
# background = selected_character["background_img"]
# player_img = selected_character["player_img"]
# obstacle_img = selected_character["obstacle_img"]

# # Carregando e redimensionando imagens
# background = pygame.image.load(bg_path).convert()

# player_img_original = pygame.image.load(player_path).convert_alpha()
# player_img = pygame.transform.scale(player_img_original, (160, 160))
# player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Começa no centro da tela

# obstacle_img_original = pygame.image.load(obstacle_path).convert_alpha()
# obstacle_img = pygame.transform.scale(obstacle_img_original, (80, 80))

# # Obstáculo único
# obstacle = None

# # Variáveis para controle da velocidade e spawn
# obstacle_speed = 5.0  # Começa devagar
# obstacle_speed_increment = 0.33
# obstacle_rotation_speed = 2  # graus por frame

# score = 0

# def show_game_over():
#     draw_text(screen, "GAME OVER - Clique para jogar novamente", font, RED, WIDTH // 2, HEIGHT // 2, center=True)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Loop principal
# running = True
# while running:
#     clock.tick(FPS)

#     screen.blit(background, (0, 0))

#     # Eventos
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Movimento total com o mouse
#     mouse_x, mouse_y = pygame.mouse.get_pos()
#     player_rect.center = (mouse_x, mouse_y)

#     # Impede sair da tela
#     if player_rect.left < 0:
#         player_rect.left = 0
#     if player_rect.right > WIDTH:
#         player_rect.right = WIDTH
#     if player_rect.top < 0:
#         player_rect.top = 0
#     if player_rect.bottom > HEIGHT:
#         player_rect.bottom = HEIGHT

#     screen.blit(player_img, player_rect)

#     # Spawna obstáculo se não tiver um
#     if obstacle is None:
#         obstacle = spawn_obstacle(obstacle_img, WIDTH)

#     # Atualiza obstáculo
#     rotated_img, rotated_rect = update_obstacle(obstacle, obstacle_speed, obstacle_rotation_speed)
#     screen.blit(rotated_img, rotated_rect)
#     obstacle["rect"] = rotated_rect

#     # Checa colisão
#     if player_rect.colliderect(rotated_rect):
#         show_game_over()
#         pygame.quit()
#         sys.exit()

#     # Saiu da tela
#     if rotated_rect.top > HEIGHT:
#         score += 1
#         obstacle = None
#         obstacle_speed += obstacle_speed_increment

#     # Score
#     draw_text(screen, f"Score: {score}", font, WHITE, 20, 20)

#     pygame.display.flip()

#BACKUP

# main.py
# main.py

import pygame
import sys
import time
from functions import spawn_obstacle, update_obstacle, draw_text
from voice_utils import ouvir_comando

# Inicialização
pygame.init()

# Tela
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo do Desvio com Obstáculo Girando")

# Relógio
clock = pygame.time.Clock()
FPS = 60

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Fonte
font = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 30)

def contagem_regressiva():
    for i in range(3, 0, -1):
        screen.fill((0, 0, 0))
        draw_text(screen, str(i), font, WHITE, WIDTH // 2, HEIGHT // 2, center=True)
        pygame.display.flip()
        time.sleep(1)

def show_game_over():
    draw_text(screen, "GAME OVER - Clique para jogar novamente", font, RED, WIDTH // 2, HEIGHT // 2, center=True)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

def esperar_comando_iniciar():
    # Tela inicial com background, título e texto
    screen.fill((0, 0, 0))
    draw_text(screen, "Jogo do Desvio", font, WHITE, WIDTH // 2, HEIGHT // 3, center=True)
    draw_text(screen, "Fale 'bora lá' para começar", small_font, WHITE, WIDTH // 2, HEIGHT // 2, center=True)
    pygame.display.flip()

    while True:
        comando = ouvir_comando()
        if "bora lá" in comando.lower():
            return

def esperar_comando_personagem(personagens_disponiveis):
    # Exibe a lista dos personagens disponíveis
    screen.fill((0, 0, 0))
    draw_text(screen, "Diga o nome do personagem", font, WHITE, WIDTH // 2, HEIGHT // 5, center=True)
    y_start = HEIGHT // 3
    for i, personagem in enumerate(personagens_disponiveis):
        draw_text(screen, personagem, small_font, WHITE, WIDTH // 2, y_start + i * 40, center=True)
    pygame.display.flip()

    while True:
        comando = ouvir_comando()
        comando_lower = comando.lower()
        for personagem in personagens_disponiveis:
            if personagem.lower() in comando_lower:
                return personagem

def carregar_imagens_personagem(nome_personagem):
    # Exemplo simples: ajustar para seu modo real de carregar imagens
    # Retorne um dict com background_img, player_img, obstacle_img já carregadas como Surface
    # Aqui só um exemplo fictício:
    if nome_personagem == "Rangx'er":
        bg = pygame.image.load("assets/ranger_bg.png").convert()
        player = pygame.image.load("assets/ranger_player.png").convert_alpha()
        obstacle = pygame.image.load("assets/ranger_obstacle.png").convert_alpha()
    elif nome_personagem == "Mage":
        bg = pygame.image.load("assets/mage_bg.png").convert()
        player = pygame.image.load("assets/mage_player.png").convert_alpha()
        obstacle = pygame.image.load("assets/mage_obstacle.png").convert_alpha()
    else:
        # Personagem default
        bg = pygame.Surface((WIDTH, HEIGHT))
        bg.fill((0, 0, 0))
        player = pygame.Surface((160, 160))
        player.fill((255, 255, 255))
        obstacle = pygame.Surface((80, 80))
        obstacle.fill((255, 0, 0))

    return {
        "background_img": bg,
        "player_img": player,
        "obstacle_img": obstacle,
    }


# === INÍCIO DO PROGRAMA ===

# Passo 1: Tela inicial e comando "bora lá"
esperar_comando_iniciar()

# Passo 2: Seleção do personagem por voz
personagens_disponiveis = ["Ranger", "Mage", "Warrior"]  # Ajuste aqui conforme personagens reais
nome_personagem = esperar_comando_personagem(personagens_disponiveis)

# Carregar imagens do personagem escolhido
selected_character = carregar_imagens_personagem(nome_personagem)

# Pega imagens
background = selected_character["background_img"]
player_img_original = selected_character["player_img"]
obstacle_img_original = selected_character["obstacle_img"]

# Redimensiona
player_img = pygame.transform.scale(player_img_original, (160, 160))
player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

obstacle_img = pygame.transform.scale(obstacle_img_original, (80, 80))

# Variáveis do jogo
obstacle = None
obstacle_speed = 5.0
obstacle_speed_increment = 0.33
obstacle_rotation_speed = 2
score = 0

# Contagem regressiva antes de começar o jogo
contagem_regressiva()

# Loop principal
running = True
while running:
    clock.tick(FPS)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento do jogador
    mouse_x, mouse_y = pygame.mouse.get_pos()
    player_rect.center = (mouse_x, mouse_y)
    player_rect.clamp_ip(screen.get_rect())

    screen.blit(player_img, player_rect)

    # Obstáculo
    if obstacle is None:
        obstacle = spawn_obstacle(obstacle_img, WIDTH)

    rotated_img, rotated_rect = update_obstacle(obstacle, obstacle_speed, obstacle_rotation_speed)
    screen.blit(rotated_img, rotated_rect)
    obstacle["rect"] = rotated_rect

    if player_rect.colliderect(rotated_rect):
        show_game_over()
        obstacle = None
        obstacle_speed = 5.0
        score = 0

    if rotated_rect.top > HEIGHT:
        score += 1
        obstacle = None
        obstacle_speed += obstacle_speed_increment

    draw_text(screen, f"Score: {score}", font, WHITE, 20, 20)

    pygame.display.flip()
