#1
'''my_str = "i am" , \
      "henry"
    
print(my_str)'''

#2
'''a_list = ['John', 'Bob', 'Paul', 'George', 'Ringo']

for i, name in enumerate(a_list, 1):
    print(i, '.', name, sep=' ')

# *args
def greet_all(*args):
    for name in args:
        print(f"Hello, {name}!")

greet_all("Alice", "Bob", "Charlie")    '''


#**kwargs
'''
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=30, job="Engineer")
'''

#decorator
'''
def shout_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.title()
    return wrapper

@shout_decorator
def say_hello(name):
    return f"Hello, {name}"

print(say_hello("Alice"))
'''

#generator
'''def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num , end = " ")'''