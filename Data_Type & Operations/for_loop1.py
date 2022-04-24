### for loop practice
##import time 
##t = 0.5
mylist=[1,2,3,4,5,6,7,8,9,10]
##
##for i in mylist:
##    print(i)
##    print('File Deletion')
##    time.sleep(t)
##
##print('\nIT\'S A PRANK BRO \n')
##
##    


for num in mylist:
    #check for even int.
    # % are usefull to find even and odd numbers 
    if num % 2 == 0:
        pass


#sum all the numbers in a list 
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(list_sum)

# sum all the numbers with indices

list_sum2 = 0
for num in range(len(mylist)):
    list_sum2 = mylist[num] + list_sum
print(list_sum)

# we can also iterate trough a string
empty_string = ''
for i in 'Hello World':

    empty_string = empty_string + i

print(empty_string)


# tuple unpacking

mylist = [(1,2),(3,4),(5,6),(7,8)]
for a,b in mylist:
    print(a,b)

    
    

        
