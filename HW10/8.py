# Напишите функцию sum_range(start, end), которая
# суммирует все целые числа от значения «start» до величины
# «end» включительно. Если пользователь задаст первое
# число большее чем второе, просто поменяйте их местами.


def sum_range(start, end):
    a = 0
    if start < end:
        for i in range(start, end + 1):
            a += i
    elif start > end:
        for j in range(end, start + 1):
            a += j
    return a


print(sum_range(1, 6))
