'''TIC - TAC - TOE GAME using python
    simple python program
    PROGRAMMER = Mital vyas'''

def printboard():
    print('  ',value[0],'  | ',value[1],' | ',value[2],'  ')
    print('-------|-----|-------')
    print('  ',value[3],'  | ',value[4],' | ',value[5],'  ')
    print('-------|-----|-------')
    print('  ',value[6],'  | ',value[7],' | ',value[8],'  ')

win1 = ''   
def checkwin():
    if((value[0] == value[1]) and (value[1] == value[2])):
        return 1
    elif((value[3] == value[4]) and (value[4] == value[5])):
        return 1
    elif((value[6] == value[7]) and (value[7] == value[8])):
        return 1
    elif((value[0] == value[3]) and (value[3] == value[6])):
        return 1
    elif((value[1] == value[4]) and (value[4] == value[7])):
        return 1
    elif((value[2] == value[5]) and (value[5] == value[8])):
        return 1
    elif((value[0] == value[4]) and (value[4] == value[8])):
        return 1
    elif((value[2] == value[4]) and (value[4] == value[6])):
        return 1
    else:
        count = 0
        for i in range(0,9):
            if(value[i] == 'x' or value[i] == 'X' or value[i] == 'o' or value[i] == 'O'):
                count = count + 1
        if(count == 9):
            return 2
    return -1

print('WELCOME TO TIC TAC TOE GAME : ')
print('1 : PLAY')
print('2 : EXIT')
choice = int(input('enter your choice : '))


match choice:
    case 1:
        player = 1
        print('X OR O : \nCHOOSE ONT OPTION : \n[please enter cahracter]')
        player1 = input('PLAYER 1 : enter your choice : ')
        player2 = input('PLAYER 2 : enter your choice : ')
        #if(player1 != 'x' or player1 != 'X' or player1 != 'o' or player1 != 'O' or player2 != 'x' or player2 != 'X' or player2 != 'o' or player2 != 'O'):
        #    print('INVALID INPUT')

        win = -1
        value = [1,2,3,4,5,6,7,8,9]
        print('  ',value[0],'  | ',value[1],' | ',value[2],'  ')
        print('-------|-----|-------')
        print('  ',value[3],'  | ',value[4],' | ',value[5],'  ')
        print('-------|-----|-------')
        print('  ',value[6],'  | ',value[7],' | ',value[8],'  ')
        while(win == -1):
            if(player % 2 == 0):
                print("\nPLAYER 2 : WHICH PLACE YOU WANT TO TIC :  ")
                tic = int(input())
                if(tic < 1 and tic > 9):
                    print('INVALID INPUT')
                value[tic-1] = player2
                printboard()
                result = checkwin()   
            else:
                print("\nPLAYER 1 : WHICH PLACE YOU WANT TO TIC :  ")
                tic = int(input())
                if(tic < 1 and tic > 9):
                    print('INVALID INPUT')
                value[tic-1] = player1
                printboard()
                result = checkwin()
            if(result == 1):
                print('\nCongratulations......you are WINNER------------\n')
                break
            elif(result == 2):
                print('\n-------------------DRAW---------------------\n')
                break
            player+=1   
    case 2:
        print('INVALID INPUT')
