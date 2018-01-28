import matplotlib.pyplot as pl
import numpy as np

def savePlot(wordFreqDict, imageName):

    indexes = np.arange(len(wordFreqDict.keys()))
    ax = pl.subplot(111)
    barWidth = 0.35
    ax.bar(indexes, wordFreqDict.values(), width=barWidth, align='center')
    pl.xticks(indexes, wordFreqDict.keys())

    pl.ylabel("Frequency")
    pl.xlabel("Words")
    pl.savefig(imageName)







