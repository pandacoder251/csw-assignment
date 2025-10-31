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

'''a = int(input("enter 1st num: "))
b = int(input("enter 2nd num: "))
c = int(input("enter 3rd num: "))
if a < b and b < c:
    print(" c is largest")
elif a> b and b > c:
    print("a is the largest")

else:
    print("b is greatest")    '''


'''
m1= float(input("enter mark 1 : "))
m2 = float(input("enter mark2 : "))
m3 = float(input("enter mark3 = "))
m4 = float(input("enter mark4 = "))
m5 = float(input("enter mark5 = "))

total = (m1+m2+m3+m4+m5)
avg = total // 5
print("Total Marks : " , total)
print("Average Marks : " , avg)
if avg > 90 and avg <= 100:
    print("Grade : O" )
elif avg > 80 and avg <= 89:
    print("Grade : A" )
elif avg > 70 and avg <= 79:
    print("Grade : B" )
elif avg > 60 and avg <= 69:
    print("Grade : C" )

else:
    print("Fail :( ")
'''

'''
x = 10 #global
def fun():
    
    print(x)
     #global y
    y = 3 
    print(y)

fun()
print(y)'''