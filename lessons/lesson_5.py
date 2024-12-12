import random


def game():
    while True:
        number = int(input("Введите число от 1 до 6:"))
        if number > 6 or number < 1:
            print("Вы ввели неправильное чилсо")
            continue
        r = random.randint(1, 6)
        if r == number:
            print("Вы победили!")
            break
        else:
            print(f"Вы проиграли выпало число {r}!")


if __name__ == "__main__":
    game()
