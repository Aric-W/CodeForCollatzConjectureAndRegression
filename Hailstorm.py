import numpy as np
import matplotlib.pyplot as plt




#generates a list of integers up to n

def FillInts(n):
    i = 1
    nums = []
    while (i < n+1):
        nums.append(i)
        i=i+1
    return nums


#generates Hailstone sequence for a given positive integer n.
#returns a tuple with tuple[0] = total stopping time of n
#tuple[1] is the hailstone sequence of n
def Hailstone(n):
    seq = []
    xn = n
    tst = 0
    
    if(n == 1):
        return 3,[4,2,1]
    while (xn > 1):
        if (xn % 2 == 0):
            xn =  np.floor(xn/2)
        elif (xn % 2 == 1):
            xn = np.floor(3*xn + 1)
        seq.append(xn)
        tst = tst + 1
    return tst, seq

#splits the set of integers up into cosets and calculates tst
#thus creates the separate "streams" of the storm
def SplitIntoStreams(data, modulus):

    cosets = []
    remainder = 0
    while(remainder < modulus):
        cosets.append([])
        remainder = remainder + 1

    j = 0
    for i in range(1,len(data)):
        cosets[j%modulus].append(i)
        j=j+1
    

    return cosets

#will generate a list of total stopping times from a list of integers
def Hailstorm(integers):
    
    tsts = []

    for i in range(0,len(integers)):
        tsts.append(Hailstone(integers[i])[0])

    return tsts

        


    











