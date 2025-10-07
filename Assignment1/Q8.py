def validatepassword(password):
    errors = []
    if len(password) < 8:
        errors.append("Must contain at least 8 characters.")
    if not any(ch.isupper() for ch in password):
        errors.append("Must include at least one uppercase letter.")
    if not any(ch.islower() for ch in password):
        errors.append("Must include at least one lowercase letter.")
    if not any(ch.isdigit() for ch in password):
        errors.append("Must include at least one digit.")
    if not any(ch in "!@#$%" for ch in password):
        errors.append("Must include at least one special character (!@#$%).")
    if any(ch.isspace() for ch in password):
        errors.append("Must not contain any whitespace.")
    if errors:
        return False, errors
    return True, []

pw = input("Enter password: ")
valid, issues = validatepassword(pw)
if valid:
    print("Password is valid.")
else:
    print("Password is invalid:")
    for e in issues:
        print("-", e)
