import pygame
import random
import math
import datetime
import os
import speech_recognition as sr
import pyttsx3
import json # Para salvar e carregar logs em um formato mais robusto

# Importa a função útil do nosso arquivo externo
from recursos.funcoes_uteis import desenhar_texto_multilinha

# --- Inicialização ---
pygame.init()
pygame.font.init()
pygame.mixer.init() # Para sons, se você adicionar depois
engine = pyttsx3.init() # Inicializa o motor de fala

# --- Configurações da tela ---
LARGURA_TELA = 1000
ALTURA_TELA = 700
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Sobrevivência Espacial")

# Ícone do jogo (opcional: substitua por um .ico ou .png menor)
try:
    icone = pygame.image.load('Recursos/imagens/nave.png')
    pygame.display.set_icon(icone)
except pygame.error:
    print("Aviso: Não foi possível carregar o ícone do jogo. Usando ícone padrão.")

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
welcome_speech_played = False # Flag para garantir que a mensagem de boas-vindas da voz só toque uma vez
listening_for_name = False # Flag para indicar que o reconhecimento de voz está ativo
voice_feedback_message = "" # Mensagem para feedback de voz na tela

# Personagem (Nave Espacial)
try:
    IMAGEM_PERSONAGEM = pygame.image.load('recursos/imagens/player.png').convert_alpha()
    IMAGEM_PERSONAGEM = pygame.transform.scale(IMAGEM_PERSONAGEM, (70, 70))
except pygame.error:
    print("Erro ao carregar imagem do personagem. Usando placeholder.")
    # Placeholder se a imagem não for encontrada
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
# O satélite irá se mover de forma randômica
try:
    IMAGEM_SATELITE = pygame.image.load('recursos/imagens/nave.png').convert_alpha()
    IMAGEM_SATELITE = pygame.transform.scale(IMAGEM_SATELITE, (60, 60))
except pygame.error:
    print("Erro ao carregar imagem do satélite. Usando placeholder.")
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
                # Cada linha é um registro JSON
                lines = f.readlines()
                # Parse apenas as 5 últimas linhas se houver mais
                last_scores = [json.loads(line) for line in lines[-5:]]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar logs: {e}. O arquivo pode estar corrompido ou vazio.")
            last_scores = []
    else:
        last_scores = []
    # Garante que os logs sejam ordenados do mais recente para o mais antigo, se necessário
    last_scores.sort(key=lambda x: datetime.datetime.strptime(x['data'] + ' ' + x['hora'], '%d/%m/%Y %H:%M:%S'), reverse=True)


def salvar_log(pontuacao_final):
    """Salva a pontuação, data e hora da partida no arquivo log.dat."""
    timestamp = datetime.datetime.now()
    log_entry = {
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
    # Usa a função seno para um pulso suave
    raio_atual = raio_sol_base + raio_sol_amplitude * math.sin(sol_pulso_tempo)
    pygame.draw.circle(TELA, AMARELO, (pos_sol_x, pos_sol_y), int(raio_atual))
    sol_pulso_tempo += raio_sol_velocidade
    if sol_pulso_tempo > 2 * math.pi: # Reseta o ciclo seno
        sol_pulso_tempo = 0

def criar_asteroide():
    """Cria um novo asteroide em uma posição aleatória no topo da tela."""
    tamanho = random.randint(30, 80)
    x = random.randint(0, LARGURA_TELA - tamanho)
    y = -tamanho # Começa acima da tela
    velocidade = ASTEROIDE_INICIAL_VELOCIDADE + (score // 100) * 0.5 # Aumenta a velocidade com a pontuação
    velocidade = min(velocidade, ASTEROIDE_VELOCIDADE_MAXIMA) # Limita a velocidade máxima

    asteroide_imagem_redimensionada = pygame.transform.scale(IMAGEM_ASTEROIDE, (tamanho, tamanho))
    asteroides.append({
        "rect": asteroide_imagem_redimensionada.get_rect(topleft=(x, y)),
        "velocidade": velocidade,
        "imagem": asteroide_imagem_redimensionada
    })

def mover_asteroides():
    """Move os asteroides para baixo e remove os que saem da tela."""
    global score
    for asteroide in asteroides[:]: # Itera sobre uma cópia para permitir remoção
        asteroide["rect"].y += asteroide["velocidade"]
        # Se o asteroide saiu da tela, remove e aumenta o score
        if asteroide["rect"].top > ALTURA_TELA:
            asteroides.remove(asteroide)
            score += 10 # Aumenta o score por asteroide desviado

def verificar_colisoes():
    """Verifica colisões entre o personagem e os asteroides."""
    global GAME_STATE
    for asteroide in asteroides:
        if personagem_rect.colliderect(asteroide["rect"]):
            salvar_log(score)
            GAME_STATE = "GAME_OVER"
            asteroides.clear() # Limpa asteroides para a próxima partida
            return True
    return False

def mover_satelite():
    """Move o objeto decorativo (satélite) de forma randômica."""
    global satelite_x, satelite_y, satelite_dx, satelite_dy

    satelite_x += satelite_dx
    satelite_y += satelite_dy

    # Inverte a direção se atingir as bordas da tela ou uma área limite
    if satelite_x < 0 or satelite_x > LARGURA_TELA - IMAGEM_SATELITE.get_width():
        satelite_dx *= -1
    if satelite_y < 0 or satelite_y > ALTURA_TELA // 2 - IMAGEM_SATELITE.get_height(): # Limita à metade superior
        satelite_dy *= -1

    # Adiciona uma pequena chance de mudança de direção aleatória
    if random.random() < 0.01: # 1% de chance a cada frame
        satelite_dx = random.choice([-1, 1]) * random.randint(1, 3)
        satelite_dy = random.choice([-1, 1]) * random.randint(1, 3)


def desenhar_elementos_jogo():
    """Desenha todos os elementos do jogo na tela."""
    TELA.blit(FUNDO_ESTRELAS, (0, 0)) # Desenha o fundo
    desenhar_sol_pulsante() # Desenha o sol pulsante

    TELA.blit(IMAGEM_SATELITE, (satelite_x, satelite_y)) # Desenha o satélite

    for asteroide in asteroides:
        TELA.blit(asteroide["imagem"], asteroide["rect"])

    TELA.blit(IMAGEM_PERSONAGEM, personagem_rect)

    # Desenha o placar
    texto_score = FONTE_PADRAO.render(f"Pontuação: {score}", True, BRANCO)
    TELA.blit(texto_score, (10, 10))

    # Mensagem de pausa
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
    """Tela para o jogador digitar o nome e usar reconhecimento de voz."""
    global PLAYER_NAME, GAME_STATE, listening_for_name, voice_feedback_message
    TELA.fill(PRETO)
    
    # Desenha o título
    titulo_render = FONTE_TITULO.render("Bem-vindo, Viajante Espacial!", True, AMARELO)
    titulo_rect = titulo_render.get_rect(center=(LARGURA_TELA // 2, 100))
    TELA.blit(titulo_render, titulo_rect)

    # Campo de entrada de texto
    prompt_texto = FONTE_PADRAO.render("Digite seu nome (ou use a voz):", True, BRANCO)
    TELA.blit(prompt_texto, (LARGURA_TELA // 2 - prompt_texto.get_width() // 2, 200))

    input_box_rect = pygame.Rect(LARGURA_TELA // 2 - 150, 250, 300, 50)
    pygame.draw.rect(TELA, BRANCO, input_box_rect, 2) # Borda do campo
    texto_exibido = FONTE_PADRAO.render(PLAYER_NAME, True, BRANCO)
    TELA.blit(texto_exibido, (input_box_rect.x + 5, input_box_rect.y + 5))

    # Botão para reconhecimento de voz
    if desenhar_botao("Falar Nome", LARGURA_TELA // 2 - 100, 320, 200, 50, AZUL, VERDE):
        listening_for_name = True
        voice_feedback_message = "Ouvindo..."
        if engine._isBusy: # Garante que nada esteja falando antes de um novo prompt
            engine.stop()
        engine.say("Por favor, diga seu nome agora.")
        engine.runAndWait() # Bloqueia brevemente para a fala do prompt

    # Exibe feedback de voz
    if voice_feedback_message:
        feedback_render = FONTE_PEQUENA.render(voice_feedback_message, True, BRANCO)
        feedback_rect = feedback_render.get_rect(center=(LARGURA_TELA // 2, 380))
        TELA.blit(feedback_render, feedback_rect)

    # Botão para continuar (se o nome foi digitado)
    if PLAYER_NAME and desenhar_botao("Continuar", LARGURA_TELA // 2 - 100, 400, 200, 50, VERDE, AZUL):
        GAME_STATE = "BOAS_VINDAS"


def tela_boas_vindas():
    """Tela de boas-vindas com nome do jogador e explicação do jogo."""
    global GAME_STATE, welcome_speech_played
    TELA.fill(PRETO)
    
    saudacao = FONTE_TITULO.render(f"Bem-vindo(a), {PLAYER_NAME}!", True, AMARELO)
    saudacao_rect = saudacao.get_rect(center=(LARGURA_TELA // 2, 100))
    TELA.blit(saudacao, saudacao_rect)

    explicacao = [
        "Sua missão é pilotar sua nave espacial através de um campo de asteroides.",
        "Mova sua nave usando o mouse apenas no eixo X (esquerda e direita).",
        "Desvie dos asteroides que caem para aumentar sua pontuação.",
        "A velocidade dos asteroides aumentará com o tempo.",
        "Pressione ESPAÇO para pausar e retomar o jogo.",
        "Sobreviva o máximo que puder!"
    ]
    
    # Usa a função utilitária para desenhar texto multilinha
    desenhar_texto_multilinha(TELA, explicacao, FONTE_PADRAO, BRANCO, LARGURA_TELA // 2, 200, 30)

    # Botão para iniciar a partida
    if desenhar_botao("Iniciar Partida", LARGURA_TELA // 2 - 150, ALTURA_TELA - 100, 300, 70, VERDE, AZUL):
        # Reinicia o jogo antes de iniciar
        global score, asteroides, personagem_rect, ASTEROIDE_INICIAL_VELOCIDADE
        score = 0
        asteroides.clear()
        personagem_rect.center = (LARGURA_TELA // 2, ALTURA_TELA - 50)
        ASTEROIDE_INICIAL_VELOCIDADE = 3 # Reseta a velocidade inicial dos asteroides
        GAME_STATE = "JOGO"
        welcome_speech_played = False # Reseta a flag para uma possível nova partida

    # Lê a mensagem de boas-vindas APENAS UMA VEZ
    if not welcome_speech_played:
        welcome_text = f"Olá, {PLAYER_NAME}. {explicacao[0]} {explicacao[1]} {explicacao[2]} {explicacao[3]} Para iniciar, clique no botão."
        if engine.isBusy:
            engine.stop()
        engine.say(welcome_text)
        engine.runAndWait()
        welcome_speech_played = True


def tela_game_over():
    """Tela de fim de jogo, mostrando Game Over e os últimos scores."""
    global GAME_STATE, welcome_speech_played
    TELA.fill(PRETO)

    game_over_texto = FONTE_TITULO.render("GAME OVER", True, VERMELHO)
    game_over_rect = game_over_texto.get_rect(center=(LARGURA_TELA // 2, 100))
    TELA.blit(game_over_texto, game_over_rect)

    # Exibe a pontuação final
    final_score_texto = FONTE_PADRAO.render(f"Sua Pontuação: {score}", True, BRANCO)
    final_score_rect = final_score_texto.get_rect(center=(LARGURA_TELA // 2, 180))
    TELA.blit(final_score_texto, final_score_rect)

    # Exibe os últimos 5 registros de partidas
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
                f"{i+1}. Pontuação: {log['pontuacao']} - Data: {log['data']} - Hora: {log['hora']}",
                True, BRANCO
            )
            log_rect = log_texto.get_rect(center=(LARGURA_TELA // 2, y_offset))
            TELA.blit(log_texto, log_rect)
            y_offset += 30
            if i >= 4: # Mostra no máximo 5 registros
                break

    # Botão de Jogar Novamente
    if desenhar_botao("Jogar Novamente", LARGURA_TELA // 2 - 150, ALTURA_TELA - 100, 300, 70, VERDE, AZUL):
        GAME_STATE = "INPUT_NOME" # Volta para a tela de input de nome para novo jogador ou mesmo jogador
        PLAYER_NAME = "" # Limpa o nome para que a tela de input apareça novamente
        score = 0 # Reseta a pontuação
        welcome_speech_played = False # Reseta a flag para que a mensagem de boas-vindas toque na próxima vez
        voice_feedback_message = "" # Limpa feedback de voz

    # Botão de Sair (opcional, para conveniência)
    if desenhar_botao("Sair do Jogo", LARGURA_TELA // 2 - 150, ALTURA_TELA - 40, 300, 50, CINZA_ESCURO, VERMELHO):
        pygame.quit()
        exit()


# --- Loop Principal do Jogo ---
running = True
clock = pygame.time.Clock()
FPS = 60

# Carrega os logs ao iniciar o jogo para a tela de Game Over
carregar_logs()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Manipulação de eventos por estado
        if GAME_STATE == "INPUT_NOME":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if PLAYER_NAME:
                        GAME_STATE = "BOAS_VINDAS"
                elif event.key == pygame.K_BACKSPACE:
                    PLAYER_NAME = PLAYER_NAME[:-1]
                    voice_feedback_message = "" # Limpa feedback ao digitar
                else:
                    PLAYER_NAME += event.unicode
                    voice_feedback_message = "" # Limpa feedback ao digitar
        elif GAME_STATE == "JOGO":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    GAME_STATE = "PAUSE"
        elif GAME_STATE == "PAUSE":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    GAME_STATE = "JOGO"

    # --- Lógica de Atualização por Estado ---
    if GAME_STATE == "INPUT_NOME" and listening_for_name:
        # A lógica de reconhecimento de voz é executada aqui no loop principal
        # para evitar múltiplos cliques no botão "Falar Nome" iniciarem várias instâncias.
        # Ele ainda bloqueia, mas só quando a flag 'listening_for_name' é True.
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                # O prompt de voz já foi dado quando o botão foi clicado
                print("Ouvindo...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3) # Adiciona limite de tempo para frase
            
            player_name_voice = r.recognize_google(audio, language='pt-BR')
            PLAYER_NAME = player_name_voice.strip()
            if engine._isBusy:
                engine.stop()
            engine.say(f"Olá, {PLAYER_NAME}. Nome confirmado.")
            engine.runAndWait()
            voice_feedback_message = f"Nome reconhecido: {PLAYER_NAME}"
            print(f"Nome reconhecido por voz: {PLAYER_NAME}")
            if PLAYER_NAME: # Se o nome foi reconhecido com sucesso
                GAME_STATE = "BOAS_VINDAS"
                listening_for_name = False # Desativa a escuta
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio.")
            voice_feedback_message = "Desculpe, não consegui entender. Tente novamente."
            if engine._isBusy:
                engine.stop()
            engine.say("Desculpe, não consegui entender. Por favor, tente novamente.")
            engine.runAndWait()
            listening_for_name = False # Desativa a escuta para permitir novo clique
        except sr.WaitTimeoutError:
            print("Tempo de espera excedido para reconhecimento de voz.")
            voice_feedback_message = "Nenhum áudio detectado. Tente novamente."
            if engine._isBusy:
                engine.stop()
            engine.say("Tempo esgotado. Por favor, tente novamente.")
            engine.runAndWait()
            listening_for_name = False
        except sr.RequestError as e:
            print(f"Erro no serviço de reconhecimento de voz; {e}")
            voice_feedback_message = f"Erro de serviço: {e}"
            if engine._isBusy:
                engine.stop()
            engine.say("Erro no serviço de reconhecimento de voz. Por favor, verifique sua conexão com a internet.")
            engine.runAndWait()
            listening_for_name = False
        except Exception as e:
            print(f"Ocorreu um erro inesperado no reconhecimento de voz: {e}")
            voice_feedback_message = f"Erro inesperado: {e}"
            if engine._isBusy:
                engine.stop()
            engine.say("Ocorreu um erro inesperado no reconhecimento de voz.")
            engine.runAndWait()
            listening_for_name = False


    if GAME_STATE == "JOGO":
        # Movimento do personagem com o mouse no eixo X
        mouse_x, _ = pygame.mouse.get_pos()
        personagem_rect.centerx = mouse_x
        # Garante que o personagem não saia da tela
        if personagem_rect.left < 0:
            personagem_rect.left = 0
        if personagem_rect.right > LARGURA_TELA:
            personagem_rect.right = LARGURA_TELA

        # Geração de asteroides
        frame_count += 1
        # Ajusta a taxa de spawn baseada na pontuação para aumentar a dificuldade
        # Garante que a taxa de spawn nunca seja muito baixa (não menos que 10 frames)
        spawn_rate_adjusted = max(10, ASTEROIDE_SPAWN_TAXA - int(score * velocidade_aumento_fator * 100))
        if frame_count % spawn_rate_adjusted == 0:
            criar_asteroide()
        
        mover_asteroides()
        mover_satelite()
        verificar_colisoes() # Pode mudar o GAME_STATE para GAME_OVER

    # --- Renderização por Estado ---
    if GAME_STATE == "INPUT_NOME":
        tela_input_nome()
    elif GAME_STATE == "BOAS_VINDAS":
        tela_boas_vindas()
    elif GAME_STATE == "JOGO":
        desenhar_elementos_jogo()
    elif GAME_STATE == "PAUSE":
        desenhar_elementos_jogo() # Desenha o jogo por baixo
        # Overlay de PAUSE
        s = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
        s.fill((0, 0, 0, 150)) # Fundo semitransparente
        TELA.blit(s, (0, 0))

        pause_texto = FONTE_PAUSE.render("PAUSE", True, BRANCO)
        pause_rect = pause_texto.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2))
        TELA.blit(pause_texto, pause_rect)
    elif GAME_STATE == "GAME_OVER":
        tela_game_over()

    pygame.display.flip()
    clock.tick(FPS)

# Finaliza o motor de fala e o Pygame
if engine._isBusy:
    engine.stop()
pygame.quit()
