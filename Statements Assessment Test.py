# Statements Assessment Test

#1 Use for, .split(), and if to create a Statement that will print out words that start with 's':

class S_words:
    # make a function
    def text(self, words):
        t_list = words.split()
        for word in t_list:
            if word[0]=='s':
                print(word)

# print even numbers 
class E_numbers:
    # print all even numbers
    def e_numbers(self):
        for i in range(0,11):
            if i%2==0:
                print(i,end=' ')
                
    
    
def main():
    print('Initial Test')
    print('')
    words = 'Print only the words that start with s in this sentence'
    s_words = S_words()
    s_words.text(words)
    print('Second Test')
    print('')
    even_numbers = E_numbers()
    even_numbers.e_numbers()
    


main()


