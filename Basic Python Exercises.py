'''
A Summary of Exercises Completed in Fall 2019 Quarter
to Pepare for hand written final exam
'''
'''
Implement the function vowels() that takes as input a string
and prints the indexes of all vowels in the string.
Hint: A vowel can be defined as any character in string 'aeiouAEIO
'''
def vowels(phrase):
    vowels='aeiouAEIOU'
    for char in phrase:
        if char in vowels:
            print(phrase.index(char))
'''
Implement function indexes() that takes as input a word (as a string)
and a one- character letter (as a string) and returns a list
of indexes at which the letter occurs in the word.
'''
def indexes (statement,char):
    indices=[]
    for i in range(len(statement)): 
        if char in statement[i]:
            indices.append(i)
    return indices
'''
Implement function that prints different results based on temp.
'''
def temperature(t):
    if t>86:
        print('It is hot')
    elif t > 32:
        print('It is cool')
    else: #t<=32
        print ('It is freezing')
    print('Goodbye')
'''
Implement function that prints different results based on body mass index.
'''
def BMI(weight,height):
    bmi=(weight*703)/height**2
    if bmi>=25.0:
        print('Overweight')
    elif bmi>=18.5:
        print('Normal')
    else:
        print('Underweight')
'''
Implement function that accepts a lst and checks if it's sorted.
'''
def checksorted(lst):
    for i in range(0,len(lst)-1):
        if lst[i]>lst[i+1]:
            return False
    else:
        return True
'''
Write function arithmetic() that takes a list of integers as input
and returns True if they form an arithmetic sequence.
(A sequence of integers is an arithmetic sequence if
the dif- ference between consecutive items of the list is always the same.)
'''
def arithmetic (lst):
    if len(lst)<2:
        return True
    seq=lst[1]-lst[0]
    for i in range(0,len(lst)-1):
        if lst[i+1]-lst[i]!=seq:
            return False
    else:
        return True
'''
Implement function factorial() that takes as input a nonnegative integer
and returns its factorial.The factorial of a nonnegative integer n, denoted
n!, is defined in this way
'''
def factorial(num):
    res=1
    for i in range(2,num+1):
        res*=i
    return res
'''
An acronym is a word formed by taking the first letters of the words in a
phrase and then making a word from them. For example, RAM is an acronym
for random access memory. Write a function acronym() that takes a phrase
(i.e., a string) as input and then returns the acronym for that phrase.
Note: The acronym should be all uppercase, even if the words in the
phrase are not capitalized.
'''
def acronym(phrase):
    words=phrase.split()
    #print(words)
    res=''
    for w in words:
        res+=w[0].upper()
    return res
'''
Implement function four_letter() that takes as input a list of words
(i.e., strings) and returns the sublist of all four letter words in the
'''
def four_letter(lst):
    indices=[]
    for word in range(0,len(lst)):
        if len(lst[word])==4:
            indices.append(lst[word])
    return indices
'''
Write function divisors() that takes a positive integer n as input and
returns the list of all positive divisors of n.
'''
def divisors(num):
    div=[]
    for x in range(1,num+1):
        if num%x==0:
            div.append(x)
    return div
'''
Rock, Paper, Scissors is a two-player game in which
each player chooses one of three items. If both players
choose the same item, the game is tied. Otherwise, the
rules that determine the winner are:

(a) Rock always beats Scissors (Rock crushes Scissors)
(b) Scissors always beats Paper (Scissors cut Paper)
(c) Paper always beats Rock (Paper covers Rock)

Implement function rps() that takes the choice
('R', 'P', or 'S') of player 1 and the choice of
player 2, and returns −1 if player 1 wins, 1 if
player 2 wins, or 0 if there is a tie.
'''
def rps(p1,p2):
    p1win=['RS','SP','PR']
    if p1+p2 in p1win:
        return -1
    elif p1==p2:
        return 0
    else:
        return 1
'''
Write function exclamation() that takes as input a string and returns
it with this modification: Every vowel is replaced by four consecutive
copies of itself and an exclama- tion mark (!) is added at the end.
'''
def exclamation(word):
    vow=''
    for v in word:
        if v in 'aeiou':
            vow+=v*4
        else:
            vow+=v
    return vow
'''
Implement function leap() that takes one input argument—a year—and
returns True if the year is a leap year and False otherwise.
(A year is a leap year if it is divisible by 4 but not by 100,
unless it is divisible by 400 in which case it is a leap year.
For example, 1700, 1800 and 1900 are not leap years but 1600 and 2000 are.)
'''
def leap(year):
    if year%4==0 and year%100!=0:
        return True
    if year%400==0:
        return True
    else:
        return False
'''
Write function geometric() that takes a list of integers as input and
returns True if the integers in the list form a geometric sequence.
A sequence a0, a1, a2, a3, a4, . . . , an −2, an − 1 is a geometric
sequence if the ratios a1/a0, a2/a1, a3/a2, a4/a3, . . . , an−1/an−2
are all equal.
'''
def geometric(lst):
    div=lst[1]/lst[0]
    for i in range(1,len(lst)-1):
        if lst[i+1]/lst[i]!=div:
            return False
    else:
        return True
'''
Write a function statement() that takes as
input a list of floating-point numbers, with positive numbers representing
deposits to and negative numbers representing withdrawals from a bank account.
Your function should return a list of two floating-point numbers; the first
will be the sum of the deposits, and the second (a negative number) will be
the sum of the withdrawals.
'''
def statement(lst):
    posTotal=0
    negTotal=0
    for n in lst:
        if n>0:
            posTotal+=n
        else:
            negTotal+=n
    return [posTotal,negTotal]
'''
Implement function pixels() that takes as input a two-dimensional
list of nonnega- tive integer entries (representing the values of pixels of
an image) and returns the number of entries that are positive (i.e.,
the number of pixels that are not dark). Your function should work on
two-dimensional lists of any size.
'''
def pixels (lst):
    pix=0
    for n in lst:
        for z in range(len(lst)+1):
            if n[z]!=0:
                pix+=1
    return pix
'''
Implement function prime() that takes a positive integer as input and returns
True if it is a prime number and False otherwise.
'''
def prime(num):
    for potentialDivisor in range(2,num+1):
        if num%potentialDivisor==0 and num!=potentialDivisor:
            return False
    else:
        return True
'''
Implement function primeFac() that takes as input a positive integer n and
returns a list containing all the numbers in the prime factorization of n.
(The prime factorization of a positive integer n is the unique list of prime
numbers whose product is n.)
'''
def primeFac(num):
    facs=[]
    n=90
    potFac=2
    while num>1:
        if num%potFac==0:
            num/=potFac
            facs.append(potFac)
        else:
            potFac+=1
    return facs
'''
Implement function evenrow() that takes a two-dimensional list of integers and
re-turns True if each row of the table sums up to an even number and False
otherwise (i.e., if some row sums up to an odd number).
'''
def evenrow(lst):
    for n in range(len(lst)):
        for j in range(len(lst)):
            if (sum(lst[n]+lst[j]))%2!=0:
                return False
    else:
        return True
'''
'''
def inversion(ltrs):
    count=0
    for i in range(len(ltrs)):
        for j in range(len(ltrs)):
            if ltrs[i]>ltrs[j]:
                count+=1
        else:
            count+=0
    return count
'''
'''
def countdown(n):
    if n<=0:
        print('Blastoff!!!')
    else: #recursive
        print(n)
        countdown(n-1)
'''
Write function collatz() that takes a positive integer x as input and
prints the Collatz sequence starting at x. A Collatz sequence is obtained
by repeatedly applying this rule to the previous number x in the sequence:

x=x/2 if even
x=3x+1 if odd

Your function should stop when the sequence gets to number 1.
Note: It is an open question whether the Collatz sequence of every
positive integer always ends at 1.

'''
def collatz(x):
        ans=0
        while x!=1:
            print(x)
            if x%2==0:
                x=x/2
                print(x)
            else:
                x=(3*x)+1
                print(x)
'''
Let list1 and list2 be two lists of integers. We say that list1 is a
sublist of list2 if the elements in list1 appear in list2 in the same
order as they appear in list1, but not necessarily consecutively.
For example, if list1 is defined as:

[15, 1, 100]

and list2 defined as:

[20, 15, 30, 50, 1, 100]

then list1 is a sublist of list2 because the numbers in list1 (15, 1, and 100) appear in
list2 in the same order. However, list

[15, 50, 100]

Implement function sublist() that takes as input lists list1 and list2 and
returns True if list1 is a sublist of list2, and False otherwise

'''
def sublist(lst1,lst2):
    i=0
    j=0
    while i in range(len(lst1)) and j in range(len(lst2)):#both varibles in lsts
        if lst1[i]!=lst2[j]:
            j+=1#add to j to make the match
        elif lst1[i]==lst2[j]:
            i+=1
            j+=1
            #if i in range(len(lst2)):
    if i not in range(len(lst1)):
        return True
    else:
        return False

'''
The mirror image of string vow is string wov, and the mirror image wood is
string boow. The mirror image of string bed cannot be represented as a string,
however, because the mirror image of e is not a valid character.

Develop function mirror() that takes a string and returns its mirror
image but only if the mirror image can be represented using letters in the
alphabet.
'''
def mirror(word):
    letters = {'b':'d','d':'b','i':'i','l':'l','o':'o','v':'v','w':'w','x':'x'}
    s=''
    for i in word:
        if i not in letters:
            return 'INVALID'
        else:
            s+=letters[i]
    return s[::-1]
'''
Implement function that returns dice if equal the same
'''
def diceTotal(): # no parameters

    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    pips = die1 + die2
    #print( die1, die2 )
    while die1==die2:
        die1 = random.randrange(1,7)
        die2 = random.randrange(1,7)
        #print( die1, die2 )
        pips += die1 + die2
    return pips



'''
Implement function wordcount() that takes as input a text—as a string—
and prints the frequency of each word in the text. You may assume that
the text has no punctuation and words are separated by blank spaces.
'''
def wordCount(text):
    textSplit=text.split()
    counters={}
    for word in textSplit:
        if word in counters:
            counters[word]+=1
        else:
            counters[word]=1
    for word in counters:
        if counters[word]>1:
            print(word,'   ','appears',counters[word],'times.')
        else:
            print(word,'    ','appears',counters[word],'time.')

'''
Implement function lookup() that implements a phone book lookup application.
Your function takes, as input, a dictionary representing a phone book.
In the dictionary, tuples containing first and last names of individual (the keys) are mapped to strings containing phone numbers (the values). Here is an example:

>>> phonebook = {('Anna','Karenina'):'(123)456-78-90', ('Yu', 'Tsun'):'(901)234-56-78',
('Hans', 'Castorp'):'(321)908-76-54'}

Your function should provide a simple user interface through which a user can enter the first
and last name of an individual and obtain the phone number assigned to that individua
'''
def lookup(phonebook):
    while True:
        first=input('Enter the first name:')
        last=input('Enter the last name:')
        person=(first,last)#construct the key
        if person in phonebook:
            print(phonebook[person])
        else:
            print('The name you entered is not known')
'''
Implement function names() that takes no input and repeatedly asks the
user to enter the first name of a student in a class. When the user
enters the empty string, the function should print for every name the
number of students with that name.
'''
def names():
    counter={}
    lst=[]
    while True:
        name=input('Enter next name:')
        if name=='':
            break
        else:
            lst.append(name)
    for name in lst:
        if name in counter:
            counter[name]+=1
                #print('There are',countName[namers],'named',name)
        else:
            counter[name]=1
                #print('There is',countName[name],'named',name)
    for name in counter:
        if counter[name]>1:
            print('There are',counter[name],'named',name)
        else:
            print('There is',counter[name],'named',name)

'''
The two-player card game War is played with a standard deck of 52 cards.
A shuffled deck is evenly split among the two players who keep their decks face-down.
The game con- sists of battles until one of the players runs out of cards.
In a battle, each player reveals the card on top of their deck; the player with the
higher card takes both cards and adds them face-down to the bottom of her stack.
If both cards have the same value, a war occurs.
In a war, each player lays, face-down, their top three cards and picks one of them.
The player who picks the higher valued card adds all eight cards to the bottom of her deck.
In case of another tie, wars are repeated until a player wins and collects all cards on the table.
If a player runs out of cards before laying down three cards in a war, he is allowed to
complete the war, using his last card as his pick.

In War, the value of a number card is its rank, and the values of cards with
rank A, K, Q, and J are 14, 13, 12, and 11, respectively.

(a) Writeafunctionwar()thatsimulatesonegameofwarandreturnsatuplecontaining the number of
battles, wars, and two-round wars in the game. Note: When adding cards to the bottom of a
player’s deck, make sure to shuffle the cards first to add additional randomness to the simulation.

(b) Write a function warStats() that takes a positive integer n as input, simulates n games
of war, and computes the average number of battles, wars, and two-round wars.
'''
def war():
    import random
    p1=random.randrange(1,15)
    p2=random.randrange(1,15)
    p1count=26
    p2count=26
    battles=0
    wars=0
    twoWars=0
    while p1count!=0 and p2count!=0:
        if p1>p2:
            p1count+=1
            p2count-=1
            battles+=1
        elif p2>p1:
            p2count+=1
            p1count-=1
            battles+=1
        elif p1==p2:
            while p1==p2:#war
                aWar=0
                p1=random.randrange(1,15)
                p2=random.randrange(1,15)
                if p1>p2:
                    p1count+=3*aWar
                    p2count-+3*aWar
                    wars+=1
                    aWar+=1
                elif p2>p1:
                    p2count+=3*aWar
                    p1count-=3*aWar
                    wars+=1
                    aWar+=1
                elif p1==p2:
                    twoWars+=1
    else: #p1count==0 or p2count==0
        return (battles,wars,twoWars)
'''
Write a function intersect() that takes two lists, each containing
no duplicate val- ues, and returns a list containing values that are
present in both lists (i.e., the intersection of the two input lists)
'''
def intersect(lst1,lst2):
    lst=[]
    i=0
    j=0
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i]==lst2[j]:
                lst.append(lst1[i] and lst2[j])
    return lst
'''
Implement a function mystery() that takes as input a positive
integer n and answers this question: How many times can n be
halved (using integer division) before reaching 1? This value should returned.
'''
def mystery(n):
    count=0
    while True:
        n*.5>1
        if n*.5<=1:
            break
        else:
            n*=.5
            count+=1
    return count

'''
Temp Class - Object Oriented
'''
class Temp:
    def __init__(self,temp=0,unit='C'):
        self.t=temp
        self.u=str(unit)
    def __repr__(self):
        return f"Temp({self.t},'{self.u}')"
    def convert(self):
        if self.u=='C':
            self.t=(self.t*9/5)+32
            self.u='F'
        else:
            self.t=(self.t-32)*5/9
            self.u='C'
    def get(self):
        return self.t
    def __eq__(self,other):
        if self.u==other.u:
            return self.get()
        else:
            t.convert()
'''
Queue Object Oriented
'''
class Queue:

    def __init__(self,lst=[]):
        #self.q=[] before the lst=[] default
        self.q=list(lst)
    def __repr__(self):
        return "Queue({})".format(self.q)
    def enqueue(self,item):
        self.q.append(item)
    def dequeue(self):
        return self.q.pop # pop return, but still need it
    #indexing calls __getitem__
    #q[1]->Queue.__getitem__(q,1)
    def __getitem__(self,index):
        return self.q[index]
    def __setitem__(self,index,item):
        self.q[index]=item
    def __len__(self):
        return len(self.q)
    def __eq__self(self,other):
        return self.q==other.q


'''
Count amount of plural words in phrase
'''
def plurals(phrase):
    ans=0
    words=phrase.split()
    for char in words:
        if char[-1]=='s':
            ans+=1
    return ans

