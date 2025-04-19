import math

while True:
    print("Welcome to the calculator")
    number1=int(input("Enter number 1  or Enter -0 exit :"))
    if number1 == -0:
        print("this program is stop")
        break
    else:
        number2=int(input("Enter number 2 :"))
        op=input("Enter operator (+ - * /)")

        if op == '+':
            total=number1 +number2
            print(total)
        elif op == '-':
            total=number1-number2
            print(total)
        elif op == '*':
            total=number1 * number2
            print(total)
        else:
            total=number1 / number2
            print(total)
        print("__________________________________________________________________________")