
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'OrderPizzaUnitTest.py'))

class Pizza:
    def setSize(self,size):
        self.s = size
    def __init__(self,size='M',toppings=[]):
        self.s=size
        self.t= set(toppings)
    def __repr__(self):
        return f"Pizza('{self.s}',{self.t})"# not printing the string version of se
    def getSize(self):
        return self.s
    def addTopping(self,top):
        self.t.add(str(top))
    def removeTopping(self,top):#remove first in line
        self.t.remove(str(top))
    def price(self):
        if self.s=='S':
            return 6.25+(.70*(len(self.t)))
        elif self.s=='M':
            return 9.95+(1.45*(len(self.t)))
        else: # self.s=='L':
            return 12.95+(1.85*(len(self.t)))           
        return priceTotal
    def __eq__(self,other):
        return self.s ==other.s and self.t==other.t
        
def orderPizza():
    pie=Pizza()
    print('Welcome to Python Pizza!')
    size=input('What size pizza would you like(S,M,L): ')
    pie.setSize(size)
    while True:
        toppings= input('What topping to add (or Enter to quit): ')
        if toppings:
            pie.addTopping(str(toppings))
        else:
            print('Thanks for ordering!')
            print('Your Pizza costs',pie.price())
            return pie


            
    
 

