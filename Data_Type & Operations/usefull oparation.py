#Usefull operatin

for num in range(0,11,2): # Iteration in range function
    #print(num)
    pass



# Inumarate

index_count=0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count+=1



#replicate 
index_count=0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count+=1



# we can use the enumerate function to get the same results


word = 'abcde'
for item in enumerate(word): # we will get tuples and we can then unpack them 
    print(item)

print('\nUnpacking Tuples \n')

word = 'abcde'
for index, letter in enumerate(word): # we will get tuples and we can then unpack them 
    print(index)
    print(letter)
    print('\n')

print('\nZipping Lists To Tuples \n')
mylist1=[1,2,3]
mylist2=['a','b','c']
#puts list_items of same index in the same tuple
for item in zip(mylist1, mylist2):
    print(item)


print('Unpacking  Zipped Tuples')
mylist1=[1,2,3]
mylist2=['a','b','c']
#puts list_items of same index in the same tuple
for numbers,alph in zip(mylist1, mylist2):
    print('\n')
    print(numbers)
    print(alph)
    print('\n')





    
