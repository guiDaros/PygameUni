<h1 style="font-size: 2.8em; text-align: center; color: #0056b3; margin-bottom: 0.5em;">Iron Márcio Game</h1>
<h2 style="font-size: 1.6em; text-align: center; color: #555; margin-top: 0.5em; margin-bottom: 2em;">A simple game where the character must dodge obstacles, developed in Python using Pygame.</h2>

<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); margin: 3em 0;">

<h2 style="font-size: 2em; color: #0056b3; margin-bottom: 1em;"><span style="margin-right: 10px;">👨‍💻</span>Developer</h2>
<ul style="list-style-type: none; padding-left: 20px;">
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">Name:</strong> Guilherme Vassoller Daros</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">RA:</strong> 1138143</li>
</ul>

<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); margin: 3em 0;">

<h2 style="font-size: 2em; color: #0056b3; margin-bottom: 1em;"><span style="margin-right: 10px;">🚀</span>Technologies Used</h2>
<ul style="padding-left: 20px;">
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">Python:</strong> Main programming language.</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">Pygame:</strong> Library for 2D game development.</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;"><code>speech_recognition</code>:</strong> For voice recognition when entering the player's name.</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;"><code>pyttsx3</code>:</strong> For text-to-speech conversion.</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;"><code>PyInstaller</code>:</strong> Tool for generating the game executable.</li>
</ul>

<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); margin: 3em 0;">

<h2 style="font-size: 2em; color: #0056b3; margin-bottom: 1em;"><span style="margin-right: 10px;">🎮</span>How to Play</h2>
<ol style="padding-left: 25px;">
    <li style="margin-bottom: 1.2em;"><strong>Start:</strong> When the game launches, type your name (or use voice recognition) and click "<strong style="color: #007bff;">Continue</strong>".</li>
    <li style="margin-bottom: 1.2em;"><strong>Welcome Screen:</strong> A welcome screen will display your name and a brief explanation of the game mechanics. Click "<strong style="color: #007bff;">Start Game</strong>" to begin.</li>
    <li style="margin-bottom: 1.2em;"><strong>Controls:</strong> Move your ship only on the <strong style="color: #dc3545;">X axis</strong> (left and right) using the <strong style="color: #007bff;">mouse cursor</strong>.</li>
    <li style="margin-bottom: 1.2em;"><strong>Objective:</strong> <strong style="color: #28a745;">Dodge</strong> the falling asteroids to score <strong style="color: #ffc107;">points</strong>.</li>
    <li style="margin-bottom: 1.2em;"><strong>Pause:</strong> Press the <strong style="color: #6c757d;">SPACE</strong> key at any time to pause the game. Press again to resume.</li>
    <li style="margin-bottom: 1.2em;"><strong>Game Over:</strong> The game ends if your ship collides with an asteroid. The Game Over screen will display your <strong style="color: #ffc107;">score</strong> and the <strong style="color: #ffc107;">last 5 game records</strong>.</li>
</ol>

<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); margin: 3em 0;">

<h2 style="font-size: 2em; color: #0056b3; margin-bottom: 1em;"><span style="margin-right: 10px;">⚙️</span>Setup & Installation</h2>
<p style="margin-bottom: 1.5em;">To set up and run the game on your machine:</p>
<ol style="padding-left: 25px;">
    <li style="margin-bottom: 1.2em;"><strong>Clone the repository:</strong>
        <pre style="background-color: #f8f8f8; padding: 1em; border-radius: 5px; overflow-x: auto; color: #555;"><code>git clone https://github.com/guiDaros/PygameUni</code></pre>
    </li>
</ol>

<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); margin: 3em 0;">

<h2 style="font-size: 2em; color: #0056b3; margin-bottom: 1em;"><span style="margin-right: 10px;">📦</span>Generating the Executable</h2>
<p style="margin-bottom: 1.5em;">To create an executable version of the game (compatible with Windows, macOS, Linux):</p>
<ol style="padding-left: 25px;">
    <li style="margin-bottom: 1.2em;">Make sure you have the <strong style="color: #dc3545;"><code>required libraries</code></strong> installed (<code>pip install pyinstaller</code>).</li>
    <li style="margin-bottom: 1.2em;">In the root folder of the project, run the build script:
        <pre style="background-color: #f8f8f8; padding: 1em; border-radius: 5px; overflow-x: auto; color: #555;"><code>python setup.py build</code></pre>
        <p style="font-size: 0.9em; font-style: italic; color: #6c757d; margin-top: 0.8em;">Note: If you're using <strong style="color: #dc3545;"><code>cx_Freeze</code></strong> instead of <code>PyInstaller</code>, the command <code>python setup.py build</code> is still valid, but the configuration details will be in <code>setup.py</code> and the final executable will be found in a folder like <code>build/exe.PLATFORM-PYTHON_VERSION/</code>.</p>
    </li>
    <li style="margin-bottom: 1.2em;">The executable and its supporting files will be created in the <strong style="color: #dc3545;"><code>dist/</code></strong> folder (or <strong style="color: #dc3545;"><code>build/</code></strong>, depending on the tool and configuration). In your case, the final executable will be in something like <code>dist/SobrevivenciaEspacial/</code> or <code>build/exe.win-amd64-3.x/SobrevivenciaEspacial.exe</code>.</li>
</ol>

<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); margin: 3em 0;">

<h2 style="font-size: 2em; color: #0056b3; margin-bottom: 1em;"><span style="margin-right: 10px;">🤝</span>Collaboration</h2>
<h3 style="font-size: 1.4em; color: #0056b3; margin-bottom: 0.8em;">Game Testers</h3>
<ul style="list-style-type: none; padding-left: 20px;">
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">Name:</strong> João Paulo Pasolini</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">RA:</strong> 1138273</li>
</ul>

<ul style="list-style-type: none; padding-left: 20px;">
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">Name:</strong> Eduardo Pagliarini Herter</li>
    <li style="margin-bottom: 0.8em;"><strong style="color: #333;">RA:</strong> 1138269</li>
</ul>
