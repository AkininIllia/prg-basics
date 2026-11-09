products_count = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

if products_count <= 2:
    total_amount = products_count * product_price
else:
    full_price_items = 2
    discounted_items = products_count - 2
    
    discounted_price = product_price * 0.75
    
    total_amount = (full_price_items * product_price) + (discounted_items * discounted_price)

print(f"Amount to pay: {total_amount:.2f}")