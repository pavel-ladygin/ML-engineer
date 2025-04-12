"""Коллекции. Расширенная группировка товаров
На вход подаются строки, представляющие собой информацию о товарах. Необходимо сгруппировать товары по категориям,
подкатегориям и вывести их в требуемом формате, отсортировав товары внутри каждой подкатегории по цене в порядке возрастания,
категории и подкатегории в каждой категории по алфавиту. Строки вводятся до тех пор, пока не встретится слово "стоп".

Условия:

Каждая строка содержит информацию о товаре в формате: Категория - Подкатегория - Название товара - Цена.
Гарантируется, что названия товаров не повторяются и что будет введено хотя бы одно значение товара.
Структура вывода:

Категория:
  Подкатегория1:
    - Название товара1 (Цена1 руб.)
    - Название товара2 (Цена2 руб.)
    ...
  Подкатегория2:
    - Название товара1 (Цена1 руб.)
    - Название товара2 (Цена2 руб.)
    ...

Формат ввода
Электроника - Телефон - Samsung Galaxy S23 - 50000
Электроника - Ноутбук - Lenovo IdeaPad 3 - 40000
Электроника - Телефон - iPhone 14 Pro Max - 80000
Продукты - Чай - Lipton зеленый - 120
Продукты - Кофе - Lavazza Crema e Aroma - 300
Одежда - Кроссовки - Adidas Ultraboost 23 - 12000
стоп


Формат вывода
Одежда:
  Кроссовки:
    - Adidas Ultraboost 23 (12000 руб.)
Продукты:
  Кофе:
    - Lavazza Crema e Aroma (300 руб.)
  Чай:
    - Lipton зеленый (120 руб.)
Электроника:
  Ноутбук:
    - Lenovo IdeaPad 3 (40000 руб.)
  Телефон:
    - Samsung Galaxy S23 (50000 руб.)
    - iPhone 14 Pro Max (80000 руб."""

from collections import defaultdict

categories = defaultdict(lambda: defaultdict(list))

while True:
    line = input()
    if line == "стоп":
        break

    category, subcategory, item, price = line.split(" - ")
    categories[category][subcategory].append((item, int(price)))

sorted_categories = sorted(categories.items())

for category, subcategories in sorted_categories:
    print(f"{category}:")
    sorted_subcategories = sorted(subcategories.items())
    for subcategory, items in sorted_subcategories:
        print(f"  {subcategory}:")
        sorted_items = sorted(items, key=lambda item: (item[1], item[0]))
        for item, price in sorted_items:
            print(f"    - {item} ({price} руб.)")