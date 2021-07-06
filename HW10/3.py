# Написать функцию season, принимающую 1 аргумент —
# номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или
# осень).
def month(x):
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
    return x


month(1)
