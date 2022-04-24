
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x=x+1 # incrementing
    x+=1 # anothe way to increment
else:
    print('X is not less than 5')



# break, continue, pass

mystring = 'Sammy'

print('\nThis is a continue loop statment for a in Sammy \n')

for letter in mystring:
    if letter == 'a':
        # once it sees the letter a it goes to the top
        # of the closest enclosing loop 
        continue
    print(letter)
    
print('\nThis is a break loop statment\n')

for letter in mystring:
    if letter == 'a':
        # once it sees the letter a it breaks out
        # of the current closest enclosing loop 
        break
    print(letter)

    
    
