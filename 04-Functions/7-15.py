def f(detector):
    current_people = 0
    max_people = 0
    
    i = 0
    while i < len(detector):
        if detector[i] == "+":
            current_people += 1
            i += 1
        elif detector[i:i+2] == "--":
            current_people -= 1
            i += 2
        else:
            i += 1
            
        if current_people > max_people:
            max_people = current_people
            
    return max_people >= 3

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))