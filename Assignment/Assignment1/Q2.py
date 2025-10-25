operation = input("Enter operation (add/sub/mul/div/mod): ").strip().lower()
num1 = (input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "add":
    print("Result:", num1 + num2)
elif operation == "sub":
    print("Result:", num1 - num2)
elif operation == "mul":
    print("Result:", num1 * num2)
elif operation == "div":
    if num2 == 0:
        print("Error: Division by zero not allowed.")
    else:
        print("Result:", num1 / num2)
elif operation == "mod":
    if num2 == 0:
        print("Error: Modulus by zero not allowed.")
    else:
        print("Result:", num1 % num2)
else:
    print("Invalid operation selected.")
