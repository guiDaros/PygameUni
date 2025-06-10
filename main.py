import pygame
import sys
import time
from functions import spawn_obstacle, update_obstacle, draw_text
from voice_utils import ouvir_comando
from assets_config import characters

# Inicialização
pygame.init()

# Tela
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo do Pitt")

# Relógio
clock = pygame.time.Clock()
FPS = 60

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (30, 30, 30)

# Fontes
font = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 30)

def contagem_regressiva():
    for i in range(3, 0, -1):
        screen.fill((0, 0, 0))
        draw_text(screen, str(i), font, WHITE, WIDTH // 2, HEIGHT // 2, center=True)
        pygame.display.flip()
        time.sleep(1)

def show_game_over():
    draw_text(screen, "GAME OVER", font, RED, WIDTH // 2, HEIGHT // 3, center=True)
    pygame.draw.rect(screen, GRAY, (WIDTH//2 - 150, HEIGHT//2, 300, 50))
    pygame.draw.rect(screen, GRAY, (WIDTH//2 - 150, HEIGHT//2 + 70, 300, 50))

    draw_text(screen, "Jogar Novamente", small_font, WHITE, WIDTH//2, HEIGHT//2 + 25, center=True)
    draw_text(screen, "Sair para Tela Inicial", small_font, WHITE, WIDTH//2, HEIGHT//2 + 95, center=True)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if WIDTH//2 - 150 <= x <= WIDTH//2 + 150:
                    if HEIGHT//2 <= y <= HEIGHT//2 + 50:
                        return "retry"
                    elif HEIGHT//2 + 70 <= y <= HEIGHT//2 + 120:
                        return "menu"

def esperar_comando_inicial():
    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, "Bem-vindo ao Jogão Top", font, WHITE, WIDTH // 2, HEIGHT // 3, center=True)
        draw_text(screen, "Diga 'iniciar' para jogar ou 'sair' para fechar", small_font, WHITE, WIDTH // 2, HEIGHT // 2, center=True)
        pygame.display.flip()

        comando = ouvir_comando()
        if "inicia" in comando:
            return "iniciar"
        elif "sair" in comando:
            pygame.quit()
            sys.exit()

def escolher_personagem():
    selecionado = None
    cols = 2
    spacing = 50
    grid_width = 300
    grid_height = 220
    start_x = (WIDTH - (grid_width + spacing) * cols) // 2
    start_y = 100

    while not selecionado:
        screen.fill((0, 0, 0))
        draw_text(screen, "Escolha seu personagem", font, WHITE, WIDTH // 2, 40, center=True)

        rects = []
        for idx, char in enumerate(characters):
            col = idx % cols
            row = idx // cols
            x = start_x + col * (grid_width + spacing)
            y = start_y + row * (grid_height + spacing)

            img = pygame.transform.scale(char["player_img"], (160, 160))
            rect = pygame.Rect(x, y, grid_width, grid_height)
            pygame.draw.rect(screen, GRAY, rect)
            screen.blit(img, (x + (grid_width - 160) // 2, y + 10))
            draw_text(screen, char["name"], small_font, WHITE, x + grid_width // 2, y + 180, center=True)
            rects.append((rect, char))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for rect, char in rects:
                    if rect.collidepoint(x, y):
                        return char

def iniciar_jogo(selected_character):
    background = selected_character["background_img"]
    player_img = selected_character["player_img"]
    obstacle_img = selected_character["obstacle_img"]

    player_img = pygame.transform.scale(player_img, (160, 160))
    obstacle_img = pygame.transform.scale(obstacle_img, (80, 80))
    player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    obstacle = None
    obstacle_speed = 5.0
    obstacle_speed_increment = 0.33
    obstacle_rotation_speed = 2
    score = 0

    contagem_regressiva()

    running = True
    while running:
        clock.tick(FPS)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_rect.center = (mouse_x, mouse_y)
        player_rect.clamp_ip(screen.get_rect())
        screen.blit(player_img, player_rect)

        if obstacle is None:
            obstacle = spawn_obstacle(obstacle_img, WIDTH)

        rotated_img, rotated_rect = update_obstacle(obstacle, obstacle_speed, obstacle_rotation_speed)
        screen.blit(rotated_img, rotated_rect)
        obstacle["rect"] = rotated_rect

        if player_rect.colliderect(rotated_rect):
            resultado = show_game_over()
            if resultado == "retry":
                iniciar_jogo(selected_character)
                return
            elif resultado == "menu":
                return

        if rotated_rect.top > HEIGHT:
            score += 1
            obstacle = None
            obstacle_speed += obstacle_speed_increment

        draw_text(screen, f"Score: {score}", font, WHITE, 20, 20)
        pygame.display.flip()

# === EXECUÇÃO PRINCIPAL ===
while True:
    acao = esperar_comando_inicial()
    if acao == "inicia":
        personagem = escolher_personagem()
        iniciar_jogo(personagem)
