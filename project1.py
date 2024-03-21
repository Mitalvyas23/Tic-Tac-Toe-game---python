import random
import string

letters = string.ascii_letters
digits = string.digits
character = string.punctuation

passwordstring = letters + digits + character

print('1 : 8 length password')
print('2 : 12 length password')
print('3 : Quite')
choice = int(input('enter your choice : '))
password = ''

match choice:
    case 1:
        for i in range(0,8):
            number = random.choice(passwordstring)
            password+=number
        print('THE PASSWORD IS : ',password)

    case 2:
        for i in range(0,12):
            number = random.choice(passwordstring)
            password+=number
        print('THE PASSWORD IS : ',password)

    case 3:
        print('Quite')

        