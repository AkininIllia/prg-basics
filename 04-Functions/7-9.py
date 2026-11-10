def f(number, even):
    digits = [int(char) for char in str(number) if char.isdigit()]
    if even:
        return sum(d for d in digits if d % 2 == 0)
    else:
        return sum(d for d in digits if d % 2 != 0)

print(f(3124, True))
print(f(3124, False))
print(f(20576, False))
print(f(20576, True))
print(f(13115, True))