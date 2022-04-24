# validating User Input
# the function below validates user input
def user_choice():

    choice = 'wrong'

    while choice.isdigit() == False:
        
        choice = input('Choose a number')
        print("Sorry, but you did not enter an integer. Please try again.")

        if choice.isdigit() == False:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_output()
            
            print("Sorry, but you did not enter an integer. Please try again.")

    return int(choice)


def display_game(game_list):
    print('Here is the current list: ',game_list)


def position_choice():
    choice = 'wrong'

    while choice not in ['0','1','2']:
        choice = input("Pick a position to replace (0,1,2): ")
        if choice not in ['0','1','2']:
            print("Sorry, but you did not enter an integer. Please try again.")

    return int(choice)

def replace_choice(game_list,position):

    user_placement= input('Type a string to place at the position: ')
    game_list[position] = user_placement

    return game_list

def game_choice():
    choice = 'wrong'

    while choice not in ['Y','N']:

        choice = input("Would you like to keep playing? Y or N ")

        if choice not in ['Y','N']:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")

    if choice =='Y':
        return True
    else:
        print('Game exit.....')
        return False


 
def main():

    game_on = True

# First Game List
    game_list = [0,1,2]

    while game_on:
        
        # Show the game list
        
        display_game(game_list)
        
        # Have player choose position
        position = position_choice()
        
        # Rewrite that position and update game_list
        game_list = replace_choice(game_list,position)
        
        # Clear Screen and show the updated game list
        
        display_game(game_list)
        
        # Ask if you want to keep playing
        game_on = game_choice()
    
    

main()
        
