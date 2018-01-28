import matplotlib.pyplot as pl
import numpy as np

'''
Purpose: This file includes functions useful fro displaying word frequency histograms

'''



'''
input: words is a string of words
output: array of words with the topN frequencies and their frequencies, every element is 
a 2D array (word, frequency)
'''




'''
input : numpy array, 2D of words and freqs
'''

def savePlot(wordFreqDict, imageName):

    indexes = np.arange(len(wordFreqDict.keys()))
    ax = pl.subplot(111)
    barWidth = 0.35
    ax.bar(indexes, wordFreqDict.values(), width=barWidth, align='center')
    pl.xticks(indexes, wordFreqDict.keys())

    pl.ylabel("Frequency")
    pl.xlabel("Words")
    pl.savefig(imageName)







