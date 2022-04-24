# Statements Assessment Test
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

odd_n = [ num for num in range(1,50) if num%3==0]
print(odd_n)

# Go through the string below and if the length of a word is even print "even!"

def even_s(string):
    if int(len(string))%2==0:
        print('The string above is even')

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

def fizzBuzz():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
# Use List Comprehension to create a list of the first letters of every word in the string:

def f_letter(string):
    f_letter=[i[0] for i in string.split()]
    print(f_letter)


