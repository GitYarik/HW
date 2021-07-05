# Создать функцию поиска минимума и максимума в списке.

from random import randint

lst = [randint(0, 100) for i in range(22)]


def min_max(x):
    return min(x), max(x)


print(min_max(lst))
