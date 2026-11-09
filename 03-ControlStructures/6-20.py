decimal_number = int(input("Enter decimal number: "))

number = decimal_number
remainders = []

if number == 0:
    remainders.append(0)

while number > 0:
    remainder = number % 2
    remainders.append(remainder)
    number = number // 2

remainders.reverse()

binary_string = "".join(str(r) for r in remainders)

print(f"{decimal_number}(10) = {binary_string}(2)")