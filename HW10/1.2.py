# В файле mylist.txt записаны строки. В каждой строке фамилия, имя и
# оценка ученика класса, разделенные пробелами. Вывести среднюю
# оценку класса.


with open("mylist.txt", "r") as fin:
    kol = 0
    sum1 = 0
    for s in fin:
        s = s.split()
        print(s)
        kol += 1
        sum1 += int(s[3])
print(f"Средний балл : {sum1 / kol}")
fin.close()
