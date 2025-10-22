paragraph = input ("Enter a paragraph : ")
text = " ".join(paragraph.split()).title()
for v in "AEIOU":
    print(v , "-", str(text.upper().count(v)))