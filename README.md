<h1 style="font-size: 2.8em; text-align: center; color: #0056b3; margin-bottom: 0.5em;">Jogo do Iron Márcio</h1>
<h2 style="font-size: 1.6em; text-align: center; color: #555; margin-top: 0.5em; margin-bottom: 2em;">Um jogo simples onde o personagem tem que desviar dos obstáculos, desenvolvido em Python com Pygame.</h2>

<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); margin: 3em 0;">

<h2 style="font-size: 2em; color: #0056b3; margin-bottom: 1em;"><span style="margin-right: 10px;">👨‍💻</span>Desenvolvedor</h2>
<ul style="list-style-type: none; padding-left: 20px;">
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">Nome:</strong> Guilherme Vassoller Daros</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">RA:</strong> 1138143</li>
</ul>

<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); margin: 3em 0;">

<h2 style="font-size: 2em; color: #0056b3; margin-bottom: 1em;"><span style="margin-right: 10px;">🚀</span>Tecnologias Utilizadas</h2>
<ul style="padding-left: 20px;">
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">Python:</strong> Linguagem de programação principal.</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">Pygame:</strong> Biblioteca para desenvolvimento de jogos 2D.</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;"><code>speech_recognition</code>:</strong> Para reconhecimento de voz na entrada do nome do jogador.</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;"><code>pyttsx3</code>:</strong> Para conversão de texto em fala (text-to-speech).</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;"><code>PyInstaller</code>:</strong> Ferramenta para gerar o executável do jogo.</li>
</ul>

<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); margin: 3em 0;">

<h2 style="font-size: 2em; color: #0056b3; margin-bottom: 1em;"><span style="margin-right: 10px;">🎮</span>Como Jogar</h2>
<ol style="padding-left: 25px;">
    <li style="margin-bottom: 1.2em;"><strong>Início:</strong> Ao iniciar o jogo, digite seu nome (ou use o reconhecimento de voz) e clique em "<strong style="color: #007bff;">Continuar</strong>".</li>
    <li style="margin-bottom: 1.2em;"><strong>Boas-Vindas:</strong> Uma tela de boas-vindas exibirá seu nome e uma breve explicação da mecânica do jogo. Clique em "<strong style="color: #007bff;">Iniciar Partida</strong>" para começar.</li>
    <li style="margin-bottom: 1.2em;"><strong>Controles:</strong> Mova sua nave apenas no eixo <strong style="color: #dc3545;">X</strong> (esquerda e direita) usando o <strong style="color: #007bff;">cursor do mouse</strong>.</li>
    <li style="margin-bottom: 1.2em;"><strong>Objetivo:</strong> <strong style="color: #28a745;">Desvie</strong> dos asteroides que caem para ganhar <strong style="color: #ffc107;">pontos</strong>.</li>
    <li style="margin-bottom: 1.2em;"><strong>Pausa:</strong> Pressione a tecla <strong style="color: #6c757d;">ESPAÇO (Space)</strong> a qualquer momento para pausar o jogo. Pressione novamente para continuar o jogo.</li>
    <li style="margin-bottom: 1.2em;"><strong>Fim de Jogo:</strong> A partida termina se sua nave colidir com um asteroide. A tela de Game Over mostrará sua <strong style="color: #ffc107;">pontuação</strong> e os <strong style="color: #ffc107;">últimos 5 registros de partidas</strong>.</li>
</ol>

<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); margin: 3em 0;">

<h2 style="font-size: 2em; color: #0056b3; margin-bottom: 1em;"><span style="margin-right: 10px;">⚙️</span>Configuração e Instalação</h2>
<p style="margin-bottom: 1.5em;">Para configurar e rodar o jogo em sua máquina:</p>
<ol style="padding-left: 25px;">
    <li style="margin-bottom: 1.2em;"><strong>Clone o repositório:</strong>
        <pre style="background-color: #f8f8f8; padding: 1em; border-radius: 5px; overflow-x: auto; color: #555;"><code>git clone     https://github.com/guiDaros/PygameUni


<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); margin: 3em 0;">

<h2 style="font-size: 2em; color: #0056b3; margin-bottom: 1em;"><span style="margin-right: 10px;">📦</span>Gerando o Executável</h2>
<p style="margin-bottom: 1.5em;">Para criar uma versão executável do jogo (compatível com Windows, macOS, Linux):</p>
<ol style="padding-left: 25px;">
    <li style="margin-bottom: 1.2em;">Certifique-se de ter as <strong style="color: #dc3545;"><code>Bibliotecass necessarias</code></strong> instaladas (<code>pip install pyinstaller</code>).</li>
    <li style="margin-bottom: 1.2em;">No terminal, na pasta raiz do projeto, execute o script de build:
        <pre style="background-color: #f8f8f8; padding: 1em; border-radius: 5px; overflow-x: auto; color: #555;"><code>python setup.py build</code></pre>
        <p style="font-size: 0.9em; font-style: italic; color: #6c757d; margin-top: 0.8em;">Obs: Se você estiver usando <strong style="color: #dc3545;"><code>cx_Freeze</code></strong> em vez de <code>PyInstaller</code>, o comando <code>python setup.py build</code> ainda é o correto, mas os detalhes da configuração estarão no <code>setup.py</code> e o executável final estará em uma pasta como <code>build/exe.PLATFORMA-VERSAO_PYTHON/</code>.</p>
    </li>
    <li style="margin-bottom: 1.2em;">O executável e seus arquivos de suporte serão criados na pasta <strong style="color: #dc3545;"><code>dist/</code></strong> (ou <strong style="color: #dc3545;"><code>build/</code></strong>, dependendo da ferramenta e configuração). No seu caso, o executável final estará em algo como <code>dist/SobrevivenciaEspacial/</code> ou <code>build/exe.win-amd64-3.x/SobrevivenciaEspacial.exe</code>.</li>
</ol>

<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); margin: 3em 0;">

<h2 style="font-size: 2em; color: #0056b3; margin-bottom: 1em;"><span style="margin-right: 10px;">🤝</span>Colaboração</h2>
<h3 style="font-size: 1.4em; color: #0056b3; margin-bottom: 0.8em;">Testador do Jogo</h3>
<ul style="list-style-type: none; padding-left: 20px;">
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">Nome:</strong> João Paulo Pasolini</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">RA:</strong> 1138273</li>
</ul>
