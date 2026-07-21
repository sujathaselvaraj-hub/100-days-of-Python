no1= int(input("Enter first number:"))
no2= int(input("Enter second number:"))
operator=str(input("Enter the operator:"))
if operator=='+':
    add= no1+ no2
    print(add, "addition of two numbers")
if operator=='-':
    minus = no1-no2
    print(minus, "subtraction of two numbers")
if operator=='*':
    multiply= no1* no2
    print(multiply, "multiplication of two numbers")
if operator=='/':
    divide= no1/no2
    print(divide, "division of two numbers")
if operator=='%':
    modulus=no1%no2
    print(modulus, "modulus of two numbers")
if operator=='**':
    exp=no1**no2
    print(exp, "exponentiation of two numbers")
if operator=='//':
    floor=no1//no2
    print(floor, "floor division of two numbers")
