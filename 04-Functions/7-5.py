def is_in_range(number, x, y):
    return x <= number <= y

number = 7
x, y = 2, 15

result = "yes" if is_in_range(number, x, y) else "no"

print(f"A number: {number}")
print(f"Number {number} in the range <{x},{y}>: {result}")