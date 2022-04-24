# comprehensions

mystring= 'hello'

mylist = []
for letter in mystring:
    mylist.append(letter)

#print(mylist)

# now we will use the comprehension approach

mylist = [letter for letter in mystring]

print(mylist)

# or 
mylist = [letter*2 for letter in mystring]

#print(mylist)
# we are just getting ride of append functionality

mylist = [num*2 for num in range(0,11) if num%2==0]

print(mylist)

celcius = [0,10,20,34,5]

print('\nCelcius to farenheit')

farenheit = [((9/5)*temp+32) for temp in celcius]

print(farenheit)
