import speech_recognition as sr

def ouvir_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo comando...")
        audio = recognizer.listen(source)

        try:
            comando = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Comando reconhecido: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("Não entendi o comando.")
        except sr.RequestError:
            print("Erro na requisição ao serviço de reconhecimento.")

    return ""
