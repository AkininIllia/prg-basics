price = float(input("Enter price: "))
discount_pct = float(input("Enter discount %: "))

reduction = price * (discount_pct / 100)
price_with_discount = price - reduction

print(f"Price with discount: {price_with_discount:.2f}")
print(f"Reduction: {reduction:.2f}")