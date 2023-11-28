#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number
if last < 0:
    last = last * -1
last = last % 10    
if last > 5:
    str = "and is greater than 5"
if last == 0:
    str = "and is 0"
if last < 6 and last != 0:
    str = "and is less than 6 and not 0"
print("Last digit of", number, "is", last, str)
