def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >=num3:
        return num1
    elif num2>= num1 and num2 >=num3:
        return num2
    else:
        return num3
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
max_num = max_num(num1, num2, num3)
print("The greatest number is:", max_num)
