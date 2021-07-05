# Создать функцию для заполнения списка рандомными
# значениями. Заполнить список с помощью функции и
# написать функцию для подсчёта одинаковых элементов
# списка.

def ran_dom(a, b, c):
    from random import randint
    from collections import Counter
    lst = [randint(a, b) for _ in range(c)]
    lst1 = []
    for j in lst:
        lst1.append(j)
    return Counter(lst1)


print(ran_dom(1, 3, 22))
