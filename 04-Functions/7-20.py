def f(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            count += 1
    return num

print(f(1))
print(f(5))