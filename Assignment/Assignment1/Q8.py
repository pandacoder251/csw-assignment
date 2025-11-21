def validate_password(password):
    valid = True
    special_chars = "!@#$%"

    # Rule 1: Length
    if len(password) < 8:
        print("The password must contain at least 8 characters.")
        valid = False

    # Rule 2: Uppercase
    has_upper = any('A' <= ch <= 'Z' for ch in password)
    if not has_upper:
        print("The password must include at least one uppercase letter (A-Z).")
        valid = False

    # Rule 3: Lowercase
    has_lower = any('a' <= ch <= 'z' for ch in password)
    if not has_lower:
        print("The password must include at least one lowercase letter (a-z).")
        valid = False

    # Rule 4: Digit
    has_digit = '0' <= ch <= '9' for ch in password
    if not has_digit:
        print("The password must include at least one digit (0-9).")
        valid = False

    # Rule 5: Special character
    has_special = any(ch in special_chars for ch in password)
    if not has_special:
        print(f"The password must contain at least one special character from the set {special_chars}.")
        valid = False

    # Rule 6: No whitespace
    has_space = any(ch in " \t\n" for ch in password)
    if has_space:
        print("The password should not contain whitespace.")
        valid = False

    return valid


# --- Main Program ---
user_password = input("Enter password: ")
if validate_password(user_password):
    print("Password is VALID")
else:
    print("Password is INVALID")