def multiply_numbers(a, b):
    return a * b

print("Welcome to Multi-Bot!")
repeats = int(input("How many sums do you want to do?"))

for i in range(repeats):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = multiply_numbers(num1, num2)
    print(f"Result: {result}")
