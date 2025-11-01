'''def right_tri():
  l = float(input("Enter the length of the triangle's leg: "))
  p= float(input("Enter the height of the triangle's leg: "))
  h = (l**2 + p**2)**0.5
  print("The length of the hypotenuse is:", h)

right_tri() 

#2 method 2

def right_tri(l, p):
  h = (l**2 + p**2)**0.5
  print("The length of the hypotenuse is:", h)

right_tri(3, 4)'''


#3
'''def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n*factorial(n-1)
num = int(input("Enter a number to find its factorial: "))
result = factorial(num)
print("The factorial of", num, "is", result)'''

#4
'''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): # check divisibility up to the square root of n
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")  '''

#5
'''def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n] 
num = int(input("Enter the number of Fibonacci terms to generate: "))
fib_sequence = fibonacci(num)
print("Fibonacci sequence up to", num, "terms:", fib_sequence)'''


#6
'''def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is", result)'''

#7
'''def armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == n   
num = int(input("Enter a number to check if it's an Armstrong number: "))
if armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")'''

#8
'''import math
def func_area_circle(r):
    return math.pi * r**2
radius = float(input("Enter the radius of the circle: "))
area = func_area_circle(radius)
print("The area of the circle with radius", radius, "is:", area)

#global & local variable

#1
global_var_count = 0
def increment_count():
    global global_var_count
    while global_var_count < 5:
        print("Inside function, count:", global_var_count)
        global_var_count += 1
    return global_var_count
increment_count()
print("Outside function, count:", global_var_count)


#2
def num_check():
    while True:
        num = int(input("Enter a positive number: " )) #local variable
        if num % 2 == 0:
            print("You entered an even number:", num)
        else:
            print("You entered an odd number:", num)
        if num == -1:
            print("Negative number entered, exiting the loop.")
            break
num_check()        '''


#3
'''item_count = 0
def add_item():
    global item_count 
    item_name = input("Enter item name: ")
    item_count += 1
    print(f"'{item_name}' added. Total items so far: {item_count}")
def show_count():
    print(f"\nTotal number of items added: {item_count}")
while True:
    user_input = input("Type 'add' to add item or 'done' to stop: ").lower()
    if user_input == "add":
        add_item()
    elif user_input == "done":
        break
    else:
        print("Invalid input. Please type 'add' or 'done'.")
show_count()'''



'''
items = [] #list to store items
def add_item():
    item_name = input("Enter item name: ")
    items.append(item_name)
    print(f"'{item_name}' added. Total items so far: {len(items)}")
def show_count():
    print(f"\nTotal number of items added: {len(items)}")
while True:
    user_input = input("Type 'add' to add item or 'done' to stop: ").lower()
    if user_input == "add":
        add_item()
    elif user_input == "done":
        print("Exiting item addition.")
        print("Final items:", items)
        break
    else:
        print("Invalid input. Please type 'add' or 'done'.")
show_count()'''