import random,  logging
logging.basicConfig(level=logging.DEBUG,  format='%(asctime)s-%(levelname)s-%(message)s')

guess=''
while guess not in ('heads','tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess=input()
toss=random.randint(0, 1) #0 ia tails, 1 is heads
if toss==0:
    toss='heads'
else:
    toss='tails'
while True:
    if toss == guess:
        print('You got it!')
        break
    else:
        print('Nope! Guess again!')
        guess=input()
 
