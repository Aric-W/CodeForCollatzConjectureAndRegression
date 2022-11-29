import Hailstorm as H
import DMARCGMforfinal as DMAR
import LineOfBestFitGenerator as LN
import numpy as np

ints = H.FillInts(50)

storm = H.Hailstorm(ints)
x = np.arange(0,50,1)
y1 = LN.GenLeastSquaresL(ints,storm,x)

LN.PlotEverything(ints,storm,[y1],['red'],x)

#print(LN.ProdSum([2,3],[4,5],1,1))
