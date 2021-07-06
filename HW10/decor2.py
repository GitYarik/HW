# 2. Создайте собственные декораторы(любой функционал) для функций из
# предыдущего дз.


def time_function(func):
    def wrapped():
        a = 0
        start = int(input("1"))
        end = int(input("2"))
        if start < end:
            for i in range(start, end + 1):
                a += i
        elif start > end:
            for j in range(end, start + 1):
                a += j
        print(a)
        func()
        x = int(input("month"))
        if 3 <= x < 6:
            print("win")
        elif 6 <= x < 9:
            print("let")
        elif 9 <= x < 12:
            print("os")
        elif x == 12 or (0 < x < 3):
            print("winter")
        else:
            print("error")

    return wrapped


@time_function
def time_sleep():
    a = int(input("d"))
    b = int(input("e"))
    c = int(input("f"))
    d = a + b
    e = b + c
    f = c + a
    # AB + BC > AC, AC + BC > AB, AB + AC > BC
    if d >= c and e >= a and f >= b:
        return print("треугольник существует")
    else:
        return print("треугольник не существует")


time_sleep()
