from random import randint


def pay_internet():
    a = randint(10, 20)
    print(f"{a} $ сумма задолженности")
    c = int(input("продолжить 1=да 2=нет"))
    if c == 1:

        v = (input("#карты 16 цифр"))
        n = len(v)
        int(v)
        while True:
            if n == 16:
                print("карта введена верна")
                price = float(input("введите сумму к оплате"))
                if price == a:
                    print("успешно")
                    break
                elif price != a:
                    print("не успешно сумаа не верна")
                    break
            else:
                print("не правельно ввели карту")
                v = (input("еще раз #карты 16 цифр"))
                n = len(v)
                int(v)
    else:
        print("goodbye")
