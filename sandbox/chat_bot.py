def chatbot():
    print("Привет! Я простой чат-бот. Спроси меня что-нибудь.")
    while True:
        user_input = input("Вы: ").lower()
        if "привет" in user_input:
            print("Бот: Привет! Как дела?")
        elif "как тебя зовут" in user_input:
            print("Бот: Меня зовут Ботик.")
        elif "пока" in user_input:
            print("Бот: Пока! Хорошего дня.")
            break
        else:
            print("Бот: Извини, я пока не понимаю этого.")


chatbot()
