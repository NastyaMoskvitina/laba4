def num1(chislo):
    return chislo % 3 == 0
chislo = int(input("Введите число: "))
print(num1(chislo))

def zadacha2():
    def num2(chislo):
        return 100 / chislo
    try:
        chislo = int(input("Введите число: "))
        print(num1(num2(chislo)))
    except ValueError:
        print("Это не число.")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")

def zadacha3():
        do = input("Введите дату: ")
        dat = do.split(".")
        return int(dat[0]) * int(dat[1]) == int(dat[2][2:4])
        print(do)

def zadacha4():
        sum1,sum2 = 0,0
        da = input("Введите номер билета: ")
        ser = int(len(da)/2)
        for i in range(ser):
            sum1 += int(da[i])
        for i in range(ser, len(da)):
            sum2 += int(da[i])
        if sum1 == sum2:
           print("Билет счастливый")
        else:
           print("Билет не счастливый")
        print(da)

zadacha2()
zadacha3()
zadacha4()
"лорло