# # main.py

# import pygame
# import sys
# import time
# from functions import spawn_obstacle, update_obstacle, draw_text
# from voice_utils import ouvir_comando
# from assets_config import characters

#     selected_character = get_personagem_by_name(nome_personagem)

#     background = selected_character["background_img"]

#     # Inicialização
#     pygame.init()

#     # Tela
#     WIDTH, HEIGHT = 1000, 600
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption("Jogo Top")

#     # Relógio
#     clock = pygame.time.Clock()
#     FPS = 60

#     # Cores
#     WHITE = (255, 255, 255)
#     RED = (255, 0, 0)

#     # Fonte
#     font = pygame.font.SysFont(None, 50)
#     small_font = pygame.font.SysFont(None, 30)

#     def contagem_regressiva():
#         for i in range(3, 0, -1):
#             screen.blit((0, 0))  # ← Aqui está o erro principal
#             draw_text(screen, str(i), font, WHITE, WIDTH // 2, HEIGHT // 2, center=True)
#             pygame.display.flip()
#             time.sleep(1)


#     def show_game_over():
#         draw_text(screen, "GAME OVER - Clique para jogar novamente", font, RED, WIDTH // 2, HEIGHT // 2, center=True)
#         pygame.display.flip()
#         waiting = True
#         while waiting:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 elif event.type == pygame.MOUSEBUTTONDOWN:
#                     waiting = False

#     def esperar_comando_iniciar():
#         # Tela inicial com background, título e texto
#         screen.fill(background, (0, 0, 0))
#         draw_text(screen, "Jogão Top", font, WHITE, WIDTH // 2, HEIGHT // 3, center=True)
#         draw_text(screen, "Fale 'bora lá' para começar", small_font, WHITE, WIDTH // 2, HEIGHT // 2, center=True)
#         pygame.display.flip()

#         while True:
#             comando = ouvir_comando()
#             if "bora lá" in comando.lower():
#                 return

#     def esperar_comando_personagem(personagens_disponiveis):
#         # Exibe a lista dos personagens disponíveis
#         screen.fill((0, 0, 0))
#         draw_text(screen, "Diga o nome do personagem", font, WHITE, WIDTH // 2, HEIGHT // 5, center=True)
#         y_start = HEIGHT // 3
#         for i, personagem in enumerate(personagens_disponiveis):
#             draw_text(screen, personagem, small_font, WHITE, WIDTH // 2, y_start + i * 40, center=True)
#         pygame.display.flip()

#         while True:
#             comando = ouvir_comando()
#             comando_lower = comando.lower()
#             for personagem in personagens_disponiveis:
#                 if personagem.lower() in comando_lower:
#                     return personagem
                
#     personagens_disponiveis = ["Ranger", "Mage", "Warrior"]  # Ajuste aqui conforme personagens reais
#     nome_personagem = esperar_comando_personagem(personagens_disponiveis)

#     def get_personagem_by_name(nome_personagem):
#         for personagem in characters:
#             if personagem["name"].lower() == nome_personagem.lower():
#                 return personagem
#         raise ValueError(f"Personagem com nome '{nome_personagem}' não encontrado.")

                
#     selected_character = get_personagem_by_name(nome_personagem)
#     background = selected_character["background_img"]





#     # === INÍCIO DO PROGRAMA ===

#     # Passo 1: Tela inicial e comando "bora lá"
#     esperar_comando_iniciar()

#     # Passo 2: Seleção do personagem por voz


#     # Carregar imagens do personagem escolhido
#     selected_character = get_personagem_by_name(nome_personagem)  # Corrigir nome da função

#     # Pega imagens
#     background = selected_character["background_img"]
#     player_img_original = selected_character["player_img"]
#     obstacle_img_original = selected_character["obstacle_img"]

#     # Redimensiona
#     player_img = pygame.transform.scale(player_img_original, (160, 160))
#     player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

#     obstacle_img = pygame.transform.scale(obstacle_img_original, (80, 80))

#     # Variáveis do jogo
#     obstacle = None
#     obstacle_speed = 5.0
#     obstacle_speed_increment = 0.33
#     obstacle_rotation_speed = 2
#     score = 0

#     # Contagem regressiva antes de começar o jogo
#     contagem_regressiva()

#     # Loop principal
#     running = True
#     while running:
#         clock.tick(FPS)
#         screen.blit(background, (0, 0))

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         # Movimento do jogador
#         mouse_x, mouse_y = pygame.mouse.get_pos()
#         player_rect.center = (mouse_x, mouse_y)
#         player_rect.clamp_ip(screen.get_rect())

#         screen.blit(player_img, player_rect)

#         # Obstáculo
#         if obstacle is None:
#             obstacle = spawn_obstacle(obstacle_img, WIDTH)

#         rotated_img, rotated_rect = update_obstacle(obstacle, obstacle_speed, obstacle_rotation_speed)
#         screen.blit(rotated_img, rotated_rect)
#         obstacle["rect"] = rotated_rect

#         if player_rect.colliderect(rotated_rect):
#             show_game_over()
#             obstacle = None
#             obstacle_speed = 5.0
#             score = 0

#         if rotated_rect.top > HEIGHT:
#             score += 1
#             obstacle = None
#             obstacle_speed += obstacle_speed_increment

#         draw_text(screen, f"Score: {score}", font, WHITE, 20, 20)

#         pygame.display.flip()


import pygame
import sys
import time
from functions import spawn_obstacle, update_obstacle, draw_text
from voice_utils import ouvir_comando
from assets_config import characters

# === INICIALIZAÇÃO DO PYGAME ===
pygame.init()

# Tela
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Top")

# Relógio
clock = pygame.time.Clock()
FPS = 60

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Fontes
font = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 30)

# === FUNÇÕES AUXILIARES ===

def contagem_regressiva():
    for i in range(3, 0, -1):
        screen.fill((0, 0, 0))  # Corrigido: limpar a tela corretamente
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
    screen.fill((0, 0, 0))
    draw_text(screen, "Jogão Top", font, WHITE, WIDTH // 2, HEIGHT // 3, center=True)
    draw_text(screen, "Fale 'bora lá' para começar", small_font, WHITE, WIDTH // 2, HEIGHT // 2, center=True)
    pygame.display.flip()

    while True:
        comando = ouvir_comando()
        if "bora lá" in comando.lower():
            return

def esperar_comando_personagem(personagens_disponiveis):
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

def get_personagem_by_name(nome_personagem):
    for personagem in characters:
        if personagem["name"].lower() == nome_personagem.lower():
            return personagem
    raise ValueError(f"Personagem com nome '{nome_personagem}' não encontrado.")

# === INÍCIO DO PROGRAMA ===

# Tela inicial com comando de voz
esperar_comando_iniciar()

# Gera lista de nomes reais dos personagens
personagens_disponiveis = [personagem["name"] for personagem in characters]

# Usuário escolhe personagem por voz
nome_personagem = esperar_comando_personagem(personagens_disponiveis)
selected_character = get_personagem_by_name(nome_personagem)

# Pega imagens do personagem
background = selected_character["background_img"]
player_img_original = selected_character["player_img"]
obstacle_img_original = selected_character["obstacle_img"]

# Redimensiona imagens
player_img = pygame.transform.scale(player_img_original, (160, 160))
player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
obstacle_img = pygame.transform.scale(obstacle_img_original, (80, 80))

# Variáveis do jogo
obstacle = None
obstacle_speed = 5.0
obstacle_speed_increment = 0.33
obstacle_rotation_speed = 2
score = 0

# Contagem regressiva
contagem_regressiva()

# === LOOP PRINCIPAL DO JOGO ===
running = True
while running:
    clock.tick(FPS)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento do jogador (mouse)
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
