print("Select language(eng,ru,ua)")
language = input()
if language == "ru":
    print("Автор: gullsssss(r0tyanka)")
    print("Что-бы начать использовать калькулятор")
    First = float(input("Введите первое число: "))
    Operation = input("Введите тип операции(+,-,/,*,**) ")
    Second = float(input("Введите второе число: "))

    if Operation == "+":
        result = First + Second
        print("Результат: ", result) 
    if Operation == "-":
        result = First - Second
        print("Результат: ", result) 
    if Operation == "*":
        result = First * Second
        print("Результат: ", result) 
    if Operation == "/":
        if Second == 0:
            print("На 0 делить нельзя")
        else:
            result = First / Second
            print("Результат: ", result) 
    if Operation == "**":
        result = First ** Second
        print("Результат: ", result)
    else:
        print("Неизвестная ошибка")
        
if language == "eng":
    print("Author: gullsssss(r0tyanka)")
    print("To start using a calculator")
    First = float(input("Input first number: "))
    Operation = input("Select a type operation(+,-,/,*,**): ")
    Second = float(input("Input second number: "))

    if Operation == "+":
        result = First + Second
        print("Result: ", result) 
    if Operation == "-":
        result = First - Second
        print("Result: ", result) 
    if Operation == "*":
        result = First * Second
        print("Result: ", result) 
    if Operation == "/":
        if Second == 0:
            print("cannot be divided by 0: ")
        else:
            result = First / Second
            print("Result: ", result) 
    if Operation == "**":
        result = First ** Second
        print("Result: ", result)
    else:
        print("Unknown error: ")
    
if language == "ua":
    print("Автор: gullsssss(r0tyanka)")
    print("Щоб почати використовувати калькулятор")
    First = float(input("Введіть перше число: "))
    Operation = input("Введіть тип операции(+,-,/,*,**) ")
    Second =float(input("Введіть другое число: "))

    if Operation == "+":
        result = First + Second
        print("Результат: ", result) 
    if Operation == "-":
        result = First - Second
        print("Результат: ", result) 
    if Operation == "*":
        result = First * Second
        print("Результат: ", result) 
    if Operation == "/":
        if Second == 0:
            print("На 0 ділити не можно")
        else:
            result = First / Second
            print("Результат: ", result) 
    if Operation == "**":
        result = First ** Second
        print("Результат: ", result)
    else:
        print("Невідома помилка")
