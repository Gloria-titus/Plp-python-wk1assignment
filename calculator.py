num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")
    
operations = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2, '/': num1 / num2 if num2 != 0 else 'Error: Division by zero is not allowed.'}
    
result = operations.get(operation, "Invalid operation. Please enter one of +, -, *, or /.")

print(f"{num1} {operation} {num2} = {result}")


    