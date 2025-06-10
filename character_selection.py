#character_selection.py

import pygame
import sys
from assets_config import characters  # Importa a lista de personagens

pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Selecione seu Personagem")
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()
FPS = 60

# Cores
WHITE = (255, 255, 255)
YELLOW = (255, 255, 100)

# Carrega as imagens redimensionadas
for char in characters:
    image = pygame.transform.scale(char["player_img"], (140, 140))
    char["image"] = image
    char["hover_image"] = pygame.transform.scale(char["player_img"], (180, 180))
    char["rect"] = char["image"].get_rect()


# Define posições em grid 2x2
margin_x, margin_y = 100, 80
spacing_x, spacing_y = 400, 250

for i, char in enumerate(characters):
    row = i // 2
    col = i % 2
    x = margin_x + col * spacing_x
    y = margin_y + row * spacing_y
    char["rect"].topleft = (x, y)

# Função que desenha a tela de seleção
def draw_selection():
    screen.fill((30, 30, 30))
    mouse_pos = pygame.mouse.get_pos()

    for char in characters:
        rect = char["rect"]
        if rect.collidepoint(mouse_pos):
            img = char["hover_image"]
            img_rect = img.get_rect(center=rect.center)
            screen.blit(img, img_rect)
            pygame.draw.rect(screen, YELLOW, img_rect, 3, 10)
        else:
            screen.blit(char["image"], rect)

        # Escreve nome abaixo da imagem
        text = font.render(char["name"], True, WHITE)
        text_rect = text.get_rect(center=(rect.centerx, rect.bottom + 20))
        screen.blit(text, text_rect)

    pygame.display.flip()

# Loop da seleção, retorna o personagem escolhido
def character_selection_loop():
    while True:
        clock.tick(FPS)
        draw_selection()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for char in characters:
                    if char["rect"].collidepoint(pygame.mouse.get_pos()):
                        return char  # Retorna o personagem escolhido
