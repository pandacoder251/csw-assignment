'''a = 3
b = 4
print("a = " ,a )
print(" b = " ,b)
a = a+b
b = a- b
a = a-b
print("a = " ,a )
print(" b = " ,b)'''

'''a = float(input("enter a number: "))
b = float (input("enter a number:"))
oper = input("enter the operation + , - , *, ** , /,//,% : ")

if oper == '+':
    print("a+b = ", a+ b)
elif oper == '-':
    print("a-b = " ,a+ b)
elif oper == '*':
    print("a*b = ", a* b)
elif oper == '**':
    print("a^b = ", a**b)
elif oper == '/':
    if b == 0 :
        print("Division by Zero")
    print("a/b = ", a/b)     
elif oper == '//':
    if b == 0 :
        print("Division by Zero")
    print("a//b = ", a//b)   
elif oper == '%':
    if b == 0 :
        print("Division by Zero")
    print("a%b = ", a%b)          
else : 
    print("Invalid Operator!")            '''

a = int(input("enter 1st num: "))
b = int(input("enter 2nd num: "))
c = int(input("enter 3rd num: "))
if a < b and b < c:
    print(" c is largest")
elif a> b and b > c:
    print("a is the largest")

else:
    print("b is greatest")    