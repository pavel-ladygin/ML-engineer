"""Даты. Разница между датами
Напишите программу, которая принимает на вход две строки:

Первая дата в формате "ГГГГ-ММ-ДД".
Вторая дата в формате "ГГГГ-ММ-ДД".
Программа должна рассчитать количество полных лет между датами, и корректно отобразить результат, учитывая склонения (год, года, лет).
Обе даты лежат в диапазоне с 1900 по 2024 год включительно. Вторая дата больше первой минимум на один год.

Формат ввода
1990-01-01
1993-09-15

Формат вывода
3 года"""

from datetime import datetime

date_str1 = input()
date_str2 = input()

date1 = datetime.strptime(date_str1, "%Y-%m-%d")
date2 = datetime.strptime(date_str2, "%Y-%m-%d")

years = date2.year - date1.year

if date2.month < date1.month or (date2.month == date1.month and date2.day < date1.day):
    years -= 1

def pluralize_year(years):
    if years % 10 == 1 and years % 100 != 11:
        return "год"
    elif 2 <= years % 10 <= 4 and (years % 100 < 10 or years % 100 > 20):
        return "года"
    else:
        return "лет"
print(f"{years} {pluralize_year(years)}")