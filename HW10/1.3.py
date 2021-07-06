# В файле записаны символы X, Y, Z. Подсчитать количество
# символов Y и Z, записанных в файле.

with open("st2.txt", "r") as xyz:
    Y = 0
    Z = 0
    for i in xyz:
        x = i.split(",")
        for j in x:
            if j == "Y":
                Y += 1
            elif j == "Z":
                Z += 1
    print(Y)
    print(Z)
