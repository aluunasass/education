class Product:
    """Класс для представления продукта."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} грн"


class ShoppingCart:
    """Класс для представления корзины покупок."""

    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, product):
        self.cart.remove(product)

    def calculate_total(self):
        total = sum(product.price for product in self.cart)
        return total

    def display_cart(self):
        if not self.cart:
            print("Корзина пуста.")
        else:
            print("Ваши товары в корзине:")
            for product in self.cart:
                print(product)
            print(f"Общая сумма: {self.calculate_total()} грн")


# Пример создания магазина с продуктами
apple = Product("Яблоко", 20)
bread = Product("Хлеб", 15)
milk = Product("Молоко", 30)

# Создание корзины покупок
cart = ShoppingCart()

while True:
    print("\nДобро пожаловать в магазин АТБ!")
    print("Доступные товары:")
    print("1. Яблоко - 20 грн")
    print("2. Хлеб - 15 грн")
    print("3. Молоко - 30 грн")
    print("4. Показать корзину")
    print("5. Оформить покупку")
    print("6. Выход")

    choice = input("Выберите действие (1-6): ")

    if choice == "1":
        cart.add_product(apple)
        print("Яблоко добавлено в корзину.")
    elif choice == "2":
        cart.add_product(bread)
        print("Хлеб добавлен в корзину.")
    elif choice == "3":
        cart.add_product(milk)
        print("Молоко добавлено в корзину.")
    elif choice == "4":
        cart.display_cart()
    elif choice == "5":
        cart.display_cart()
        print("Спасибо за покупку!")
        break
    elif choice == "6":
        print("До свидания!")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите номер от 1 до 6.")
