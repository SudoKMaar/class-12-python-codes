"""Write a random number generator that generates random numbers
between 1 and 6 simulates a dice"""
#--author Abhishek Kumar(14732821)
import random
dice = [x for x in range(1,7)]
while(True):
    choice=input ("Press r to roll the dice or press any key to quit")
    if (choice != 'r'):
        break
    n= random.choice(dice)
    print(n)
