# float formatting

# formatting: '{values:width.precision f }'

r=result = 100/777

print('The result was {}'.format(result))

print('The result was {r:10.3f}'.format(r=result))
print('The result was {r:10.8f}'.format(r=result)) 


# F strings formatting
name = 'Jose'
print('Hello my name is {}'.format(name)) # This is the usuall way

print(f'Hello my name is {name} ')    # This is the new way Python3.6

name = 'Sam'
age = 3

print(f'His name is {name} and he\'s {age} years old.')


