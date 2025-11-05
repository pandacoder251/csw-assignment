#1
'''def compare_no_case(str1, str2):
    return str1.casefold() == str2.casefold()
print(compare_no_case("cat", "CAT"))  # True
s ="HI"
print(s.lower())  #hi '''
#2
'''
first = 'will'
second = 'arm'
print(first>second)  
print(first<second)  
print(first==second) 
print(first!=second) 
print(first>=second) 
print(first<=second) '''
#3
'''s = 'PythonisFun'
s1 =s[2:6]
s2 = s[-4:-1]
s3 = s[1:-1]
s4 = s[::3]
s5 = s[5:9:2]
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)'''


#4
'''print(ord('a'))
print(chr(66))

s = "doggy"
for ch in s:
    ch = ord(ch)
    print(ch , end = " ")'''

#5
'''s = 'Python is Fun'
print("Length = " , len(s))
print("Largest Char = " , max(s))
print("Smallest Char = " , min(s))
print("Count of 'n' = " , s.count('n'))
print("Index of 'i' = " , s.index('i'))
print ("count p : " , s.count('P'))
print("index F : " , s.index('F'))'''


#6
'''text = "I like apple and apples."
print(text.replace("apple", "banana"))  # I like banana and bananas.
print(text.replace("apples", "oranges" , 1))'''

#7
'''text = "python programming is fun"
print(text.startswith("py"))
print(text.startswith("pro",7))
print(text.endswith("fun"))
print(text.endswith("FUN"))
print(text.endswith("on", 0, 21))'''



#9
'''s = "***Hello World***"
print(s.lstrip('*'))
print(s.rstrip('*'))
print(s.strip('*'))
print(s.replace('*', '#'))
print(s.replace('*', '#', 1))
print(s + 'People')
print(s * 2)
print(s.center(20, '-'))
print(s.ljust(20, '-'))
print(s.rjust(20, '-'))'''

#8
'''s = "python Programming  "
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())

s = "Programming in Python Programming"
print(s.lstrip("Programming"))
print(s.rstrip("Programming"))
print(s.strip("Programming"))'''


#9
'''print(bin(10),hex(10),oct(10))
print(int('0b1010',2))
print(int('0xa',16))
print(int('0o12',8))
print(format(10,'b'))
print(format(10,'x'))
print(format(10,'o'))'''

#10
'''s1 = "python123"
s2 = "python"
s3 = "12345"
print(s1.isalnum())
print(s2.isalpha())
print(s3.isdigit())
print(s2.isdecimal())
print(s2.isdigit())
print(s2.isidentifier())
print(s2.isprintable())
print(s2.isspace())
print(s2.istitle())
print(s2.islower())
print(s2.isupper())'''


#11
'''alphabet = ord('A')
list = []
for i in range(26):
    list.append(chr(alphabet + i))
print(list)

s = ''.join(list)
print(s)

s= "python is fun"
rev = reversed(s)
print(rev)
rev = ''.join(rev)
print(rev)'''

#justification methods
s = "hello"
print(s.ljust(10,'-'))
print(s.rjust(10,'-'))
print(s.center(10,'-'))

n = "24"
print(n.zfill(10))
print("-24".zfill(10))
print("+24".zfill(10))