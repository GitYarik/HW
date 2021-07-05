#Есть два списка, написать функцию, которая принимает
#два списка и возвращает список с общими элементами
#первых двух.
from random import randint

lst1 = [randint(0, 10) for i in range(7)]
lst2 = [randint(0, 10) for j in range(7)]
lst3=[]



def lst(x,y,z):
    for i in x:
        for j in y:
            if i == j:
                z.append(j)
                break
    return z

print(lst(lst1,lst2,lst3))
print(lst1)
print(lst2)