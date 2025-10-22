def encrypt(text):
    text = text[::-1]
    chars = list(text)
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    return ''.join(chars)

def decrypt(encrypted):
    chars = list(encrypted)
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    return ''.join(chars)[::-1]

msg = input("Enter a string: ")
enc = encrypt(msg)
dec = decrypt(enc)
print(f"Encrypted: {enc}")
print(f"Decrypted: {dec}")