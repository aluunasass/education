import tkinter as tk
from tkinter import messagebox

# Список товаров
products = [
    {"id": 1, "name": "Кошачья лапка", "price": 200},
    {"id": 2, "name": "Собачья лапка", "price": 250},
    {"id": 3, "name": "Лапка енота", "price": 300},
    {"id": 4, "name": "Лапка медведя", "price": 400},
]

# Корзина
cart = []


def add_to_cart(product):
    """Добавить товар в корзину."""
    cart.append(product)
    messagebox.showinfo(
        "Корзина", f"Добавлено: {product['name']} за {product['price']} рублей"
    )


def show_cart():
    """Показать содержимое корзины."""
    if not cart:
        messagebox.showinfo("Корзина", "Корзина пуста.")
        return

    cart_details = "\n".join(
        [f"{item['name']} - {item['price']} рублей" for item in cart]
    )
    total = sum(item["price"] for item in cart)
    messagebox.showinfo("Корзина", f"{cart_details}\n\nИтого: {total} рублей")


def checkout():
    """Оформить заказ."""
    if not cart:
        messagebox.showinfo(
            "Оформление заказа", "Корзина пуста. Добавьте товары перед покупкой."
        )
        return

    total = sum(item["price"] for item in cart)
    messagebox.showinfo(
        "Оформление заказа", f"Спасибо за покупку! Итоговая сумма: {total} рублей"
    )
    cart.clear()


# Создание окна приложения
root = tk.Tk()
root.title("Магазин лапок")
root.geometry("400x400")

# Заголовок
title_label = tk.Label(root, text="Магазин лапок", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Товары
for product in products:
    frame = tk.Frame(root)
    frame.pack(pady=5)

    name_label = tk.Label(
        frame, text=f"{product['name']} - {product['price']} рублей", font=("Arial", 12)
    )
    name_label.pack(side=tk.LEFT, padx=10)

    add_button = tk.Button(
        frame, text="Добавить в корзину", command=lambda p=product: add_to_cart(p)
    )
    add_button.pack(side=tk.RIGHT)

# Кнопки управления
cart_button = tk.Button(
    root, text="Показать корзину", command=show_cart, bg="lightblue", font=("Arial", 12)
)
cart_button.pack(pady=10)

checkout_button = tk.Button(
    root, text="Оформить заказ", command=checkout, bg="lightgreen", font=("Arial", 12)
)
checkout_button.pack(pady=10)

# Запуск основного цикла приложения
root.mainloop()
