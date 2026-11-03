hours = int(input('Enter number of hours of parking: '))
if hours < 1 and hours >= 0:
    print('Parking fee is 0 PLN')
elif hours >= 1 and hours < 3:
    print('Parking fee is 5 PLN')
elif hours >= 3 and hours < 6:
    print('Parking fee is 15 PLN')
elif hours >= 6:
    print('Parking fee is 20 PLN')
else:
    print('Invalid input')