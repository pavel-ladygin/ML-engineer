"""Функции. Аргументы 2
Вам нужно написать функцию lists_sum, которая принимает произвольное количество списков чисел, и возвращает сумму всех этих чисел.
Предусмотрите дополнительный аргумент unique, который по умолчанию равен False, но если в функцию подается unique=True, то функция должна вернуть сумму всех уникальных чисел из всех списков.
Если поданы только пустые списки или списки чисел вообще не поданы в функцию, то считать сумму чисел нулём.
Пример использования

lists_sum([1, 1], [1], [1, 2, 3]) # должна вернуть 9

lists_sum([1, 1, 1], [1, 1], unique=True) # должна вернуть 1

lists_sum([1, 1, 1], unique=False) # должна вернуть 3"""
import ast

def lists_sum(*args, unique=False):

    if not args:
      return 0


    all_numbers = []

    if len(args) == 1 and isinstance(args[0], list) and all(isinstance(item,list) for item in args[0]):
      # Если пришел один список списков
      for lst in args[0]:
        all_numbers.extend(lst)

    else:
      # Если пришло несколько списков как аргументы
      for lst in args:
        if isinstance(lst,list):
           all_numbers.extend(lst)
        else:
          print("Аргументы должны быть списком чисел или списком списков")
          return 0


    if unique:
        unique_numbers = set(all_numbers)
        return sum(unique_numbers)
    else:
        return sum(all_numbers)



if __name__ == '__main__':
    input_str = input()
    try:
        result = eval(input_str)  # Выполнение введенной строки как кода
        print("Результат:", result)
    except Exception as e:
        print()