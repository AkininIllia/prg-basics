def f(number):
    num_str = str(number)
    digit_counts = {}
    
    for digit in num_str:
        digit_counts[digit] = digit_counts.get(digit, 0) + 1
        
    return sum(int(digit) * count for digit, count in digit_counts.items() if count > 1)

print(f(1027))
print(f(230335))
print(f(513553007))