# Напишите функцию, которая принимает значения трёх
# сторон треугольника и отвечает на вопрос существует ли он.

def rea(a, b, c):
    d = a + b
    e = b + c
    f = c + a
    # AB + BC > AC, AC + BC > AB, AB + AC > BC
    if d >= c and e >= a and f >= b:
        return print("треугольник существует")
    else:
        return print("треугольник не существует")


rea(1, 2, 3)
