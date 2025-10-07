import string

sentence = input("Enter a sentence: ")
separator = input("Enter a custom separator: ")

cleaned = ''.join(ch for ch in sentence if ch not in string.punctuation)
words = cleaned.lower().split()
words.sort(reverse=True)

result = separator.join(words)
print("Output:", result)
