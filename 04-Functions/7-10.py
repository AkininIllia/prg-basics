def f(x, y):
    return sum(1 for n in range(x, y + 1) if n < 0 and n % 2 == 0)

print(f(-7, 8))
print(f(-1, 11))