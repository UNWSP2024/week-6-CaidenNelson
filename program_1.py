


import random
import statistics
from hmac import digest_size
from random import Random
from zoneinfo import reset_tzpath


# Program #1: Random Dice

#Date = 10.11.24
#Programmer = Caiden
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.
tSum = 0
def randDice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)



    # Sum 2 numbers

    global dSum
    dSum = d1+d2
    print(dSum)
    return dSum
    # return sum to calling function
#create loop
for x in range(101):
    randDice()
    #find total dice number
    tSum = tSum + dSum
    #find average
#find average
average = round((tSum/100),2)
print('The average of two dice rolled 100 times rounded to the nearest hundreth is',average)



#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
