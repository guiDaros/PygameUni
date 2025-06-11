import speech_recognition as sr
import pyttsx3

def inicializar_voz():
    """Inicializa o engine de síntese de voz"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidade da fala
    return engine

def ouvir_comando():
    """Ouve e reconhece comandos de voz"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    try:
        comando = r.recognize_google(audio, language='pt-BR')
        print(f"Comando reconhecido: {comando}")
        return comando.lower()
    except Exception as e:
        print(f"Erro no reconhecimento: {e}")
        return ""

def falar(engine, texto):
    """Sintetiza voz a partir do texto"""
    engine.say(texto)
    engine.runAndWait()