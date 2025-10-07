text = input("Enter a paragraph: ")

cleaned = ' '.join(text.split()).title()

vowels = "AEIOU"
counts = {v: cleaned.upper().count(v) for v in vowels}

print("Processed Text:", cleaned)
print("Vowel Counts:", ', '.join([f"{v}: {counts[v]}" for v in vowels]))
