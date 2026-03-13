print("Что-бы начать использовать калькулятор")
a=float(input("Введите первое число: "))
c = input("Введите тип операции(+,-,/,*,**) ")
b=float(input("Введите второе число: "))
#
if c == "+":
	result=(a+b)
    print("Результат: ",result)

if c == "-":
	result=(a-b)
    print("Результат: ",result)

if c == "*":
	result=(a*b)
    print("Результат: ",result)

if c == "/":
	result=(a/b)
    print("Результат: ",result)
    if b == "0":
		print("На 0 делить нельзя")
    
if c == "**":
	result=(a**b)
	print("Результат:",result)
