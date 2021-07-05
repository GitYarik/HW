# Создать функцию для заполнения списка рандомными
# значениями. Заполнить список с помощью функции и
# написать функцию для подсчёта одинаковых элементов
# списка.


def random_counter(x, y, z):
    from random import randint
    from collections import Counter
    lst = [randint(x, y) for _ in range(z)]
    lst1 = []
    print(f'{lst} random list')
    for j in lst:
        lst1.append(j)
    return Counter(lst1)


print(random_counter(1, 11, 22))
