"""Строки. Формирование URL-адреса
С клавиатуры вводится две строки:

Раздел сайта (например, "articles", "blog", "news")
Заголовок статьи (например, "How to write a program in Python"). Заголовок статьи не содержит знаков препинания.
Программа должна сгенерировать URL-адрес для сайта https://www.mycoolsyte.com/, который будет иметь следующий формат:
https://www.mycoolsyte.com/<раздел>/<заголовок-статьи>;. Преобразуйте заголовок в соответствие с примером.

Формат ввода
articles

How to write a program in Python
Формат вывода
Созданный URL: https://www.mycoolsyte.com/articles/how-to-write-a-program-in-python"""
a = input().lower()
b = input().lower()
s = "https://www.mycoolsyte.com/"
for i in b:
    if i == " ":
        b = b.replace(i, "-")
print("Созданный URL: "+ s+a+"/"+b)