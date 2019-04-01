import random

b=1
while b!=0:
    b=int(input('Come on nostrils - damus. See if you can guess the number I am thinking of between 1 and 100...'))
    a=random.randint(1,100)
    c=10
    while (c !=0):
        c-=1
        if c==0:
            print('Your luck has run out!')   
            break
        if b < a:
            print('Too low Wally')
        elif b > a:
            print('Too high malaka!')
        elif b==a:
            print ('You finally made it! The number was',  + a)
            break
        b=int(input('Try again Sunshine...'))

    b=int(input('To Quit Press 0 or any key to play again...'))
print('Next time Gadget...Next time!')
