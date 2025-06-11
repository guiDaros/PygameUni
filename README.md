Jogo do Iron Marcio
Um jogo simples onde o personagem tem que desviar dos obstaculos, desenvolvido em Python com Pygame.

Nome do Desenvolvedor 
Guilherme Vassoller Daros

RA (1138143)

Tecnologias Utilizadas
Python: Linguagem de programação principal.

Pygame: Biblioteca para desenvolvimento de jogos 2D.

speech_recognition: Para reconhecimento de voz na entrada do nome do jogador.

pyttsx3: Para conversão de texto em fala (text-to-speech).

PyInstaller: Ferramenta para gerar o executável do jogo.

Como Jogar
Início: Ao iniciar o jogo, digite seu nome (ou use o reconhecimento de voz) e clique em "Continuar".

Boas-Vindas: Uma tela de boas-vindas exibirá seu nome e uma breve explicação da mecânica do jogo. Clique em "Iniciar Partida" para começar.

Controles: Mova sua nave apenas no eixo X (esquerda e direita) usando o cursor do mouse.

Objetivo: Desvie dos asteroides que caem para ganhar pontos.

Pausa: Pressione a tecla ESPAÇO (Space) a qualquer momento para pausar o jogo. Pressione novamente para retomar.

Fim de Jogo: A partida termina se sua nave colidir com um asteroide. A tela de Game Over mostrará sua pontuação e os últimos 5 registros de partidas.

Estrutura do Projeto
seu_jogo/
├── main.py                     # Código principal do jogo
├── setup.py                    # Script para gerar o executável
├── README.md                   # Este arquivo
└── Recursos/                   # Pasta para todos os assets do jogo
    ├── imagens/
    │   ├── fundo_estrelas.png  # Imagem de fundo do jogo (substitua)
    │   ├── nave_personagem.png # Imagem do personagem (substitua)
    │   └── asteroide.png       # Imagem do asteroide/inimigo (substitua)
    │   └── objeto_circulando.png # Imagem do objeto decorativo (substitua)
    ├── sons/                   # Sons do jogo (opcional)
    ├── fontes/                 # Fontes do jogo (opcional)
    └── funcoes_uteis.py        # Módulo com funções auxiliares (ex: desenhar texto multilinha)

Configuração e Instalação
Clone o repositório:


Instale as dependências:

pip install pygame speechrecognition pyttsx3 pyinstaller

Execute o jogo:

python main.py

Gerando o Executável
Para gerar um executável do jogo (Windows, macOS, Linux):

Certifique-se de ter o PyInstaller instalado (pip install pyinstaller).

Execute o script setup.py:

python setup.py

O executável será criado na pasta dist/SobrevivenciaEspacial/.

Colaboravção e Commits
Este projeto foi desenvolvido seguindo as diretrizes de controle de versão (Git). Espera-se que o repositório contenha commits descritivos para cada etapa de desenvolvimento.


Testador do Jogo
Nome: 

RA: 
