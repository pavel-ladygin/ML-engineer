""""Строки. Замена символов
С клавиатуры вводится строка. В строке заменить пробелы звездочкой.
Если встречается подряд несколько пробелов, то их следует заменить одним знаком "*",
 пробелы в начале и конце строки удалить.

Формат ввода
Какая-нибудь строка типа этой .
Формат вывода
Какая-нибудь*строка*типа*этой*."""
a = input()
cnt = 1
for i in range(len(a)):
    if a[i] == " ":
        cnt += 1
        a = a.replace(a[i], "*")
a1 = a
for i in range(len(a)-1):
    cur = a[i]
    _rigth = a[i+1]
    if cur == "*" and _rigth == "*":
        a1 = a1.replace(cur+_rigth, "*")
if a1[0] == "*":
    a1 = a1[1:-1]
if a1[-1] == "*":
    a1 = a1[0:-2]
print(a1)