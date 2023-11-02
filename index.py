number1 = input(" Enter your First Number: ")
operator = input(" Input which operation you would like to do: +, -, *, /, % : ")
number2 = input("Enter your Second Number: ")

number1 = int(number1)
number2 = int(number2)

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
elif operator == "%":
    print(number1 % number2)
else:
    print("Invalid Operator")
