import math
import datetime

now = datetime.datetime.now()

# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that 
# they will turn 100 years old.

person = raw_input('Enter your name: ')
print('Your name is: ', person);

age = int(raw_input('Enter your age: '))
print('Your age is: ', age);

year = now.year
current_year = year

year_tobe_100 = (100 - age) + current_year 

num_times = int(raw_input('Enter the number of times to print the message: '))

for x in range (0,num_times):
    print(person, ' , you will be 100 years old in the year, ', year_tobe_100)
