import datetime
import webbrowser

import pyttsx3
import speech_recognition as sr


def speak(text):
    """Говорит текст вслух."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen():
    """Распознает голосовые команды."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="ru-RU")
        print(f"Вы сказали: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return "Не понял"
    except sr.RequestError:
        return "Ошибка сети"


def voice_assistant():
    """Основная функция ассистента."""
    speak("Привет! Я ваш голосовой помощник. Что вы хотите?")
    while True:
        command = listen()
        if "время" in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"Сейчас {now}")
        elif "открой сайт" in command:
            speak("Какой сайт открыть?")
            url = listen()
            webbrowser.open(f"http://{url}")
            speak(f"Открываю {url}")
        elif "пока" in command:
            speak("До свидания!")
            break
        else:
            speak("Извините, я не понял команду.")


voice_assistant()
