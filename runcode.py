import Hailstorm as H
import LineOfBestFitGenerator as LN
import numpy as np

data = H.FillInts(50)
streams = H.SplitIntoStreams(data,9)


LN.PlotEverything(streams[1])

print(H.Hailstone(11))


