def pay_houses():
    c = float(input("показания горячей вооды"))
    b = float(input("показания холодной вооды"))
    if c < 0 or b < 0:
        print("показаия не могут быть отрицательными ")
    else:
        hotwoter = 3.54
        coldwoter = 1.78
        summ1 = c * hotwoter
        summ2 = b * coldwoter
        summm3 = summ1 + summ2
        print(f"сумма за горячую воду  {summ1}")
        print(f"сумма за холодныю воду {summ2}")
        c = int(input("продолжить 1=да 2=нет"))
        if c == 1:
            v = (input("#карты 16 цифр"))
            n = len(v)
            int(v)
            while True:
                if n == 16:
                    print(f"бщий долг по кварртире {summm3}")
                    price = float(input("введите сумму к оплате"))
                    if price == summm3:
                        print("успешно")
                        chek=int(input("печать чек 1=да 2=нет"))
                        if chek==1:
                            print("возьмите чек")
                            break
                        else:
                            print("пока")
                            break
                    elif price != summm3:
                        print("не успешно сумаа не верна")
                        break
                else:
                    print("не правельно ввели карту")
                    v = (input("еще раз #карты 16 цифр"))
                    n = len(v)
                    int(v)
        else:
            print("goodbye")

