human_years = float(input("Enter the dog's age in human years: "))

if human_years < 0:
    print("Age cannot be negative.")
elif human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 21 + (human_years - 2) * 4

if dog_years.is_integer():
    dog_years = int(dog_years)

print(f"The dog's age in dog's years is {dog_years} years")