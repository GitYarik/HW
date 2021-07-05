# Написать функцию season, принимающую 1 аргумент —
# номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или
# осень).

def season():
    if month <= 2 or month == 12:
        return "winter"
    elif 3 <= month < 6:
        return "wesna"
    elif 6 <= month < 9:
        return "leto"
    elif 9 <= month < 12:
        return "osen"
    else:
        return "error"


month = int(input("Введите номер месяца (1-12): "))
print(season())
