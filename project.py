import random 

number = random.randint(1,100)

print('welcome to GUESS THE NUMBER GAME..... ')
print('if you want to quite game ---than write Quite')
while True:
    number1 = input('enter a number : ')
    if(number1 == 'Quite'):
        break
    number1 = int(number1)
    if(number == number1):
        print('\nCongratulation...YOU GUESS THE NUMBER')
        break
    elif(number > number1):
        print('Your number is to small ..guess the big number')
    else:
        print('your number is to big...guess the small number')

print('-----------GAME OVER----------')
    
