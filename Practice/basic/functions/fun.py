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
print("The area of the circle with radius", radius, "is:", area)'''

