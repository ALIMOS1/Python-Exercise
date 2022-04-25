def square(num):
    return num**2

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]

def check_even(num):
    return num%2 == 0



def main():
    
    my_nums = [1,2,3,4,5]
    for item in map(square,my_nums):
        print(item)
        
    # squared numbers in a list 
    squared_nums = list(map(square,my_nums))
    print(squared_nums)

    names = ['Andy','Eve','Sally']
    even_names = list(map(splicer,names))
    
    # the filter only reurns True values
    # from the function
    only_even_int = list(filter(check_even, my_nums))
    print(only_even_int)

    # the lambda function behavious
    # like any other function
    squared_nums2 =list(map(lambda num:num**2, my_nums))
    print(squared_nums2)

    only_even_int2=list(filter(lambda num:num%2 == 0, my_nums))
    print(only_even_int2)

main()
