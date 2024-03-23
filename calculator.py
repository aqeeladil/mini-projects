num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator: ")

if op == "+":
    print("The addition is", num1 + num2)

elif op == "-":
    print("The substraction is", num1 - num2)

elif op == "*":
    print("The multiplication is", num1 * num2)

elif op == "/":
    print("The division is", abs(num1 / num2))
else:
    print("Enter valid operator")


