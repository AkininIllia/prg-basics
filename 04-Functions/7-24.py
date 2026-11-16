def f(expression):
    total = int(expression[0])
    for i in range(1, len(expression), 2):
        operator = expression[i]
        digit = int(expression[i + 1])
        if operator == "+":
            total += digit
        elif operator == "-":
            total -= digit
    return total

print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))