class Employee:
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = (first+'.'+last+'@email.com').lower()
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first,self.last)


    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)


class Developer(Employee):
    
    raise_amt = 1.10
    def __init__(self,first,last,pay,prog_lang):
        # Employee class will handle what's below
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang
        
        
    


dev_1 = Developer('Alim','Ali',50000,'Python')
dev_2 = Developer('Test','Employee',40000,'Javascrip')





def main():
    print(dev_1.email)
    print(dev_1.fullname())
    print(dev_1.prog_lang)
    print('')
    print('Is Developer a subclass of Employee ?')
    print(issubclass(Developer,Employee))
    print(isinstance(dev_1,Employee))

main()
