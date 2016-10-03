import math

num = int(raw_input('Enter an integer: '))

check = int(raw_input('Enter a check interger value: '))

isOdd = num % 2

if num == 4:
    print("Of course 4 is even!")
else:
    if isOdd == 1:
        print('It\'s odd!')
    else:
        print('It\'s even.')

print('Checking...')
if num % check == 0:
    print(check, ' divides ', num, ' evenly.')
else:
    print(check, '  does not divide ', num, ' evenly.')
