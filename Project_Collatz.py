import sys
def Collatz(number):
    while True:
        if number == 0:
            sys.exit()
            #print('OK then get outta here!')
            #break
        elif number == 1:
            print('Done it again!')
            break
        elif number % 2 == 0:
            number=(number//2)
            print(number)
        else:
            number=(number*3+1)
            print(number)
            
try:
    Collatz(int(input('Enter a number 0 to exit: ')))
except ValueError:
    print('You must enter a valid number: ')
        
