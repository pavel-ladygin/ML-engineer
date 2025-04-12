"""Коллекции. Словари
С клавиатуры вводятся слова через запятую с пробелом. Выведите на экран три наиболее часто встречаемых слова,
вместе с количеством этих слов. Количество должно быть отделено от слова двоеточием и пробелом.
Каждая пара слово-количество должна быть выведена на отдельной строчке. Для простоты гарантируется, что в строке нет слов с одинаковой встречаемостью.

Формат ввода
три, три, и, ещё, три, будет, дырка, и, будет, и, дырка, и, дырка, и, дырка

Формат вывода
и: 5
дырка: 4
три: 3"""
from collections import Counter

input_string = input()
words = input_string.split(", ")

word_counts = Counter(words)

most_common_words = word_counts.most_common(3)

for word, count in most_common_words:
  print(f"{word}: {count}")