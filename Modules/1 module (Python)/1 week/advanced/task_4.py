"""Строки. Анаграммы
Напишите программу на Python, которая принимает на вход два слова и определяет, являются ли эти слова анаграммами друг друга
(регистр букв игнорируется). Анаграмма - это слово или фраза, образованные перестановкой букв другого слова или фразы.
Например, "listen" и "silent" являются анаграммами друг друга, так как они состоят из одних и тех же букв, расположенных в другом порядке.

Программа должна выводить результат в виде сообщения "Слова являются анаграммами." или "Слова не являются анаграммами.".

Формат ввода
listen

silent
Формат вывода
Слова являются анаграммами."""
a = input().lower()
b = input().lower()
a = sorted(a)
b = sorted(b)
if a == b:
    print("Слова являются анаграммами.")
else:
    print("Слова не являются анаграммами.")