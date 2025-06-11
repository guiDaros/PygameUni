Sobrevivência Espacial
Um jogo simples de sobrevivência espacial desenvolvido em Python com Pygame.

Nome do Desenvolvedor 
Guilherme Vassoller Daros

RA (1138143)

Pequena Descrição da História do Jogo
Em "Sobrevivência Espacial", você é um piloto habilidoso de uma nave espacial em meio a um campo de asteroides perigoso. Sua missão é desviar dos destroços que caem do céu, aprimorando seus reflexos e sua pontuação. A cada asteroide desviado, sua pontuação aumenta, mas a ameaça também cresce, pois a velocidade dos asteroides se intensifica. Quanto tempo você consegue sobreviver neste ambiente hostil?

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

git clone https://github.com/dolthub/dolt
cd seu_jogo

Instale as dependências:

pip install pygame speechrecognition pyttsx3 pyinstaller

Adicione seus assets:
Certifique-se de que suas imagens personalizadas (fundo_estrelas.png, nave_personagem.png, asteroide.png, objeto_circulando.png) estão na pasta Recursos/imagens/.

Execute o jogo:

python main.py

Gerando o Executável
Para gerar um executável do jogo (Windows, macOS, Linux):

Certifique-se de ter o PyInstaller instalado (pip install pyinstaller).

Execute o script setup.py:

python setup.py

O executável será criado na pasta dist/SobrevivenciaEspacial/.

Colaboração e Commits
Este projeto foi desenvolvido seguindo as diretrizes de controle de versão (Git). Espera-se que o repositório contenha commits descritivos para cada etapa de desenvolvimento.

Instruções para o Colega (Testador do Jogo):

Para o colega que for colaborar, siga estes passos:

Faça um fork deste repositório para a sua conta GitHub.

Clone o seu fork para sua máquina local.

Crie uma nova branch para sua alteração:

git checkout -b adicionar-nome-testador

Edite este arquivo README.md e adicione seu nome completo e RA na seção Testador do Jogo abaixo.

Adicione as mudanças e faça um commit:

git add README.md
git commit -m "feat: Adiciona nome do testador no README - [Seu Nome]"

Adicione uma tag ao seu commit:

git tag "Testador do Jogo: [Seu Nome] e [Seu RA]"

Envie a branch para o seu fork:

git push origin adicionar-nome-testador

Crie um Pull Request do seu fork para o repositório original.

Testador do Jogo
Nome: [NOME DO SEU COLEGA AQUI]

RA: [RA DO SEU COLEGAS AQUI]