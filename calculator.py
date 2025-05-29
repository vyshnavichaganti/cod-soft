# Simple Calculator

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose the operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

# Perform calculation based on user choice
if operation == '1':
    result = num1 + num2
    op_symbol = '+'
elif operation == '2':
    result = num1 - num2
    op_symbol = '-'
elif operation == '3':
    result = num1 * num2
    op_symbol = '*'
elif operation == '4':
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        exit()
    result = num1 / num2
    op_symbol = '/'
else:
    print("Invalid operation choice.")
    exit()

print(num1, op_symbol, num2, "=", result)