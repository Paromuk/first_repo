try:
    number1 = float(input("Введите первое число:"))
    number2 = float(input("Введите второе число:"))
    number3 = float(input("Введите третье число:"))
    number4 = float(input("Введите четвёртое число:"))
    if number1 % 2 !=0 and number2 % 2 !=0 and number3 % 2 !=0 and number4 % 2 !=0:
         print("not found")
    else :
        if number1 % 2 ==0:
            max= number1
        if number2 % 2 ==0 and number2 > max:
            max = number2
        if number3 % 2 ==0 and number3 > max:
            max= number3
        if number4 % 2 ==0 and number4 > max:
            max= number4
        print(f"Наибольшее четное число: {max}")
except ValueError:
    print("Ошибка! Неккоректный ввод переменной")
   

