import speech_recognition as sr

def ouvir_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale agora...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            comando = r.recognize_google(audio, language="pt-BR")
            print("Você disse:", comando)
            return comando.lower()
        except sr.UnknownValueError:
            print("Não entendi. Tente de novo.")
        except sr.RequestError:
            print("Erro no serviço de reconhecimento.")
        return ""
