import random

while True:
    try:
       b=int(input('Enter 1 to roll the Dice or x to exit>'))
       a=random.randint(1,6)
       print('The dice rolled a ...', a)
    except ValueError:
        break
print('Ciao!')

   
