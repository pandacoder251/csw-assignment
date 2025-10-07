import string

sentence = input("Enter a sentence: ")
cleaned = ''.join(ch for ch in sentence if ch not in string.punctuation)
words = cleaned.lower().split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word in sorted(frequency):
    print(f"{word}: {frequency[word]}")
