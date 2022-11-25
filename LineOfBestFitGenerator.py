import DMARCGMforfinal as UseDmar
import numpy as np



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
        sum = pow(numbers1[i],power1)*pow(numbers2[i],power2)
    return sum

#xs and ys must have the same dimension
#uses DMAR conjugate gradient method  to 
# calculate the regression parameters for 
#Linear Linear regression given list of points (xi,yi)
def SolveForRegParamL(xs,ys,x0):
    A = np.array[[(len(xs)+len(ys))/2,SpecializedSum(xs,1)],[SpecializedSum(xs,1),SpecializedSum(xs,2)]]
    b = np.array([SpecializedSum(ys,1),ProdSum(xs,ys,1,1)])

    aT = UseDmar.LinearCGDMAR(A, b, x0, tol=1e-7)

    return aT



