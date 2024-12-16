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
        if product in self.cart:
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

    def apply_discount(self, discount_percentage):
        total = self.calculate_total()
        discount_amount = total * (discount_percentage / 100)
        discounted_total = total - discount_amount
        return discounted_total


# Пример создания магазина с продуктами
apple = Product("Яблоко", 20)
bread = Product("Хлеб", 15)
milk = Product("Молоко", 30)
cheese = Product("Сыр", 60)
butter = Product("Масло", 40)
chicken = Product("Курица", 90)
potato = Product("Картофель", 10)
onion = Product("Лук", 8)
carrot = Product("Морковь", 12)
egg = Product("Яйца (упаковка)", 35)
pepsi = Product("Пепси (бутылка)", 25)
papita = Product("Печенье Папита", 18)

# Создание корзины покупок
cart = ShoppingCart()

while True:
    print("\nДобро пожаловать в магазин АТБ!")
    print("Доступные товары:")
    print("1. Яблоко - 20 грн")
    print("2. Хлеб - 15 грн")
    print("3. Молоко - 30 грн")
    print("4. Сыр - 60 грн")
    print("5. Масло - 40 грн")
    print("6. Курица - 90 грн")
    print("7. Картофель - 10 грн")
    print("8. Лук - 8 грн")
    print("9. Морковь - 12 грн")
    print("10. Яйца (упаковка) - 35 грн")
    print("11. Пепси (бутылка) - 25 грн")
    print("12. Печенье Папита - 18 грн")
    print("13. Показать корзину")
    print("14. Удалить товар из корзины")
    print("15. Применить скидку")
    print("16. Оформить покупку")
    print("17. Выход")

    choice = input("Выберите действие (1-17): ")

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
        cart.add_product(cheese)
        print("Сыр добавлен в корзину.")
    elif choice == "5":
        cart.add_product(butter)
        print("Масло добавлено в корзину.")
    elif choice == "6":
        cart.add_product(chicken)
        print("Курица добавлена в корзину.")
    elif choice == "7":
        cart.add_product(potato)
        print("Картофель добавлен в корзину.")
    elif choice == "8":
        cart.add_product(onion)
        print("Лук добавлен в корзину.")
    elif choice == "9":
        cart.add_product(carrot)
        print("Морковь добавлена в корзину.")
    elif choice == "10":
        cart.add_product(egg)
        print("Яйца добавлены в корзину.")
    elif choice == "11":
        cart.add_product(pepsi)
        print("Пепси добавлена в корзину.")
    elif choice == "12":
        cart.add_product(papita)
        print("Печенье Папита добавлено в корзину.")
    elif choice == "13":
        cart.display_cart()
    elif choice == "14":
        cart.display_cart()
        remove_choice = input(
            "Введите название товара, который хотите удалить из корзины: "
        )
        for product in cart.cart:
            if remove_choice.lower() == product.name.lower():
                cart.remove_product(product)
                print(f"{product.name} удалено из корзины.")
                break
        else:
            print("Товар не найден в корзине.")
    elif choice == "15":
        discount = float(input("Введите процент скидки: "))
        discounted_total = cart.apply_discount(discount)
        print(f"Общая сумма с учетом скидки: {discounted_total} грн")
    elif choice == "16":
        cart.display_cart()
        print("Спасибо за покупку!")
        break
    elif choice == "17":
        print("До свидания!")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите номер от 1 до 17.")
