from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Создаем бота
bot = ChatBot("LapBot")

# Обучаем его на русском языке
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.russian")

# Основной цикл общения
print("Привет! Я бот. Задай мне вопрос.")
while True:
    user_input = input("Вы: ")
    if user_input.lower() in ["пока", "выход"]:
        print("Бот: Пока!")
        break
    response = bot.get_response(user_input)
    print(f"Бот: {response}")
