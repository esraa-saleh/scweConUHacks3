
import json
from watson_developer_cloud import SpeechToTextV1
import plotter
from collections import Counter
from nltk.corpus import stopwords
'''
outfile needs to be with extension .json

'''
OK = 1
N_OK = -1

def __transcribe__(fileWav,  dirPath=''):
    # bluemix authentication username
    username = '808cf5d9-039c-4190-9e12-0936377e14ff'

    # bluemix authentication password
    password = 'NgEXU2SQAPyv'

    i = 1
    extensionList = []
    while (fileWav[-i] != '.'):
        extensionList.append(fileWav[-i])
        i += 1

    extension = ''.join(extensionList)[::-1]

    stt = SpeechToTextV1(username=username, password=password)
    audio_file = open(dirPath + fileWav, "rb")

    result = stt.recognize(audio_file, content_type="audio/" + extension,
                           continuous=True, timestamps=False,
                           max_alternatives=1)
    return result



def __jsonToTranscription__(jsonResult):
    allWords = []
    for i in range(len(jsonResult['results'])):
        allWords.extend(list(jsonResult['results'][i]['alternatives'][0]['transcript']))
    result = "".join(allWords)
    return result




def __getWordsAndFreqs__(wordsStr, topN=2):
    words = wordsStr.split()
    wordsNoStops = [w for w in words if (w not in stopwords.words('english') and w != '%HESITATION' and w != 'I')]

    counts = Counter(wordsNoStops)

    if (len(counts) < topN):
        return N_OK, {}

    # counts is a dictionary of words mapped to their frequencies
    wAndF = counts.most_common(topN)
    size = len(wAndF)

    wordFreqDict = {}
    for i in range(size):
        wordFreqDict[wAndF[i][0]] = wAndF[i][1]

    return OK, wordFreqDict



def waveToFreqsDict(numWords, fileWavName, dirPath =''):
    jsonResult = __transcribe__(fileWavName, dirPath)
    transcription = __jsonToTranscription__(jsonResult)
    sig, wordsFreqsDict = __getWordsAndFreqs__(transcription, topN=numWords)
    return sig, wordsFreqsDict

def getFreqPlot(wordsFreqsDict):
    plotter.savePlot(wordsFreqsDict)



if __name__ == '__main__':

    # # Open audio file(.wav) in wave format
    dirPath = '/Users/esraasaleh/PycharmProjects/scweAtConUHacks/scweConUHacks3/'
    fileWav = 'test.mp3'
    sig, myDict = waveToFreqsDict(numWords=5, fileWavName='beauty.mp3')
    getFreqPlot(myDict)
