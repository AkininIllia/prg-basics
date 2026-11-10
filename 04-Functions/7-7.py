def f(binary_number):
    return all(char in "01" for char in binary_number)

print(f("101101"))
print(f("1311a10100"))