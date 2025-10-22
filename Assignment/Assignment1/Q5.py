decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)[2:]
octal = oct(decimal)[2:]
hexa = hex(decimal)[2:]

print(f"Binary: {binary} (Digits: {len(binary)})")
print(f"Octal: {octal} (Digits: {len(octal)})")
print(f"Hexadecimal: {hexa.upper()} (Digits: {len(hexa)})")

print("\nVerification:")
print("Binary to Decimal:", int(binary, 2))
print("Octal to Decimal:", int(octal, 8))
print("Hexadecimal to Decimal:", int(hexa, 16))