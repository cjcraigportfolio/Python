'''
1.	Develop a class Volume that stores the volume for a stereo that has a value between 0 and 11.  Usage of the class is listed below the problem descriptions.  Throughout the class you must guarantee that:

•	The numeric value of the Volume is set to a number between 0 and 11.  Any attempt to set the value to greater than 11 will set it to 11 instead, any attempt to set a negative value will instead set it to 0. 
•	This applies to the following methods below: __init__, set, up, down
You must write the following methods:
•	__init__ - constructor.   Construct a Volume that is set to a given numeric value, or, if no number given, defaults the value to 0.   (Subject to 0 <= vol <=11 constraint above.)
•	__repr__ - converts Volume to a str for display,  see runs below.
•	set – sets the volume to the specified argument (Subject to 0 <= vol <=11 constraint above.)
•	get – returns the numeric value of the Volume 
•	up – given a numeric amount, increases the Volume by that amount. (Subject to 0 <= vol <=11 constraint above.)
•	down – given a numeric amount, decreases the Volume by that amount. (Subject to 0 <= vol <=11 constraint above.)
•	__eq__  - implements the operator ==.   Returns True if the two Volumes have the same value and False otherwise.






2.	Write a standalone function partyVolume() that takes accepts one argument, a string containing the name of a file.  The objective of the function is to determine the a Volume object that is the result of many people at a party turning the Volume up and down.  More specifically: the first line of the file is a number that indicates the initial value of a Volume object.  The remaining lines consist of a single character followed by a space followed by a number.  The character will be one of ‘U” or ‘D’ which stand for “up” and “down” respectively.  The function will create a new Volume object and then process each line of the file by calling the appropriate method of the Volume object which changes the value of the Volume.  The function then returns the final Volume object.   Guidelines/hints:

•	This is a standalone function, it should NOT be inside (indented within) the class. It should be listed in the module after the Volume class and without indentation.

•	Note that the first line of the file will be treated differently than all the other lines.  Probably the easiest way to do this is to 1) open the file, 2) call the .readline() method (no s!) which reads a single line, the initial value of the Volume, then 3) call the .readlines() method which reads the rest of the lines.  Item 2) will be used to set the initial Volume and 3) will be iterated over to represent turning the volume up and down some number of time.

•	Make sure you return the final Volume object.
'''

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'PVUnitTEST.py'))

class Volume:
    def set(self,cntrlVol):#1
        v=Volume()
        limVol=max(min(cntrlVol,11),0)
        self.v=limVol
    def get(self):
        return(self.v)
    def __repr__(self):
        #return('hah!')
        return"Volume({})".format(self.v)
    def __init__(self,cntrlVol=0): #2
        #initialize object
        #print('init')
        limVol=max(min(cntrlVol,11),0)
        self.v=limVol
    def __eq__(self,other): #return
        #if self.x == other.x and self.y==other.y: #equality of numbers
            #if "is" is true then == is true, but not vice versa 
            #return True
        #else:
            #return False
        return self.get() == other.get()
    def up(self,changeVol):#3
        cntrlVol=self.v+changeVol
        limVol=max(min(cntrlVol,11),0)
        self.v=limVol
    def down(self,changeVol):#4
        cntrlVol=self.v-changeVol
        limVol=max(min(cntrlVol,11),0)
        self.v=limVol
        
def partyVolume(filename):
    infile=open(filename)
    c=Volume()
    firstVol=eval(infile.readline())
    c.set(firstVol)
    lineList=infile.readlines()
    for a in range(len(lineList)):
        lineList[a]=lineList[a].split()
    for b in range(len(lineList)):
        if lineList[b][0]=='U':
            up=lineList[b][1]
            c.up(eval(up))
        else:
            down=lineList[b][1]
            c.down(eval(down))
    return c
    
