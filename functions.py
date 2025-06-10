#functions.py

import pygame
import random
import math

def spawn_obstacle(obstacle_img, screen_width):
    """Cria um novo obstáculo em uma posição X aleatória no topo da tela."""
    rect = obstacle_img.get_rect()
    rect.x = random.randint(0, screen_width - rect.width)
    rect.y = -rect.height  # Começa acima da tela
    return {
        "image": obstacle_img,
        "rect": rect,
        "angle": 0
    }

def update_obstacle(obstacle, speed, rotation_speed):
    """
    Move o obstáculo para baixo e aplica rotação.
    Retorna a nova imagem rotacionada e o novo retângulo.
    """
    obstacle["angle"] = (obstacle["angle"] + rotation_speed) % 360
    rotated_image = pygame.transform.rotate(obstacle["image"], obstacle["angle"])
    rotated_rect = rotated_image.get_rect(center=obstacle["rect"].center)
    rotated_rect.y += speed
    return rotated_image, rotated_rect

def draw_text(surface, text, font, color, x, y, center=False):
    """Desenha texto na tela."""
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)
