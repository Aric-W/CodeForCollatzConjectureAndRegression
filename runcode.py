import Hailstorm as H
import LineOfBestFitGenerator as LN
import numpy as np

data = H.FillInts(50000)
streams = H.SplitIntoStreams(data,9)

print("Done")
#LN.PlotEverything(data)


