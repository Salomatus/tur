class Category:
    """Класс для категорий"""

    name: str
    description: str
    __goods: list  # приватный атрибуд

    # общее количество категорий и общее количество уникальных продуктов
    number_of_categories = 0
    number_of_unique_products = 0

    def __init__(self, name, description):
        """Метод для инициализации экземпляра класса, задаем значение атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.__goods = []  # Инициализируем список товаров

        Category.number_of_categories += 1
        Category.number_of_unique_products += 1

    def add_product(self, product):
        """Метод для добавления товара в список товаров"""
        self.__goods.append(product)

    @property
    def goods(self):
        return "\n".join(str(product) for product in self.__goods)

    def __len__(self):
        return sum(product.quantity for product in self.__goods)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."


class Product:
    """Класс для продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса, задаем значение атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.__price = price  # приватный атрибут
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        """Класс-метод для создания товара и возращения объекта"""
        return cls(name, description, price, quantity)

    @classmethod
    def create_product1(cls, name, description, price, quantity, products_list):
        for existing_product in products_list:
            if existing_product.name == name:
                if existing_product.price < price:
                    existing_product.price = price
                existing_product.quantity += quantity
                return None
        new_product = cls(name, description, price, quantity)
        products_list.append(new_product)
        return new_product

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены"""
        if new_price <= 0:
            print("ценна введена некорректно")
        elif new_price < self.__price:
            confirmation = input("Вы уверены, что хотите понизить цену? (y/n): ")
            if confirmation.lower() == "y":
                self.__price = new_price
                print("Цена успешно понижена")
            else:
                print("Действие отменено")
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.)"

    def __add__(self, other):
        result = self.__price * self.quantity + other.__price * other.quantity
        return result


# Создание объекта класса Category и добавление товаров:

category_1 = Category("Фрукты", "Отечественные")
product1 = Product.create_product("Яблоки", "Отечественные", 15.5, 55)
category_1.add_product(product1)

category_2 = Category("Электроника", "Техника для дома")
product2 = Product.create_product("Телевизор", "4K Smart TV", 50000, 10)
product3 = Product.create_product("Смартфон", "Android", 30000, 5)
category_2.add_product(product2)
category_2.add_product(product3)

# Вывод списка товаров категории:
print(category_1.goods)
print(category_2.goods)

# вывод количества остатка на складе
print(category_2)
print(category_1)

# Изменение цены товара:
product1.price = 45000

# Попытка изменения цены на некорректное значение:
product2.price = -1000

# Подтверждение понижения цены товара:
product3.price = 25000

# Отмена понижения цены товара:
product3.price = 35000

# вывод общего остатка
total_price = product3 + product2
print(f"Общая сумма остатка {total_price}")
