#В текстовый файл построчно записаны фамилия и имя учащихся
#класса и его оценка за контрольную. Вывести на экран всех учащихся,
#чья оценка меньше 3 баллов и посчитать средний балл по классу.

f=open("st1.txt")
otmetka=0
while True:
    s=f.readline().split()
    a, b = map(int, s)

    if not s: break
    age = float(s[3])
    otmetka+=age/4
    if age<3:
         print(s)
print(otmetka)

f.close()

