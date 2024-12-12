import time

BOSS = "Саша"


class Friend:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Привет. Я {self.name}. Мне {self.age}."

    def __repr__(self):
        return f"{self.name}"

    def play_volleyball(self):
        print(f"{self.name} играет с {BOSS} в волейбол")
        time.sleep(5)

    def eat(self):
        food = input("Что будем кушать?:")
        print(f"{self.name} жрет с {BOSS} {food}")
        time.sleep(5)

    def go_to_beer(self):
        if self.age >= 18:
            print(f"{self.name} пьет пивко с {BOSS}")
        else:
            print(f"{self.name} не продали пивко")

    def get_options(self) -> dict:
        return {
            "Волейбол": self.play_volleyball,
            "Жрать": self.eat,
            "Пивко": self.go_to_beer,
        }


DASHA = Friend(name="Даша", age=12)
ZLATA = Friend(name="Злата", age=11)

NIKITA = Friend(name="Никита", age=25)
FRIENDS = [DASHA, ZLATA, NIKITA]


def game():
    for id, friend in enumerate(FRIENDS):
        print(f"{id}) {friend}")

    friend_id = int(input("Выберите подружку:"))
    friend = FRIENDS[friend_id]

    for id, (name, option) in enumerate(friend.get_options().items()):
        print(f"{id}) {name}")

    option_id = int(input("Введите опцию:"))

    for id, (name, option) in enumerate(friend.get_options().items()):
        if id == option_id:
            option()


if __name__ == "__main__":
    while True:
        game()
