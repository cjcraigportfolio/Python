'''
Christian Craig
Assignment3
DSC430
“I have not given or received any unauthorized assistance on this assignment.”
'''
class ellipse:
    '''
This is the parent class of the ellipse that
contains a blank constructor. You can set
and get (which define and return variables).
Set will be used in the child class below.
The class can calculate the area as well as the
circumference. Call "E" to see the value amount (repr).
    '''
    def __init__(self): #blank constructor
        self.a=0
        self.b=0
        self.h=0
        self.k=0
        self.pi=3.14159265359
        
    def seta(self,ina):
        self.a=ina

    def setb(self,inb):
        self.b=inb

    def seth(self,inh):
        self.h=inh

    def setk(self,ink):
        self.k=ink

    def geta(self):
        return self.a

    def getb(self):
        return self.b

    def geth(self):
        return self.h

    def getk(self):
        return self.k
    
    def __repr__(self):
        return "Values(a={},b={},h={},k={})".format(self.a,self.b,self.h,self.k)

    def area(self): 
        '''
The purpose of the area function
is to calculate the area of a single ellipse
        '''
        a=self.pi*self.a*self.b #area formula for a single ellipse
        return round(a,3)
        
    def circ(self):
        '''
The purpose of the circ function
is to calculate the circumference of a single ellipse
        '''
        c=self.pi * ( 3*(self.a+self.b) - ( (3*self.a + self.b) * (self.a + 3*self.b) )**(1/2) ) #circumference formula for a single ellipse
        return round(c,3)



class ellipseAccept(ellipse):
    '''
The ellipseAccept class accepts all of the
appropriate variables from the parent class.
You can initiate the class then, call the functions
that are in the parent class.
    '''
    def __init__(self,a,b,h,k,pi=3.14159265359): #contructor that accepts varibales
        self.a=a
        self.b=b
        self.h=h
        self.k=k
        self.pi=pi

    
def step_range(start,stop,step):
    '''
The step_range function is used to calculate the
steps in the ranges for the box_method function.
Start = first point, Stop = end point,
Step = amount used to get to Stop.
    '''
    r=start
    while r<=stop:
        yield round(r,3)
        r+=step
    return r

def test_values(a1,b1,h1,k1,a2,b2,h2,k2):
    '''
The test_values function tests predetermined variables
that calculate the area as well as the circumference for
ellipse 1 (e1) and ellipse 2 (e2). The function will also
produce the results from the monte_carlo and box_method functions.

    '''
    e1=ellipseAccept(a1,b1,h1,k1)
    e2=ellipseAccept(a2,b2,h1,k2)
    print("ellipse one: area={} circumference={}".format(e1.area(),e1.circ()))
    print("ellipse two: area={} circumference={}".format(e2.area(),e2.circ()))
    print(monte_carlo(e1,e2))
    print(box_method(e1,e2))

def values():
    '''
The values function takes user input for ellipse 1 and ellipse 2.
All inputs must be integers. Furthermore, a and b for both ellipses must be
positive integers within 1 and 10. The area and circumference are calculated
for ellipse 1 (e1) and ellipse 2 (e2).The function will also produce the results
from the monte_carlo and box_method functions.
    '''

    while True:
        try: #h1,k1 and h2,k2 can only be positve integers 1-10
            a1=int(input('Please input a1 (integer 1 through 10): '))
            assert a1>=1 and a1<=10
            b1=int(input('Please input b1 (integer 1 through 10): '))
            assert b1>=1 and b1<=10
            h1=int(input('Please input h1: '))
            k1=int(input('Please input k1: '))
            
            a2=int(input('Please input a2 (integer 1 through 10): '))
            assert a2>=1 and a2<=10
            b2=int(input('Please input b2 (integer 1 through 10): '))
            assert b2>=1 and b2<=10
            h2=int(input('Please input h2: '))
            k2=int(input('Please input k2: '))
            break
        except ValueError: #raises error if a1,b1 h1,k1 and a2,b2 h2,k2 not integers 
            print('Please type an integer.')
        except AssertionError: #raises error if a1,b1 and a2,a2 not positive
            print('Please make sure value is between 1 and 10.')
      
    e1=ellipseAccept(a1,b1,h1,k1)
    e2=ellipseAccept(a2,b2,h2,k2)
    print("ellipse one: area={} circumference={}".format(e1.area(),e1.circ()))
    print("ellipse two: area={} circumference={}".format(e2.area(),e2.circ()))
    print(monte_carlo(e1,e2))
    print(box_method(e1,e2))
    end=input('Do you wish to leave(Y/N)? ')
    try:
        assert end=='Y' or end=='N' 
        if end=='Y':
            quit()
        elif end=='N':
            values()
    except AssertionError: #Must answer Y or N
        print('Please enter Y or N')
#print function in values
          
def monte_carlo(e1,e2):
    '''
The monte_carlo function runs a simulation
for the area of the overlap of the two ellipses.
Inputs are taken from the values function, then
randomly generated points (x and y) are created.
The function checks if the point is in the bound of the
overlap or outside. The area is then created
by the points in the overlap bound over the points
outside of the bound.

Accuracy will be checked in the test_values function. 
    '''
    import random
    count = 0.0
    in_area = 0.0
    '''
    Get points from values function
    '''
    a1=e1.geta()
    b1=e1.getb()
    h1=e1.geth()
    k1=e1.getk()

    a2=e2.geta()
    b2=e2.getb()
    h2=e2.geth()
    k2=e2.getk()

    random.seed(1) #to get same random variables for testing
  
    while count<1000:
        '''
Note that in our randomly generated
points we are only using points from ellipse 1.
That is because we are creating a box around ellipse 1
which will be our bound. All points will be within the bound
but we need to see which are in the ellipse
        '''
        x=random.uniform(h1-a1, h1+a1)  #get position, choosing one ellipse
        y=random.uniform(k1-b1, k1+b1)  
      

        if ((x-h1)**2/a1**2)+((y-k1)**2/b1**2)<= 1 and ((x-h2)**2/a2**2)+((y-k2)**2/b2**2)<=1: #check if in the bound of the overlap
            in_area+=1 #amount the overlap
        
        count+=1 #total points generated
    area_box= ((2*a1)*(2*b1)) #choosing ellipse one to create bound, can be either
    monte_carlo_estimate=round((in_area/count)*area_box,3) #total points generated over amount in area * the area of the bound
    
    
    return "monte carlo estimated overlap = {}".format (monte_carlo_estimate)
     
def box_method(e1,e2):
    '''
The box_method function estimates the area
of the overlap by calculating the area of
rectangles generated in the overlap. Like the
monte_carlo function, inputs are received from the
values functions. You use the step_range function to determine
the bounds as well as the step amount for the x an y.
Building the rectangles - You then create a dictionary
to get all of your y values, then subtract the max and min
of those y values for every x value, this gives you the
height. Then put those heights into a list, then
multiply them by your step.

Accuracy will be checked in the test_values function. 
    '''
    lst=[]
    xy_dict={}
    '''
    Get points from
    values function
    '''
    a1=e1.geta()
    b1=e1.getb()
    h1=e1.geth()
    k1=e1.getk()

    a2=e2.geta()
    b2=e2.getb()
    h2=e2.geth()
    k2=e2.getk()

   
    '''
As in the monte_carlo function, you are creating bound
using one ellipse. 
    '''
    area=0
    for x in step_range(h1-a1,h1+a1,.05): #choosing 1 box
        
        for y in step_range(k1-b1,k1+b1,.05):

            if((x-h1)**2/a1**2)+((y-k1)**2/b1**2)<=1 and ((x-h2)**2/a2**2)+((y-k2)**2/b2**2)<=1: #check if in the bound of the overlap
                lst.append ((x,y))
    for x,y in lst: 
        '''
Create dictionary to get list of y's for
every x value. 
        '''
        xy_dict.setdefault(x,[]).append(y)
        height_lst=[]
        for x,y in xy_dict.items():
            height=abs(max(y)-min(y)) #for y's of each x
            height_lst.append(height*.05) #multiply each height by step
        area=round(sum(height_lst),3) 
    return "box method estimated overlap = {}".format(float(area))


def intro(): #introduction statement
    '''
Welcome to the ellipse calculator 3000!
First you will be shown the ellipse class (parent) and the ellipseAccept class (child).
They show how a single ellipse is calculated by using the key variables (a,b,h,k).
"a" determines the width of the ellipse, while "b" determines the height.
"h" is the x value of the origin, while "k" is the y.
Two estimations will be presented and tested for accuracy in the test_values function.
The estimation methods we will be using are monte_carlo and the box method.
Explanations will be given for each function. Enjoy!
    '''

