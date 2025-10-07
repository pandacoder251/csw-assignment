def generatebill(item, price, quantity=1, discount=0, taxrate=0.05):

    subtotal = price * quantity
    discount_amount = subtotal * (discount / 100)
    discounted_total = subtotal - discount_amount
    tax_amount = discounted_total * taxrate
    final_total = discounted_total + tax_amount

    print("\n----- BILL SUMMARY -----")
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: ₹{price}")
    print(f"Discount: {discount}%")
    print(f"Tax Rate: {taxrate * 100}%")
    print(f"Total Payable Amount: ₹{final_total:.2f}")
    print("------------------------\n")

# Function Calls
generatebill("Book", 500)
generatebill("Pen", 20, quantity=10)
generatebill("Bag", 1000, discount=10, taxrate=0.12)
generatebill("Laptop", 50000, 2, 10, 0.05)
