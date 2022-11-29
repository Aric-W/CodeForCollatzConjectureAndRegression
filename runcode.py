import Hailstorm as H
import DMARCGMforfinal as DMAR
import LineOfBestFitGenerator as LN
import numpy as np

ints1 = H.FillInts(5000)
ints2 = H.MultiplesOf(2,500)

storm1 = H.Hailstorm(ints1)
storm2 = H.Hailstorm(ints2)

x = np.arange(0,5001,1)
y1 = LN.GenLeastSquaresL(ints1,storm1,x)
y2 = LN.GenLeastSquaresL(ints2,storm2,x)
y3 = LN.GenLeastSquaresQ(ints1,storm1,x)

LN.PlotEverything(ints1,storm1,[y1,y2,y3],['red','green','orange'],x)

#print(LN.ProdSum([2,3],[4,5],1,1))
