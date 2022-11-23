import numpy as np
import matplotlib.pyplot as plt
import math
import DMARCGMforfinal


#generates a list of integers up to n
def FillInts(n):
    i = n
    nums = []
    while (i > 0):
        nums.append(i)
        i=i-1
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



#generates Hailstone sequences for a given positive integer.
def Hailstorm(n):
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

def GiveFunc():
    return 10 + (1/50)*x

tup = Hailstorm(47)
print(tup[0])    
#print(tup[1])


nums = FillInts(50)
#powers7 = powers(2,10)
tsts = []

# i = 0
# while(i < len(powers7[0])):
#     tsts.append(Hailstorm(powers7[0][i])[0])
#     i = i + 1

i = 0
while(i < len(nums)):
     tsts.append(Hailstorm(nums[i])[0])
     i = i + 1


#plt.scatter(nums[0], tsts)

x = np.arange(0,50,1)
y = GiveFunc()
y2 = x
plt.xlabel("integers")
plt.ylabel("total stopping times")
plt.plot(x,y,'orange')
plt.plot(x,y2,'red')
plt.scatter(nums,tsts)
plt.show()