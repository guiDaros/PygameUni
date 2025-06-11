# setup.py
from cx_Freeze import setup, Executable
import os

# Certifique-se de que a pasta 'Recursos' está na mesma pasta do 'setup.py'
# e que as imagens estão em 'Recursos/imagens'

# Configurações para cx_Freeze
# Base no Windows: para aplicativos GUI, evita a janela do console
base = None
if os.sys.platform == "win32":
    base = "Win32GUI"

# Define os executáveis
executables = [
    Executable(
        "main.py",
        base=base,
        target_name="SobrevivenciaEspacial.exe", # Nome do executável
        icon="recursos/imagens/nave.png" # Opcional: ícone do executável (mude para .ico se for usar)
    )
]

# Opções de build, incluindo a pasta Recursos
build_options = {
    "packages": ["pygame", "random", "math", "datetime", "os", "speech_recognition", "pyttsx3", "json"], # Adicione todos os pacotes que seu main.py importa
    "includes": [], # Inclua módulos específicos se necessário
    "excludes": ["tkinter"], # Exclua pacotes que não são necessários
    "include_files": [
        "Recursos" # Inclui a pasta Recursos e todo o seu conteúdo
    ]
}

# Chama a função setup para criar o executável
setup(
    name="SobrevivenciaEspacial",
    version="1.0",
    description="Um jogo onde o Iron Marcio tem que esquivar das roçadeiras",
    options={"build_exe": build_options},
    executables=executables
)

print("\nExecutável gerado na pasta 'build/exe.PLATFORMA-VERSAO_PYTHON/'")
