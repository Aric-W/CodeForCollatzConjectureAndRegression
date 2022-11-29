import DMARCGMforfinal as UseDmar
import numpy as np
import matplotlib.pyplot as plt



#with numpy arrays we can do matrix by vector mult
# and matrix by matrix mult with the @ operator

#Takes a list of numbers and raises each of them to a power and
#sums these numbers
def SpecializedSum(numbers,pw):
    i = 0
    sum = 0
    while(i < len(numbers)):
        sum = sum + pow(numbers[i],pw)
        i = i + 1
    return np.array(numbers),sum


#numbers1 and numbers2 must have the same dimension
#will multiply numbers rased to a specified power in two lists in order
def ProdSum(numbers1,numbers2,power1,power2):
    sum = 0
    for i in range(0,len(numbers1)):
        sum = sum+pow(numbers1[i],power1)*pow(numbers2[i],power2)
    return sum

#xs and ys must have the same dimension
#uses DMAR conjugate gradient method (with starting point x0)  to 
# calculate the regression parameters for 
#Linear Linear regression given list of points (xi,yi)
def SolveForRegParamL(xs,ys):
    A = np.array([[(len(xs)+len(ys))/2,SpecializedSum(xs,1)[1]],[SpecializedSum(xs,1)[1],SpecializedSum(xs,2)[1]]])
    b = np.array([SpecializedSum(ys,1)[1],ProdSum(xs,ys,1,1)])

    #starts at the origin as the initial guess 
    x0 = np.array([1,1])
    aT = UseDmar.LinearCGDMAR(A, b, x0, tol=1e-7)

    return aT

#gives us the actual line of best fit
def GenLeastSquaresL(xs,ys,x):
    regParam = SolveForRegParamL(xs,ys)

    y = regParam[0] + regParam[1]*x

    return y


#colors will always be a list
def PlotEverything(data,tsts,lines,colors,range):

    
    

    plt.scatter(data, tsts)
    plt.xlabel("integers")
    plt.ylabel("total stopping times")

   
    i=0
    for line in lines:
        plt.plot(range,line,colors[i])
        i=i+1

    

    

    plt.show()

