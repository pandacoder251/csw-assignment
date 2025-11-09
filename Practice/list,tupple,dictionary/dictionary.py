dict = {
    "name" : "abcd" , "age" : 3 , "branch" : "cse"
}

print(dict)
print(dict.get("name"))
print(dict.get("section" , "Not found"))

#dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}

print(squares)



