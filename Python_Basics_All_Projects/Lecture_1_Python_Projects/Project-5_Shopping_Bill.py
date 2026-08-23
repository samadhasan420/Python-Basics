print("\n----- Shopping Bill -----")

product1 = input("\n\nProduct1 name: ")
price1 = float(input("Price: $"))
quantity1 = float(input("Quantity: "))
total1 = (price1 * quantity1)

product2 = input("\nProduct2 name: ")
price2 = float(input("Price: $"))
quantity2 = float(input("Quantity: "))
total2 = (price2 * quantity2)

product3 = input("\nProduct3 name: ")
price3 = float(input("Price: $"))
quantity3 = float(input("Quantity: "))
total3 = (price3 * quantity3)

final = (total1 + total2 + total3)

print("\nProduct1:", product1)
print("Price:", price1)
print("Quantity", quantity1)
print("Total:", "$"+str(total1))

print("\nProduct2:", product2)
print("Price:", price2)
print("Quantity", quantity2)
print("Total:", "$"+str(total2))

print("\nProduct3:", product3)
print("Price:", price3)
print("Quantity", quantity3)
print("Total:", "$"+str(total3))

print("-------------------------" + "\nFinal Bill: $"+str(final) + "\n-------------------------")