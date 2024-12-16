import random


def rock_paper_scissors():
    choices = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(choices).capitalize()
    user_choice = input("Выберите: Камень, Ножницы или Бумага: ").capitalize()

    if user_choice == computer_choice:
        print(f"Ничья! Компьютер тоже выбрал {computer_choice}.")
    elif (
        (user_choice == "Камень" and computer_choice == "Ножницы")
        or (user_choice == "Ножницы" and computer_choice == "Бумага")
        or (user_choice == "Бумага" and computer_choice == "Камень")
    ):
        print(f"Вы победили! Компьютер выбрал {computer_choice}.")
    else:
        print(f"Вы проиграли! Компьютер выбрал {computer_choice}.")


rock_paper_scissors()
