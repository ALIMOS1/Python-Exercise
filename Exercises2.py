# given a list of ints, return True if
# thr array contains a 3 next to a 3 on a list

def has_33(nums):
    for i in range(0, len(nums)-1):
        # if nums[i:i+2]== [3,3] # graps a slice at a time 
        if nums[i] == 3 and nums[i+1] ==3:
            return True
    return False 


def paper_doll(astring):
    triple_string =''
    for i in astring:
        triple_string += i*3
    return triple_string




         
def blackjack(a,b,c):
    int_list = [a,b,c]
    total_sum = sum(int_list)
    if total_sum <= 21:
        return total_sum
    
    elif total_sum <= 31 and 11 in int_list:
        return total_sum-10
    else:
        return 'Bust'


def summer_69(arr):
    total_number = 0
    for i in arr:
        if i>=6 and i<=9:
            pass
        else:
            total_number+=i
    return total_number

def count_primes(num):
    '''
    Count Primes:
    Returns the numbers that exist up to and including
    a given number
    '''
    # check for 0 or 1 
    if num<2:
        return 0

    # 2 or greater & store prime numbers 
    primes = [2]
    # counter going up to the input num 
    x = 3

    while x<=num:
        for y in range(3,x,2):
            if x%y == 0:
                x=x+2
                break
        else:
            primes.append(x)
            x=x+2

    print(primes)
            
        

    
    
       
        
        
