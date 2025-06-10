#assets_config.py

import pygame

pygame.init()
pygame.display.set_mode((1, 1))  # janela mínima só para inicializar o display

def load_image(path, size=None):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, size) if size else img

characters = [
    {
        "id": "player1",
        "name": "Marcio Solo",
        "player_img": load_image("assets/player1.png", (160, 160)),
        "obstacle_img": load_image("assets/obstacle1.png", (80, 80)),
        "background_img": load_image("assets/bg1.jpg")
    },
    {
        "id": "player2",
        "name": "Marcio a Jato",
        "player_img": load_image("assets/player2.png", (160, 160)),
        "obstacle_img": load_image("assets/obstacle2.png", (80, 80)),
        "background_img": load_image("assets/bg2.png")
    },
    {
        "id": "player3",
        "name": "Iron Marcio",
        "player_img": load_image("assets/player3.png", (160, 160)),
        "obstacle_img": load_image("assets/obstacle3.png", (80, 80)),
        "background_img": load_image("assets/bg3.png")
    },
    {
        "id": "player4",
        "name": "Super Marcio",
        "player_img": load_image("assets/player4.png", (160, 160)),
        "obstacle_img": load_image("assets/obstacle4.png", (80, 80)),
        "background_img": load_image("assets/bg4.png")
    }
]
