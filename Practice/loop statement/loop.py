''' n = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("The sum of the first", n, "positive integers is:", sum)

n = int(input("Enter a positive integer: "))
rev = 0
while n> 0:
    dg = n % 10
    rev = rev * 10 + dg
    n = n // 10
print("The reverse of the given number is:", rev)'''

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
