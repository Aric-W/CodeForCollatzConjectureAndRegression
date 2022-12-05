import Hailstorm as H
import LineOfBestFitGenerator as LN
import numpy as np
import matplotlib.pyplot as plt

#data numbers have to be in order
data = H.FillInts(500)
LN.PlotEverything(data,True)
streams = H.SplitIntoStreams(data,47)

#The PlotEverything method just takes a set of x-values and 
# from that generates the appropriate
#y values and the regression lines as well as a scatter plot of the (x,y)
#data points.
#in addition there is a second parameter that should be given the value of True
#if the user wishes to plot multiple datasets
# after the first in multiple pyplot windows.

LN.PlotEverything(streams[46],True)
#first 18 primes odd primes with 41,43,47,53 removed
data = [3,5,7,11,13,17,19,23,29,37,57,59,61,67]
LN.PlotEverything(data)
#LN.PlotEverything(streams[0])

plt.show()





