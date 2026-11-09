N = int(input("Enter the number of prime numbers to find (N): "))

primes_found = 0
number = 2

print("Prime numbers:", end=" ")

while primes_found < N:
    is_prime = True
    
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
            
    if is_prime:
        print(number, end=" ")
        primes_found += 1
        
    number += 1

print()