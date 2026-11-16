def f(dice):
    max_streak = 0
    current_streak = 0
    prev_digit = None
    best_digit = None

    for digit in dice:
        if digit == prev_digit:
            current_streak += 1
        else:
            current_streak = 1
            prev_digit = digit

        if current_streak > max_streak:
            max_streak = current_streak
            best_digit = int(digit)

    return best_digit

print(f("5233165554211"))
print(f("2133"))