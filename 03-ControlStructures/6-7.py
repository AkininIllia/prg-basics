age = int(input('Enter your age: '))
if age >= 0 and age < 13:
    print('You are a child.')
elif age >= 13 and age < 19:
    print('You are a teenager.')
elif age >= 19 and age < 64:
    print('You are an adult.')
elif age >= 64:
    print('You are a senior.')
else:
    print('Invalid input')