import numpy as np
import matplotlib.pyplot as plt




#generates a list of integers up to n

def FillInts(n):
    i = n
    nums = []
    while (i > 0):
        nums.append(i)
        i=i-1
    return nums

def MultiplesOf(n,m):
    i = m
    nums = []
    while(i > 0):
        nums.append(n*i)
        i = i-1
    return nums

#generates list of powers of k up to e
#also generates list of strings k^0,k^1,...,k^e
#returns them as a tuple
def powers(k,e):
    res = []
    nums = []
    i = 0
    while (i <= e):
        res.append(pow(k,i))
        nums.append(str(k) + "^" +  str(i))
        i = i+1
    return res,nums



#generates Hailstone sequence for a given positive integer n.
#returns a tuple with tuple[0] = total stopping time of n
#tuple[1] is the hailstone sequence of n
def Hailstone(n):
    seq = []
    xn = n
    tst = 1
    while (xn > 1):
        if (xn % 2 == 0):
            xn =  np.floor(xn/2)
        elif (xn % 2 == 1):
            xn = np.floor(3*xn + 1)
        seq.append(xn)
        tst = tst + 1
    return tst, seq


def Hailstorm(integers, injective=False):
    i = 0
   
    stormSize = len(integers)

    if(injective):
        tsts = set();
        while(i < stormSize):
            tsts.append(Hailstone(integers[i])[0])
            i = i+1
    else:
         tsts = []
         while(i < stormSize):
            tsts.append(Hailstone(integers[i])[0])
            i = i+1
        

    return tsts


