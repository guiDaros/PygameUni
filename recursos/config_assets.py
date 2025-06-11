import os
import pygame
from pygame.locals import *

# Configuração de paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECURSOS_DIR = os.path.join(BASE_DIR, 'Recursos')
IMAGENS_DIR = os.path.join(RECURSOS_DIR, 'imagens')

# Paths das imagens
IMAGENS = {
    'background': os.path.join(IMAGENS_DIR, 'background.png'),
    'player': os.path.join(IMAGENS_DIR, 'player.png'),
    'obstacle': os.path.join(IMAGENS_DIR, 'obstacle.png'),
    'nave': os.path.join(IMAGENS_DIR, 'nave.png')
}

def carregar_imagens():
    """Carrega e retorna todas as imagens do jogo"""
    imagens = {}
    
    try:
        # Carrega o fundo (convert() para melhor performance)
        imagens['background'] = pygame.image.load(IMAGENS['background']).convert()
        
        # Carrega o player e obstáculos com alpha (transparência)
        imagens['player'] = pygame.image.load(IMAGENS['player']).convert_alpha()
        imagens['obstacle'] = pygame.image.load(IMAGENS['obstacle']).convert_alpha()
        imagens['nave'] = pygame.image.load(IMAGENS['nave']).convert_alpha()

        
    except Exception as e:
        print(f"Erro ao carregar imagens: {e}")
        # Pode adicionar um fallback aqui (como formas geométricas)
        imagens = None
    
    return imagens