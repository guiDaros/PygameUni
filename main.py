import pygame
import random
import math
import datetime
import os
import json # Para salvar e carregar logs em um formato mais robusto

# Importa a função útil do nosso arquivo externo
from recursos.funcoes_uteis import desenhar_texto_multilinha

# --- Inicialização ---
pygame.init()
pygame.font.init()
pygame.mixer.init() # Para sons, se você adicionar depois

# --- Configurações da tela ---
LARGURA_TELA = 1000
ALTURA_TELA = 700
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Sobrevivência Espacial")

# Ícone do jogo (opcional: substitua por um .ico ou .png menor)
try:
    icone = pygame.image.load('recursos/imagens/nave.png')
    pygame.display.set_icon(icone)
except pygame.error:
    print("Aviso: Não foi possível carregar o ícone do jogo. Usando ícone padrão.")

# --- MÚSICA DE FUNDO ---
# ATENÇÃO: Substitua 'recursos/sons/trilha_sonora.mp3' pelo caminho do seu arquivo de música
# Crie a pasta 'recursos/sons/' e coloque seu arquivo lá.
MUSICA_FUNDO_PATH = 'recursos/sons/trilha_sonora.mp3'
try:
    pygame.mixer.music.load(MUSICA_FUNDO_PATH)
    pygame.mixer.music.play(-1) # -1 faz a música tocar em loop infinito
    pygame.mixer.music.set_volume(0.3) # Define o volume da música (0.0 a 1.0)
except pygame.error as e:
    print(f"Erro ao carregar música de fundo: {e}")
    print(f"Verifique se '{MUSICA_FUNDO_PATH}' existe e está no formato correto.")


# --- Cores ---
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 100, 200)
VERMELHO = (200, 0, 0)
VERDE = (0, 200, 0)
CINZA_ESCURO = (50, 50, 50)
CINZA_CLARO = (150, 150, 150)

# --- Fontes ---
FONTE_TITULO = pygame.font.Font(None, 74)
FONTE_PADRAO = pygame.font.Font(None, 36)
FONTE_PEQUENA = pygame.font.Font(None, 24)
FONTE_PAUSE = pygame.font.Font(None, 100)

# --- Variáveis do Jogo ---
PLAYER_NAME = ""
GAME_STATE = "INPUT_NOME" # Estados: INPUT_NOME, BOAS_VINDAS, JOGO, PAUSE, GAME_OVER

# Personagem (Nave Espacial)
try:
    IMAGEM_PERSONAGEM = pygame.image.load('recursos/imagens/player.png').convert_alpha()
    IMAGEM_PERSONAGEM = pygame.transform.scale(IMAGEM_PERSONAGEM, (70, 70))
except pygame.error:
    print("Erro ao carregar imagem do personagem. Usando placeholder.")
    IMAGEM_PERSONAGEM = pygame.Surface((70, 70), pygame.SRCALPHA)
    pygame.draw.polygon(IMAGEM_PERSONAGEM, AZUL, [(35, 0), (0, 70), (70, 70)])

personagem_rect = IMAGEM_PERSONAGEM.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA - 50))

# Fundo
try:
    FUNDO_ESTRELAS = pygame.image.load('recursos/imagens/background.png').convert()
    FUNDO_ESTRELAS = pygame.transform.scale(FUNDO_ESTRELAS, (LARGURA_TELA, ALTURA_TELA))
except pygame.error:
    print("Erro ao carregar imagem de fundo. Usando fundo preto.")
    FUNDO_ESTRELAS = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    FUNDO_ESTRELAS.fill(PRETO)

# Obstáculos (Asteroides)
try:
    IMAGEM_ASTEROIDE = pygame.image.load('recursos/imagens/obstacle.png').convert_alpha()
except pygame.error:
    print("Erro ao carregar imagem do asteroide. Usando placeholder.")
    IMAGEM_ASTEROIDE = pygame.Surface((50, 50), pygame.SRCALPHA)
    pygame.draw.circle(IMAGEM_ASTEROIDE, CINZA_ESCURO, (25, 25), 25)

asteroides = []
ASTEROIDE_INICIAL_VELOCIDADE = 3
ASTEROIDE_VELOCIDADE_MAXIMA = 15
ASTEROIDE_SPAWN_TAXA = 60 # Frames entre spawns (menor = mais frequente)
frame_count = 0
velocidade_aumento_fator = 0.0005 # Aumento da velocidade por frame

# Objeto decorativo (Satélite)
try:
    IMAGEM_SATELITE = pygame.image.load('recursos/imagens/nave.png').convert_alpha()
    IMAGEM_SATELITE = pygame.transform.scale(IMAGEM_SATELITE, (60, 60))
except pygame.error:
    print("Erro ao carregar imagem da nave. Usando placeholder.")
    IMAGEM_SATELITE = pygame.Surface((60, 60), pygame.SRCALPHA)
    pygame.draw.circle(IMAGEM_SATELITE, CINZA_CLARO, (30, 30), 30)
    pygame.draw.line(IMAGEM_SATELITE, AMARELO, (0,30), (60,30), 5)

satelite_x = random.randint(0, LARGURA_TELA - IMAGEM_SATELITE.get_width())
satelite_y = random.randint(0, ALTURA_TELA // 2)
satelite_dx = random.choice([-1, 1]) * 2
satelite_dy = random.choice([-1, 1]) * 2

# Sol Pulsante (Círculo Amarelo)
pos_sol_x = 900
pos_sol_y = 100
raio_sol_base = 40
raio_sol_amplitude = 10
raio_sol_velocidade = 0.05 # Velocidade da pulsação
sol_pulso_tempo = 0

# Placar
score = 0
last_scores = []
LOG_FILE = "log.dat"

# --- Funções do Jogo ---

def carregar_logs():
    """Carrega os últimos logs de partidas do arquivo log.dat."""
    global last_scores
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, 'r') as f:
                lines = f.readlines()
                parsed_logs = []
                for line in lines:
                    log_data = json.loads(line)
                    if 'nome_jogador' not in log_data:
                        log_data['nome_jogador'] = "Desconhecido"
                    parsed_logs.append(log_data)
                last_scores = parsed_logs[-5:] # Pega apenas os 5 últimos
        except (IOError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar logs: {e}. O arquivo pode estar corrompido ou vazio.")
            last_scores = []
    else:
        last_scores = []
    last_scores.sort(key=lambda x: datetime.datetime.strptime(x['data'] + ' ' + x['hora'], '%d/%m/%Y %H:%M:%S'), reverse=True)


def salvar_log(pontuacao_final):
    """Salva a pontuação, data, hora e nome do jogador da partida no arquivo log.dat."""
    timestamp = datetime.datetime.now()
    log_entry = {
        "nome_jogador": PLAYER_NAME, # Adiciona o nome do jogador ao log
        "pontuacao": pontuacao_final,
        "data": timestamp.strftime("%d/%m/%Y"),
        "hora": timestamp.strftime("%H:%M:%S")
    }
    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(log_entry) + '\n')
    carregar_logs() # Recarrega para ter os logs atualizados na tela de Game Over

def desenhar_sol_pulsante():
    """Desenha o círculo amarelo (sol) que pulsa."""
    global sol_pulso_tempo
    raio_atual = raio_sol_base + raio_sol_amplitude * math.sin(sol_pulso_tempo)
    pygame.draw.circle(TELA, AMARELO, (pos_sol_x, pos_sol_y), int(raio_atual))
    sol_pulso_tempo += raio_sol_velocidade
    if sol_pulso_tempo > 2 * math.pi:
        sol_pulso_tempo = 0

def criar_asteroide():
    """Cria um novo asteroide em uma posição aleatória no topo da tela."""
    tamanho = random.randint(30, 80)
    x = random.randint(0, LARGURA_TELA - tamanho)
    y = -tamanho
    velocidade = ASTEROIDE_INICIAL_VELOCIDADE + (score // 100) * 0.5
    velocidade = min(velocidade, ASTEROIDE_VELOCIDADE_MAXIMA)

    asteroide_imagem_redimensionada = pygame.transform.scale(IMAGEM_ASTEROIDE, (tamanho, tamanho))
    asteroides.append({
        "rect": asteroide_imagem_redimensionada.get_rect(topleft=(x, y)),
        "velocidade": velocidade,
        "imagem": asteroide_imagem_redimensionada
    })

def mover_asteroides():
    """Move os asteroides para baixo e remove os que saem da tela."""
    global score
    for asteroide in asteroides[:]:
        asteroide["rect"].y += asteroide["velocidade"]
        if asteroide["rect"].top > ALTURA_TELA:
            asteroides.remove(asteroide)
            score += 10

def verificar_colisoes():
    """Verifica colisões entre o personagem e os asteroides."""
    global GAME_STATE
    for asteroide in asteroides:
        if personagem_rect.colliderect(asteroide["rect"]):
            salvar_log(score)
            GAME_STATE = "GAME_OVER"
            asteroides.clear()
            return True
    return False

def mover_satelite():
    """Move o objeto decorativo (satélite) de forma randômica."""
    global satelite_x, satelite_y, satelite_dx, satelite_dy

    satelite_x += satelite_dx
    satelite_y += satelite_dy

    if satelite_x < 0 or satelite_x > LARGURA_TELA - IMAGEM_SATELITE.get_width():
        satelite_dx *= -1
    if satelite_y < 0 or satelite_y > ALTURA_TELA // 2 - IMAGEM_SATELITE.get_height():
        satelite_dy *= -1

    if random.random() < 0.01:
        satelite_dx = random.choice([-1, 1]) * random.randint(1, 3)
        satelite_dy = random.choice([-1, 1]) * random.randint(1, 3)


def desenhar_elementos_jogo():
    """Desenha todos os elementos do jogo na tela."""
    TELA.blit(FUNDO_ESTRELAS, (0, 0))
    desenhar_sol_pulsante()

    TELA.blit(IMAGEM_SATELITE, (satelite_x, satelite_y))

    for asteroide in asteroides:
        TELA.blit(asteroide["imagem"], asteroide["rect"])

    TELA.blit(IMAGEM_PERSONAGEM, personagem_rect)

    texto_score = FONTE_PADRAO.render(f"Pontuação: {score}", True, BRANCO)
    TELA.blit(texto_score, (10, 10))

    texto_pausa_info = FONTE_PEQUENA.render("Pressione Espaço para Pausar", True, CINZA_CLARO)
    TELA.blit(texto_pausa_info, (texto_score.get_width() + 20, 15))


def desenhar_botao(texto, x, y, largura, altura, cor_normal, cor_hover):
    """Desenha um botão e retorna True se clicado."""
    mouse_pos = pygame.mouse.get_pos()
    clicado = pygame.mouse.get_pressed()[0]

    rect = pygame.Rect(x, y, largura, altura)
    
    if rect.collidepoint(mouse_pos):
        pygame.draw.rect(TELA, cor_hover, rect, border_radius=10)
        if clicado:
            return True
    else:
        pygame.draw.rect(TELA, cor_normal, rect, border_radius=10)

    texto_render = FONTE_PADRAO.render(texto, True, BRANCO)
    texto_rect = texto_render.get_rect(center=rect.center)
    TELA.blit(texto_render, texto_rect)
    return False

# --- Telas do Jogo ---

def tela_input_nome():
    """Tela para o jogador digitar o nome."""
    global PLAYER_NAME, GAME_STATE
    TELA.fill(PRETO)
    
    titulo_render = FONTE_TITULO.render("Bem-vindo, Player!", True, AMARELO)
    titulo_rect = titulo_render.get_rect(center=(LARGURA_TELA // 2, 100))
    TELA.blit(titulo_render, titulo_rect)

    prompt_texto = FONTE_PADRAO.render("Digite seu nome:", True, BRANCO)
    TELA.blit(prompt_texto, (LARGURA_TELA // 2 - prompt_texto.get_width() // 2, 200))

    input_box_rect = pygame.Rect(LARGURA_TELA // 2 - 150, 250, 300, 50)
    pygame.draw.rect(TELA, BRANCO, input_box_rect, 2)
    texto_exibido = FONTE_PADRAO.render(PLAYER_NAME, True, BRANCO)
    TELA.blit(texto_exibido, (input_box_rect.x + 5, input_box_rect.y + 5))

    if PLAYER_NAME and desenhar_botao("Continuar", LARGURA_TELA // 2 - 100, 400, 200, 50, VERDE, AZUL):
        GAME_STATE = "BOAS_VINDAS"


def tela_boas_vindas():
    """Tela de boas-vindas com nome do jogador e explicação do jogo."""
    global GAME_STATE
    TELA.fill(PRETO)
    
    saudacao = FONTE_TITULO.render(f"Bem-vindo(a), {PLAYER_NAME}!", True, AMARELO)
    saudacao_rect = saudacao.get_rect(center=(LARGURA_TELA // 2, 100))
    TELA.blit(saudacao, saudacao_rect)

    explicacao = [
        "Sua missão é pilotar sua armadura tecnologica para esquivar das roçadeiras.",
        "Mova sua armadura usando o mouse apenas no eixo X (esquerda e direita).",
        "Desvie das roçadeiras que os vizinhos estão jogando para aumentar sua pontuação.",
        "A velocidade das roçadeiras aumentará com o tempo.",
        "Pressione ESPAÇO para pausar e retomar o jogo.",
        "GRAXA VÉIA GRAXA VÉIA"
    ]
    
    desenhar_texto_multilinha(TELA, explicacao, FONTE_PADRAO, BRANCO, LARGURA_TELA // 2, 200, 30)

    if desenhar_botao("Iniciar Partida", LARGURA_TELA // 2 - 150, ALTURA_TELA - 100, 300, 70, VERDE, AZUL):
        global score, asteroides, personagem_rect, ASTEROIDE_INICIAL_VELOCIDADE
        score = 0
        asteroides.clear()
        personagem_rect.center = (LARGURA_TELA // 2, ALTURA_TELA - 50)
        ASTEROIDE_INICIAL_VELOCIDADE = 3
        GAME_STATE = "JOGO"


def tela_game_over():
    """Tela de fim de jogo, mostrando Game Over e os últimos scores."""
    global GAME_STATE, score
    TELA.fill(PRETO)

    game_over_texto = FONTE_TITULO.render("GAME OVER", True, VERMELHO)
    game_over_rect = game_over_texto.get_rect(center=(LARGURA_TELA // 2, 100))
    TELA.blit(game_over_texto, game_over_rect)

    final_score_texto = FONTE_PADRAO.render(f"Sua Pontuação: {score}", True, BRANCO)
    final_score_rect = final_score_texto.get_rect(center=(LARGURA_TELA // 2, 180))
    TELA.blit(final_score_texto, final_score_rect)

    historico_titulo = FONTE_PADRAO.render("Últimas Partidas:", True, AMARELO)
    historico_titulo_rect = historico_titulo.get_rect(center=(LARGURA_TELA // 2, 250))
    TELA.blit(historico_titulo, historico_titulo_rect)

    y_offset = 280
    if not last_scores:
        no_scores_text = FONTE_PEQUENA.render("Nenhum registro de partida ainda.", True, CINZA_CLARO)
        TELA.blit(no_scores_text, (LARGURA_TELA // 2 - no_scores_text.get_width() // 2, y_offset))
    else:
        for i, log in enumerate(last_scores):
            log_texto = FONTE_PEQUENA.render(
                f"{i+1}. {log.get('nome_jogador', 'Desconhecido')} - Pontuação: {log['pontuacao']} - Data: {log['data']} - Hora: {log['hora']}",
                True, BRANCO
            )
            log_rect = log_texto.get_rect(center=(LARGURA_TELA // 2, y_offset))
            TELA.blit(log_texto, log_rect)
            y_offset += 30
            if i >= 4:
                break

    # Posições dos botões ajustadas para responsividade
    button_width = 300
    button_height = 70
    button_spacing = 15
    
    # Posição do botão Sair do Jogo (o mais abaixo)
    exit_button_y = ALTURA_TELA - button_height - 20
    
    # Posição do botão Jogar Novamente
    restart_button_y = exit_button_y - button_height - button_spacing
    
    # Botões de reiniciar e sair (agora só clicáveis)
    if desenhar_botao("Jogar Novamente", LARGURA_TELA // 2 - button_width // 2, restart_button_y, button_width, button_height, VERDE, AZUL):
        GAME_STATE = "INPUT_NOME"
        PLAYER_NAME = ""
        score = 0

    if desenhar_botao("Sair do Jogo", LARGURA_TELA // 2 - button_width // 2, exit_button_y, button_width, button_height, CINZA_ESCURO, VERMELHO):
        pygame.quit()
        exit()


# --- Loop Principal do Jogo ---
running = True
clock = pygame.time.Clock()
FPS = 60

carregar_logs()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if GAME_STATE == "INPUT_NOME":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if PLAYER_NAME:
                        GAME_STATE = "BOAS_VINDAS"
                elif event.key == pygame.K_BACKSPACE:
                    PLAYER_NAME = PLAYER_NAME[:-1]
                else:
                    PLAYER_NAME += event.unicode
        elif GAME_STATE == "JOGO":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    GAME_STATE = "PAUSE"
        elif GAME_STATE == "PAUSE":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    GAME_STATE = "JOGO"

    # --- Lógica de Atualização por Estado ---
    if GAME_STATE == "JOGO":
        mouse_x, _ = pygame.mouse.get_pos()
        personagem_rect.centerx = mouse_x
        if personagem_rect.left < 0:
            personagem_rect.left = 0
        if personagem_rect.right > LARGURA_TELA:
            personagem_rect.right = LARGURA_TELA

        frame_count += 1
        spawn_rate_adjusted = max(10, ASTEROIDE_SPAWN_TAXA - int(score * velocidade_aumento_fator * 100))
        if frame_count % spawn_rate_adjusted == 0:
            criar_asteroide()
        
        mover_asteroides()
        mover_satelite()
        verificar_colisoes()

    # --- Renderização por Estado ---
    if GAME_STATE == "INPUT_NOME":
        tela_input_nome()
    elif GAME_STATE == "BOAS_VINDAS":
        tela_boas_vindas()
    elif GAME_STATE == "JOGO":
        desenhar_elementos_jogo()
    elif GAME_STATE == "PAUSE":
        desenhar_elementos_jogo()
        s = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
        s.fill((0, 0, 0, 150))
        TELA.blit(s, (0, 0))

        pause_texto = FONTE_PAUSE.render("PAUSE", True, BRANCO)
        pause_rect = pause_texto.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2))
        TELA.blit(pause_texto, pause_rect)
    elif GAME_STATE == "GAME_OVER":
        tela_game_over()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
