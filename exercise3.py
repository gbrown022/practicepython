# GCB 01-OCT-2016

# 1. print all elements from a list of ints that are less than 5
# 2. make a new list that has all the elements less than 5
# 3. Write in one line
# 4. Ask the user for a number and return a list that contains only 
#    elements from the original list that are smaller than the number
#    given by the user

# List:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print('Exercise part 1.')
for number in a:
    if number <= 5:
        print number

print('')

print('Exercise part 2.')
smallValues = []
for number in a:
    if number <= 5:
        smallValues.append(number)

print smallValues
print('')

print('Exercise part 3.')
smallVals = [number for number in a if number <= 5]
print(smallVals)

print('Exercise part 4.')
user_max = int(raw_input('Select the largest number to pick from the list: '))
smallVals2 = [number for number in a if number <= user_max]
print smallVals2
