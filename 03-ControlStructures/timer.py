###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 5:
    print(countdown)
    countdown -= 1
    time.sleep(1)  # Wait for 1 second
# Display the last five seconds in words
for i in range(5, 0, -1):
    if i == 5:
        print("five")
    elif i == 4:
        print("four")
    elif i == 3:
        print("three")
    elif i == 2:
        print("two")
    else:
        print("one")
    time.sleep(1)

print("Time's up!")
