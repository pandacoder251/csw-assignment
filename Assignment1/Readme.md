# CSW Assignment – Python Fundamentals and String Capabilities

### Q1. Generate Bill Function
Define a Python function `generatebill(item, price, quantity=1, discount=0, taxrate=0.05)` that calculates and prints the final payable amount after applying discount and tax.

**Steps:**
- Compute subtotal = `price × quantity`
- Apply a discount percentage on the subtotal
- Apply a tax (default 5%) on the discounted amount
- Print a detailed bill: item name, quantity, price, discount, tax, total amount

**Function Calls:**
1. Using only required arguments (item, price)
2. Custom quantity, default discount and tax
3. Named arguments for discount and tax, default quantity
4. All arguments explicitly

### Q2. Simple Calculator
Design a Python program simulating a calculator using `if-elif` statements.  

**Requirements:**
- Allow user to choose operation: add, sub, mul, div, mod
- Input two numbers
- Perform operation and display result
- Handle division/modulus by zero with a warning

### Q3. Number of Days in a Month
- Accept month name as input
- Determine number of days
- For February, ask year to check leap year
- Use dictionary mapping
- Handle invalid inputs

### Q4. Palindrome Checker
Implement two functions:

1. **For-loop approach:** Checks palindrome ignoring case.
2. **Two-pointer approach:** Checks palindrome ignoring case, spaces, punctuation.



### Q5. Decimal to Other Bases
- Read decimal number
- Convert to binary, octal, hexadecimal (without prefixes)
- Count digits in each
- Reverse convert to decimal to verify correctness

**Example Input:** `255`  
**Output:** Binary: `11111111`, Octal: `377`, Hex: `FF`



### Q6. String Encryption & Decryption
- **Encryption:** Reverse string + swap every adjacent pair
- **Decryption:** Reverse process to obtain original string

**Example Input:** `"hello"`  
**Output:** Encrypted: `eholl`, Decrypted: `hello`


### Q7. Sentence Word Sorter
- Read sentence and custom separator
- Split into words, ignore punctuation
- Sort words in reverse alphabetical order
- Join with separator and display

**Example Input:** `"Hello, world! Python."`, Separator: `—`  
**Output:** `world—python—hello`

### Q8. Password Validator
- Validate rules:
  - Minimum 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character `!@#$%`, no whitespaces
- Return `True` if valid, else `False` with list of violated rules


### Q9. Paragraph Processor
- Convert paragraph to title case
- Remove extra spaces
- Count occurrences of vowels A, E, I, O, U

**Example Input:** `"thisisanexampleparagraph"`  
**Output:**  



**Learning Levels:** L2, L3

---

### Q10. Word Frequency Counter
- Read sentence
- Ignore case & punctuation
- Count frequency of each unique word
- Display frequencies sorted alphabetically

**Example Input:** `"Helloworld, hello!"`  
**Output:** `hello: 2 world: 1`


