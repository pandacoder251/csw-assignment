def palindrome_for_loop(s):
    s = s.lower()
    return s == s[::-1]

def palindrome_two_pointer(s):
    import string
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

text = input("Enter a string: ")

print("For-loop Check:", "Palindrome" if palindrome_for_loop(text) else "Not Palindrome")
print("Two-pointer Check:", "Palindrome" if palindrome_two_pointer(text) else "Not Palindrome")
