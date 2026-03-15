print("Автор: gullsssss")
print("Что-бы начать использовать калькулятор")
First=float(input("Введите первое число: "))
Operation = input("Введите тип операции(+,-,/,*,**) ")
Second=float(input("Введите второе число: "))
#
if Operation == "+":
    result= First+Second
    print("Результат: ", result) 

if Operation == "-":
    result= First-Second
    print("Результат: ", result) 

if Operation == "*":
    result= First*Second
    print("Результат: ", result) 

if Operation == "/":
    if b == 0:
        print("На 0 делить нельзя")
    else:
        result = Fisrt/Second
        print("Результат", result) 
    
if Operation == "**":
    result= First**Second
    print("Результат:", result)
else:
    print("Неизвестная операция")
