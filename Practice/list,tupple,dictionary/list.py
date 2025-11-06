'''lst = ["apple", "banana", "cherry"] 
print(lst)

lst = list(("apple", "banana", "cherry"))  
print(lst) 
lst = list(())
print(lst)'''

#2
'''lst = [2, 1, "two", 3.0]     # initial list
lst.append(4)             # adds 4 to the end
print(lst)                # [1, 'two', 3.0, 4]

lst.remove(1)             # removes the first occurrence of value 1
print(lst)                # ['two', 3.0, 4]

lst.pop(2)                # removes element at index 2 (which is 4)
print(lst)                # ['two', 3.0]
lst.insert(1, "inserted") # inserts "inserted" at index 1
print(lst)    '''            # ['two', 'inserted', 3.0]


#3
'''a = [1, 2, 3, 4, 5] 
b = a.copy()
print("1:-", b) 
b = a[:] #memory address will be different
print("2:-", b)    
b.append(4) 
print(b) 
a = b[:]

print(a)  '''

#deep copy
'''import copy
a = [1, 2, 3] 
b = copy.deepcopy(a)
print("1:-", b) 
b[0] = 'X'
print("2:-", b)    
print("3:-", a)'''

#slicing
'''a= [1,2,3,4,5,6,7,8,9]
b = a[2:5]
print(b)  # [3, 4, 5]
c = a[:3]
print(c)  # [1, 2, 3]
d = a[6:]
print(d)  # [7, 8, 9]'''

#enumerate
'''lst = ['a', 'b', 'c']
for index, value in enumerate(lst):
    print(index, value)
print("-"*5)    
for i , value in enumerate(lst, start=1):
    print(i, value)'''


#extend
'''lst = [1, 2, 3]
lst2 = [4, 5, 6]
lst.extend(lst2)
print(lst)  # [1, 2, 3, 4, 5, 6]    
lst.extend([7, 8])
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8]

#clear
lst.clear()
print(lst)  # []'''

#pop
'''lst = [10, 20, 30, 40, 50]
popped_element = lst.pop(2)  # removes element at index 2
print("Popped Element:", popped_element)  # Popped Element: 30
print("Updated List:", lst)  # Updated List: [10, 20, 40, 50]
#insert
lst.insert(2, 25)  # inserts 25 at index 2
print("After Insertion:", lst)  # After Insertion: [10, 20, 25, 40, 50]

#remove
lst.remove(40)  # removes the first occurrence of value 40
print("After Removal:", lst)  # After Removal: [10, 20, 25, 50]'''

#count
'''lst = [10, 20, 10, 30, 10]
count_10 = lst.count(10)
print("Count of 10:", count_10)  # Count of 10: 3
#sort
lst.sort()
print("Sorted List:", lst)  # Sorted List: [10, 10, 10, 20, 30]
#reverse
lst.reverse()
print("Reversed List:", lst)  # Reversed List: [30, 20, 10, 10, 10]''' 

#list as stack
'''stack  = []
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after pushes:", stack)  # Stack after pushes: [1, 2, 3]
print("Popped element:", stack.pop())  # Popped element:    3    

print("Stack after pop:", stack)  # Stack after pop: [1, 2]
#isempty
print("Is stack empty? " ,not stack)   
stack.pop() 
print(f"Stack after third pop: {stack}")   
 
print(f"Is stack empty? {len(stack)==0}")  '''


'''
#rpn evaluation
# Stack implemented using a list
stack = []

# Function to push an element into the stack
def push(x):
    stack.append(x)
    print(x, "pushed into stack.")

# Function to pop an element from the stack
def pop():
    if isempty():
        print("Stack is empty! Cannot pop.")
        return None
    else:
        return stack.pop()

# Function to check if stack is empty
def isempty():
    return len(stack) == 0

# Function to display all elements
def display():
    if isempty():
        print("Stack is empty!")
    else:
        print("Stack elements:", stack)

# Function to evaluate Reverse Polish Notation (RPN)
def evaluate_rpn(expression):
    for i in expression:
        if i.isdigit():   # Operand
            push(int(i))
        else:                 # Operator
            val2 = pop()
            val1 = pop()
            if i == '+':
                push(val1 + val2)
            elif i == '-':
                push(val1 - val2)
            elif i == '*':
                push(val1 * val2)
            elif i == '/':
                push(val1 // val2)
    return pop()

# --- Main Menu ---
while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Evaluate RPN")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        x = input("Enter element to push: ")
        push(x)
    elif choice == '2':
        popped = pop()
        if popped is not None:
            print("Popped element:", popped)
    elif choice == '3':
        display()
    elif choice == '4':
        expr = input("Enter RPN Expression (e.g., 534*+): ")
        result = evaluate_rpn(expr)
        print("Result:", result)
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.")'''


#listcomprehension
from functools import reduce  # Corrected 'impory' to 'import'

'''def add(x, y):
    return x + y

c = [1, 2, 3, 4, 5, 6]
total = reduce(add, c)
print(total)  # Output: 21

# Using a lambda function instead of a named function
c = [1, 2, 3, 4, 5, 6]
total = reduce(lambda x, y: x + y, c)
print(total)  # Output: 21'''


#passing argument throuh a list:-

def set_list_vals(list_arg):
    list_arg[0] = 100
    list_arg[1] = 200
    list_arg[2] = 250
a_list = [0,0,0]
set_list_vals(a_list)
print(a_list)