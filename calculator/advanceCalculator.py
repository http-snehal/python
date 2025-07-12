num1 = float(input("enter the number 1: "))
op = input("enter the operator: ")
num2 = float(input("enter the number 2: "))

if op == "+":
    print("The sum is:", num1 + num2)
elif op == "-":
    print("The difference is:", num1 - num2)
elif op == "*":
    print("The product is:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("The quotient is:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")

elif op == "%":
    if num2 != 0:
        print("The modulus is:", num1 % num2)
    else:
        print("Error: Division by zero is not allowed.")

elif op == "**":
    print("The power is:", num1 ** num2)





