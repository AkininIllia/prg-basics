def f(x, y):
    return sum(n for n in range(x, y + 1) if n % 2 == 0 and n % 3 == 0 and n % 4 != 0)

print(f(1, 20))
print(f(10, 30))