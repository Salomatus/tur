import unittest
from unittest import mock

import pytest

from src.main import Category, Product


def test_add_product():
    category = Category("Фрукты", "Отечественные")
    product = Product.create_product("Яблоки", "Отечественные", 15.5, 55)
    category.add_product(product)
    assert category.goods == "Яблоки, 15.5 руб. Остаток: 55 шт.)"


def test_change_price():
    product = Product.create_product("Телевизор", "4K Smart TV", 50000, 10)
    assert product.price == 50000
    product.price = 45000
    assert product.price == 45000


def test_negative_price():
    product = Product.create_product("Смартфон", "Android", 30000, 5)
    assert product.price == 30000
    product.price = -1000
    assert product.price == 30000


def test_confirm_price_change():
    product = Product.create_product("Смартфон", "Android", 30000, 5)
    assert product.price == 30000
    with mock.patch("builtins.input", return_value="y"):
        product.price = 25000
    assert product.price == 25000


def test_cancel_price_change():
    product = Product.create_product("Смартфон", "Android", 30000, 5)
    assert product.price == 30000
    with mock.patch("builtins.input", return_value="n"):
        product.price = 25000
    assert product.price == 30000


class TestProduct(unittest.TestCase):
    def test_add_method(self):
        # Создаем два объекта Product
        product1 = Product("Яблоки", "Отечественные", 15.5, 55)
        product2 = Product("Телевизор", "4K Smart TV", 50000, 10)

        # Вычисляем ожидаемый результат
        expected_result = 15.5 * 55 + 50000 * 10

        # Вызываем метод __add__ и проверяем, что результат совпадает с ожидаемым
        self.assertEqual(product1 + product2, expected_result)


def test_add_product_valid():
    category = Category("Электроника", "Техника для дома")
    product = Product("Телевизор", "4K Smart TV", 50000, 10)
    category.add_product(product)
    assert len(category._Category__goods) == 1


def test_add_product_invalid():
    category = Category("Электроника", "Техника для дома")
    with pytest.raises(TypeError):
        category.add_product("Телевизор")