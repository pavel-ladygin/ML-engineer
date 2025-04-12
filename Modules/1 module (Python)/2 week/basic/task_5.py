"""Даты
С клавиатуры вводится дата в формате DD-MM-YYYY. Нужно вывести дату начала недели,
к которой относится введенная дата (дата понедельника недели), в таком же формате.

Формат ввода
22-09-2022

Формат вывода
19-09-2022
"""
from datetime import datetime, timedelta

date_str = input()

date_obj = datetime.strptime(date_str, "%d-%m-%Y")

weekday = date_obj.weekday()  # 0 - понедельник, 6 - воскресенье

monday_date = date_obj - timedelta(days=weekday)

monday_date_str = monday_date.strftime("%d-%m-%Y")

print(monday_date_str)