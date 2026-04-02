language = input("Select language(eng,fra,ua): ")
if language == "fra":
    print("Auteur: gullsssss(r0tyanka)")
    print("Pour commencer à utiliser la calculatrice")
    First = float(input("Saisissez le premier nombre: "))
    Operation = input("Entrez le type de transaction(+,-,/,*,**) ")
    Second = float(input("Entrez le deuxième numéro: "))

    if Operation == "+":
        result = First + Second
        print("Résultat: ", result) 
    elif Operation == "-":
        result = First - Second
        print("Résultat: ", result) 
    elif Operation == "*":
        result = First * Second
        print("Résultat: ", result) 
    elif Operation == "/":
        if Second == 0:
            print("On ne peut pas diviser par 0")
        else:
            result = First / Second
            print("Résultat: ", result) 
    if Operation == "**":
        result = First ** Second
        print("Résultat: ", result)
    else:
        print("Erreur inconnue")
        
if language == "eng":
    print("Author: gullsssss(r0tyanka)")
    print("To start using a calculator")
    First = float(input("Input first number: "))
    Operation = input("Select a type operation(+,-,/,*,**): ")
    Second = float(input("Input second number: "))

    if Operation == "+":
        result = First + Second
        print("Result: ", result) 
    elif Operation == "-":
        result = First - Second
        print("Result: ", result) 
    elif Operation == "*":
        result = First * Second
        print("Result: ", result) 
    elif Operation == "/":
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
    elif Operation == "-":
        result = First - Second
        print("Результат: ", result) 
    elif Operation == "*":
        result = First * Second
        print("Результат: ", result) 
    elif Operation == "/":
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
        
if language == "ru":
    print("Автор: gullsssss(r0tyanka)")
    print("Чтобы использовать калькулятор")
    First = float(input("Введите первое число: "))
    Operation = input("Введите тип операции(+,-,/,*,**) ")
    Second =float(input("Введите второе число: "))
    
    if Operation == "+":
        result = First + Second
        print("Результат: ", result) 
    elif Operation == "-":
        result = First - Second
        print("Результат: ", result) 
    elif Operation == "*":
        result = First * Second
        print("Результат: ", result) 
    elif Operation == "/":
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
        
