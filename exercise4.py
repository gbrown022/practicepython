# GCB 02-OCT-2016
import math

userNumber = int(raw_input("enter a number: "))

divisors = []
divisors = [x for x in range(1,userNumber) if userNumber % x == 0]

print('divisors of ', userNumber, 'are: ', divisors)
