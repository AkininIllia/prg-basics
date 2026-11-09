previous_price = 200.00
current_price = 140.00

print(f"Current product price: {current_price:.2f}")
print(f"Previous product price: {previous_price:.2f}")

price_drop_percentage = ((previous_price - current_price) / previous_price) * 100

if price_drop_percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(round(price_drop_percentage))}%")