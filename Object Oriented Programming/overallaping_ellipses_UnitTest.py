from overlapping_ellipses import intro,ellipse, ellipseAccept, step_range, test_values, values, monte_carlo, box_method
'''
Christian Craig
'''
def main():
    print(intro.__doc__)
    
    '''
Unit test for class ellipse
    '''
    print('\nClass name = "ellipse"')
    print(ellipse.__doc__)
    print('E=ellipse()')
    print('E')
    E=ellipse()
    print('{}.The expected amount for each value is 0.'.format(E)) #repr test

    print('Function name = "area"')
    print(ellipse.area.__doc__)
    print('E.area()')
    print('The blank constructor area = {}. The expected value is 0.'.format(E.area())) #area function with blank constructor
    
    print('\nFunction name = "circ"')
    print(ellipse.circ.__doc__)
    print('E.circ()')
    print('The blank constructor circumference = {}.The expected value is 0.'.format(E.circ())) #area function with blank constructor


    '''
Unit test for class ellipseAccept
    '''
    print('\nClass name = "ellipseAccept"')
    print(ellipseAccept.__doc__)
    print('e=ellipseAccept(1,4,3,2)')
    e=ellipseAccept(1,4,3,2)
    print('e')
    print(e)
    print('Test Get functions')
    print('e.geta() == 1  Result = {}'.format(e.geta() == 1))
    print('e.getb() == 4  Result = {}'.format(e.getb() == 4))
    print('e.geth() == 3  Result = {}'.format(e.geth() == 3))
    print('e.geth() == 2  Result = {}'.format(e.getk() == 2))
    
    print('Test Set functions')
    e.seta(3)
    print('e.seta(3)')
    e.setb(1)
    print('e.setb(1)')
    e.seth(2)
    print('e.seth(2)')
    e.setk(2)
    print('e.setk(2)')
    print('Re-Test Get Function')
    print('e.geta() == 3  Result = {}'.format(e.geta() == 3))
    print('e.getb() == 1  Result = {}'.format(e.getb() == 1))
    print('e.geth() == 2  Result = {}'.format(e.geth() == 2))
    print('e.getk() == 2  Result = {}'.format(e.getk() == 2))
    
    print('\nTest area and circ function. Explanations of functions near top of page.')
    print('function name = "area"')
    print('e.area()')
    print('The ellipse area = {}  The expected value is 9.425'.format(e.area()))
    print('function name = "circ"')
    print('e.circ()')
    print('The ellipse circumference = {}  The expected value is 13.364'.format(e.circ()))
    print('link to calculator for comparison:\nhttps://keisan.casio.com/exec/system/1223289167')

    '''      
Unit Test for step_range function
    '''
    print('\nfunction name = "step_range"')
    print(step_range.__doc__)
    print('step_range(start,stop,step)')
    print('testing .1 step in range 1 through 2 (less than 2)')
    print('step_range(1,2,.1)')
    print(list(step_range(1,2,.1)))
    
    '''
Unit Test for monte_carlo estimation.
    '''
    print('\nfunction name = "monte_carlo"')
    print(monte_carlo.__doc__)
    print('testing function of monte carlo estimate.')
    print('monte_carlo(e1,e2)')
    e1=ellipseAccept(1,3,4,5)
    e2=ellipseAccept(3,2,1,3)
    print('e1=ellipseAccept(1,3,4,5)')
    print('e2=ellipseAccept(3,2,1,3)')
    print(monte_carlo(e1,e2))
    
    '''
Unit Test for box_method
    '''
    print('\nfunction name = "box_method"')
    print(box_method.__doc__)
    print('testing function of box method estimate')
    print('box_method(e1,e2)')
    e1=ellipseAccept(1,3,4,5)
    e2=ellipseAccept(3,2,1,3)
    print('e1=ellipseAccept(1,3,4,5)')
    print('e2=ellipseAccept(3,2,1,3)')
    print(box_method(e1,e2))
    '''
Unit Test for test_values function
    '''
    print('\nfunction name = "test_values"')
    print(test_values.__doc__)
    print('\nFirst we will test the functionality of the test_values function.')
    print('\nAfter that,we will test the monte_carlo and box_method functions for the following cases:')
    print('1. Ellipses with the exact coordinates')
    print('2. No overlap')
    print('3. Overlap')
    print('test_values(a1,b1,h1,k1,a2,b2,h2,k2)')
    print('test_values(1,3,4,5,3,2,1,3)')
    print('e1=ellipseAccept(a1,b1,h1,k1)')
    print('e2=ellipseAccept(a2,b2,h1,k2)')
    print('\nSummary Results:')
    test_values(1,3,4,5,3,2,1,3)
    e1=ellipseAccept(1,3,4,5)
    e2=ellipseAccept(3,2,1,3)
    print('\nTest comparison of results above:')
    print('\nellipse one: area = {} circumference = {}  Expected values = 9.425 and 13.364'.format(e1.area(),e1.circ()))
    print('ellipse two: area = {} circumference = {}  Expected values = 18.85 and 15.865'.format(e2.area(),e2.circ()))
    print('\nReference link in previous section to get Expected values.')

    '''
Unit Test for monte_carlo and box_method
functions in the test_values function
    '''
    print('\nTest for monte_carlo and box_method functions in test_values functions:')

    print('\n1.Ellipses with the same exact coordinates:')
    print('test_values(3,3,3,3,3,3,3,3)')
    print('e1=ellipseAccept(3,3,3,3)')
    print('e2=ellipseAccept(3,3,3,3)')
    test_values(3,3,3,3,3,3,3,3)
    print('\nNOTICE ABOVE - that the area overlap estimations are close to the actual area of ellipse 1 and 2.')

    print('\n2.Checking if estimates return 0 if no overlap:')
    print('test_values(1,2,2,2,1,1,4,5)')
    print('e1=ellipseAccept(1,2,2,2)')
    print('e2=ellipseAccept(1,1,4,5)')
    test_values(1,2,2,2,1,1,4,5)
    
    print('\n3.Checking overlap against a mathematical formula from online:')
    print('test_values(3,2,0,0,3,3,0,1)')
    print('e1=ellipseAccept(3,2,0,0)')
    print('e2=ellipseAccept(3,3,0,1)')
    test_values(3,2,0,0,3,3,0,1)
    
    print('Mathematical overlap output from source = 17.602')
    print('\nlink to mathmatical output: https://link.springer.com/content/pdf/10.1007/s00791-013-0214-3.pdf')
    print('In the link, reference pg 300, case 5')
    print('Source: "Calculating ellipse overlap areas" by Hughes and Chraibi')

    '''
Unit Test for values function
    '''
    
    print('\nfunction name="values"')
    print(values.__doc__)
    values()
    
    
if __name__=='__main__':
    main()
