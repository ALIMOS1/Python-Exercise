# Nested Statment and scope
# LEGB Rule
# local,Enclosing, Global, Build-in 


name = 'I am global'

def greet():
    name= 'I am enclosing'
    def hello():
        # If no local name
        # it will check enclosing name
        # if we get ride of the enclosing
        # it will go higher up and look for global
        name = 'I am local'
        print('Hello '+name)
    hello()


def main():

    greet()

main()
