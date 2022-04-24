# Interactions between Python Functions
from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess=''
    # checks if the input is correct 
    while guess not in ['0', '1','2']:
        guess = input('please select 0,1 or 2 ')
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Horray Correct')
        print(mylist)

    else:
        print('Incorect')
        print(mylist)
    
    

def main():
    mylist = ['','O','']
    shuffle_list(mylist)
    guess=player_guess()
    check_guess(mylist,guess)
    

main()
