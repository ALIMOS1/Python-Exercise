class Animal():
    # base/main class
    def __init__(self):
        print('Animal Created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')
        
# derivate class, it inheritate some or all
# the feature from the base class

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
    def bark(self):
        print('WOOF!')

#print(help(Dog))
