import pygame

def desenhar_texto_multilinha(superficie, texto_linhas, fonte, cor, centro_x, start_y, espacamento_linha):
    """
    Desenha várias linhas de texto na superfície.

    Args:
        superficie (pygame.Surface): A superfície onde o texto será desenhado.
        texto_linhas (list): Uma lista de strings, onde cada string é uma linha.
        fonte (pygame.font.Font): A fonte a ser usada.
        cor (tuple): A cor do texto (RGB).
        centro_x (int): A coordenada X central para alinhar o texto.
        start_y (int): A coordenada Y inicial para a primeira linha de texto.
        espacamento_linha (int): O espaçamento em pixels entre as linhas.
    """
    y_offset = start_y
    for linha in texto_linhas:
        texto_renderizado = fonte.render(linha, True, cor)
        texto_rect = texto_renderizado.get_rect(center=(centro_x, y_offset))
        superficie.blit(texto_renderizado, texto_rect)
        y_offset += espacamento_linha

