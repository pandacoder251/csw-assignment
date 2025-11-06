#set comprehension

# Create a set of even numbers from a list
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = {x for x in numbers if x % 2 == 0}
print("Even numbers:", evens)
print("-"*10)
# Create a set of characters from a string, excluding vowels
text = "set comprehension example"
vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = {char for char in text if char.isalpha() and char.lower() not in vowels}
print("Consonants:", consonants)
print("-"*10)'''


#set comprehension
#1
names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
unique_names = {i for i in names}
print(unique_names)  # Output: {'Alice', 'Bob', 'Charlie'}


