#1
''' n = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("The sum of the first", n, "positive integers is:", sum)
#2
n = int(input("Enter a positive integer: "))
rev = 0
while n> 0:
    dg = n % 10
    rev = rev * 10 + dg
    n = n // 10
print("The reverse of the given number is:", rev)'''
#3
#n = int(input("Enter a positive integer: "))
'''count = 0
while n> 0:
    dg = n%10
    count += 1
    n = n//10
print("The number of digits in the given number is:", count)'''

'''while True:
    password = input("enter the password: ")
    if password == "python123":
        print("Access granted")
        break
    else:
        print("Access denied")'''



#jump statement

#1
'''n = int(input("Enter a positive integer: "))
i = 0
while i < n:
    i += 1
    if i%3 == 0:
        continue 
    print(i)'''

#2
'''sum = 0
while True:
    num = int(input("Enter a  integer: "))
    if num > 0:
        sum += num
    elif num<0:
        print("Looping terminated.")
        print("Sum of positive numbers entered:", sum)
        break
    
    print("You entered:", num)
    print("Enter the next number (negative to quit):")
    continue'''


#3
'''password = "123"
while True:
    user = input("Enter the secrete number : ")
    if user != password:
        print("Wrong number, try again")
        continue
    elif user == "exit":
        print("Exiting the loop")
        break
    else:
        print("Access granted")
        break'''


#for loop 
#1
'''def sum_of_divior(n):
    total_sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            total_sum += i
    return total_sum
num = int(input("Enter a positive integer: "))
result = sum_of_divior(num)
print("The sum of all divisors of", num, "is:", result)'''

#2
'''def fib_without_recursion(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
num = int(input("Enter the number of Fibonacci terms to generate: "))
fib_sequence = fib_without_recursion(num)
print("Fibonacci sequence up to", num, "terms:", fib_sequence)'''

#3
