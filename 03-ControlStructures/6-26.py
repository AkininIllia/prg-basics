CORRECT_PIN = "0805"

max_attempts = 3

for attempt in range(max_attempts):
    entered_pin = input("Enter the PIN code: ")
    
    if entered_pin == CORRECT_PIN:
        print("Correct! Access granted.")
        break
    else:
        print("Incorrect...")
else:
    print("Sorry, your payment card has been blocked.")
