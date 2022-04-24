# *args is a parameter that takes any number of
# argumnts in a tuple
# instead of specified arguments in a function

def myfunc(*args):
    print(args)


# **kwargs is treated like a keyword argument or dict
# ex: fruit = 'apple', sport = 'soccer' etc..

def myDictionaryFunction(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    print(kwargs)
