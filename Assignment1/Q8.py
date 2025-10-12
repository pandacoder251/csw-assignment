def validate_password(pass):
    valid = True
    special_chars = "!@#$%"

    #Rule1
    if len(password)<8:
        print("The password must contain atleast 8 characters")
        valid = False

    #Rule2
    has_upper = False
    for ch in password:
        if 'A' <= ch <= 'Z':
            has_upper = True
            break

        if not has_upper :
            print("The password must include atleast one uppercase letter(a-z)")
            valid = False

    #Rule 3   

    has_lower = False
    for ch in password:
        if 'a' <= ch <= 'z':
            has_upper = True
            break

        if not has_lower :
            print("The password must include atleast one lowercase letter(A-Z)")
            valid = False

    #Rule 5

    has_digit = False
    for ch in password:
        if '0' <= ch <= '9':
            has_digit = True
            break

        if not has_digit :
            print("The password must contain one special character from the set !@#$%")
            valid = False 


     #Rule 6

    has_space = False
    for ch in password:
        if ch== " " or ch== "\t" or ch== "\n":
            has_space = True
            break

        if not has_space :
            print("The password should not have whitespace.")
            valid = False


user_pasword = input("Enter password: ")
if validate_password(user_password):
    print("password is valid")

else:
    print("Password is invalid")
