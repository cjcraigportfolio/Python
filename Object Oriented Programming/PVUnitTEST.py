# hw7TEST.py

>>> from hw7 import *

##### Volume #####

# set and get

>>> v = Volume()
>>> v.set(5.3)
>>> v
Volume(5.3)
>>> v.get()
5.3
>>> v.get()==5.3 # return not print
True
>>> 

# __init__, __repr__, up, down

>>> v = Volume(4.5) # set Volume with value
>>> v
Volume(4.5)
>>> v.up(1.4)
>>> v
Volume(5.9)
>>> v.up(6) # should max out at 11
>>> v
Volume(11)
>>> v.down(3.5)
>>> v
Volume(7.5)
>>> v.down(10) # minimum must be 0
>>> v
Volume(0)

# default arguments for __init__

>>> v = Volume() # Volume defaults to 0
>>> v
Volume(0)


# can compare Volumes using == 

>>> # comparisons
>>> v = Volume(5)
>>> v.up(1.1)
>>> v == Volume(6.1)
True
>>> Volume(3.1) == Volume(3.2)
False

# constructor cannot set the Volume greater
# than 11 or less than 0

>>> v = Volume(20)
>>> v
Volume(11)
>>> v = Volume(-1)
>>> v
Volume(0)
>>> 

##### partyVolume #####

>>> partyVolume('party1.txt')
Volume(4)
>>> partyVolume('party2.txt')
Volume(3.75)
>>> partyVolume('party3.txt')
Volume(0.75)

# make sure return not print

>>> partyVolume('party1.txt')==Volume(4) # return not print
True
>>> partyVolume('party2.txt')==Volume(3.75)
True
>>> partyVolume('party3.txt')==Volume(0.75)
True








