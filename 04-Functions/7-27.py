def f(product_code):
    first_three_sum = sum(int(digit) for digit in product_code[:3])
    control_digit = int(product_code[3])
    return first_three_sum % 7 == control_digit

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))