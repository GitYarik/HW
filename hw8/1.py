a = {1: " pay_houses ", 2: " pay_phone ", 3: " pay_internet ", 4: "exit"}

b = ""
while b != "4":
    b = input(f'ВЫБЕРЕТИ ОПЕРЦИЮ {a}')
    if b == "1":
        from kw import pay_houses

        pay_houses()
    elif b == "2":
        from phone import pay_phone

        pay_phone()
    elif b == "3":
        from internet import pay_internet

        pay_internet()

    elif b == "4":
        print("goodbye")


    else:
        print("erorr")
