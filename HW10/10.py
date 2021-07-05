#Список [16, -17, 2, 78.7, False, False, {‘True’: True}, 555, 12, 23, 42,
#‘DD’] Функция, принимает на вход список -выбирает из него
#все int и float -составить из него новый список,
#отсортированный от наименьшего значения большему
lst=[16,-17, 2, 78.7, False, False, {"True": True}, 555, 12, 23, 42,"DD"]

def num(x):
    s = []
    for i in x:
        if type(i) is int or type(i) is float:
             s.append(i)
    return sorted(s)

print(num(lst))

