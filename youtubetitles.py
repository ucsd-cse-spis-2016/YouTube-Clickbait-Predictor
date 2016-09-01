import json
import requests
import math
import string
import numpy
from collections import defaultdict
import pprint #make sure to do pprint.pprint("string") when printing

#https://www.googleapis.com/youtube/v3/search?part=snippet&key=[API_KEY]
#After getting stuff from API, turns into code and stuff


cBPt1 = "https://www.googleapis.com/youtube/v3/search?part=snippet,id&type=video&"
cBPt2= "&channelId=UCxJf49T4iTO_jtzWX3rW_jg&maxResults=50&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU"
normPt1 = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&publishedAfter=2014-06-25T00:00:00Z&"
normPt2 = "&publishedBefore=2014-07-01T23:59:59Z&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU"


def getVids(link):
        result = requests.get(link)
        return result

def getNextVids(rdata, linkPt1, linkPt2):
        link = linkPt1 + "pageToken=" + str(rdata['nextPageToken']) + linkPt2
        result = getVids(link)
        newData = makeDict(result)
        return newData

def combineAllData(rdata, numPages, linkPt1, linkPt2):
        newData = []
        tempData = {}
        for i in range(numPages):
                if i == 0:
                        newData.append(rdata)
                        tempData = rdata
                else:
                        tempData = getNextVids(tempData, linkPt1, linkPt2)
                        newData.append(tempData)
        return newData

        
def makeDict(result):
        #makes into a dict
        rdata = json.loads(result.text)
        return rdata

def getVidIds(rdata):
        ids = []
        for i in range (len(rdata['items'])):
                ids.append(rdata['items'][i]['id']['videoId'])
        return ids

def getAllVidIds(dictList):
        ids = []
        for i in range(len(dictList)):
                ids = ids + getVidIds(dictList[i])
        return ids

def getTitleList(rdata):
        titles = []
        for i in range (len(rdata['items'])):
                titles.append(rdata['items'][i]['snippet']['title'])
        return titles

def wordList(titleList):
        titleDict = defaultdict(int)
        listOfWords = []
        for i in range(len(titleList)):
                splitSent = titleList[i].split()
                listOfWords += splitSent

        for i in range(len(listOfWords)):
                try:
                        titleDict[listOfWords[i]] = 1 + titleDict[listOfWords[i]]
                except:
                        titleDict[listOfWords[i]] = 1
        wordList = [[titleDict[d],d] for d in titleDict.keys()]
        for i in range(len(wordList)):
                wordList[i][1] = wordList[i][1].lower()
        
        wordList.sort()
        wordList.reverse()
        return wordList

def makeWords(titleList):
        wordCountDict = defaultdict(int)
        for tl in titleList:
                for w in text_to_wordlist(tl):
                        wordCountDict[w] += 1
        return wordCountDict


def countPunct(title):
        count = 0
        for i in range(len(title)):
                puncs = set(string.punctuation)
                for p in puncs:
                        if title[i] == p:
                                count += 1
        return count

def countCaps(title):
        '''returns a percentage of the capital characters'''
        count = 0
        length = len(title)
        for i in range(len(title)):
                if title[i] == title[i].upper() and title[i] != " ":
                        count += 1
                if title[i] == " ":
                        length -= 1
        percent = float(count) / length
        return percent

def getAllTitles(dictList):
        titles = []
        for i in range(len(dictList)):
                titles = titles + getTitleList(dictList[i])
        return titles

def makeStatsDict(idList, titleList):
        statsDict = {}
        for i in range(len(idList)):
                tempList ={}
                result=getVids("https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+idList[i]+"&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU")
                rdata = makeDict(result)
                try:
                        tempList['Likes'] = (rdata['items'][0]['statistics'][u'likeCount'])
                        tempList['Dislikes'] = (rdata['items'][0]['statistics'][u'dislikeCount'])
                        tempList['Views'] = (rdata['items'][0]['statistics'][u'viewCount'])
                        tempList['Id'] = (rdata['items'][0]['id'])

                        likes = float(rdata['items'][0]['statistics']['likeCount'])
                        dislikes = float(rdata['items'][0]['statistics']['dislikeCount'])
                        views = float(rdata['items'][0]['statistics']['viewCount'])
                
                        tempList['CBRatio'] = ((dislikes - likes)/(likes + dislikes)) / views
                        statsDict[titleList[i]] = tempList
                except:
                        print "No Likes/Dislikes for " + titleList[i]

        return statsDict

def makeStatsList(idList, titleList):
        statsList = []
        for i in range(len(idList)):
                tempList =[]
                result=getVids("https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+idList[i]+"&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU")
                rdata = makeDict(result)
                try:
                        likes = float(rdata['items'][0]['statistics']['likeCount'])
                        dislikes = float(rdata['items'][0]['statistics']['dislikeCount'])
                        views = float(rdata['items'][0]['statistics']['viewCount'])

                        CBRatio = ((dislikes - likes)/(likes + dislikes)) / views
                        statsList.append([CBRatio, titleList[i]])
                except:
                        CBRatio = 0
                        statsList.append([CBRatio, titleList[i]])

        return statsList

def findCBRatio(title, statsList):
        for t in statsList:
                if t[1] == title:
                        return t[0]

def findCBRatio2(link):
        vidId = ""
        for i in range(len(link)):
                if link[i] == "=":
                        vidId = link[(i+1):len(link)]
        result = getVids("https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+vidId+"&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU")
        rdata = makeDict(result)
        return vidId

def makeCBList(statsDict):
        CBList = []
        titleList = statsDict.keys()
        for i in range (len(titleList)):
                tempList = []

                tempList.append(statsDict[titleList[i]]['CBRatio'])
                tempList.append(titleList[i])
                tempList.append(statsDict[titleList[i]]['Id'])
                
                CBList.append(tempList)
        return CBList

def tfidf(cBWords, normWords, normTitles):
        tfidfList = []
        for i in range(len(cBWords)):
                idf = 0
                tempList = []
                for x in range(len(normWords)):
                        if cBWords[i][1] == normWords[x][1]:
                                idf = normWords[x][0]
                                tempList = [cBWords[i][0] * math.log(len(normTitles)/(idf + 1)), cBWords[i][1]]
                                tfidfList.append(tempList)
                                
        return tfidfList

def text_to_wordlist(text):
    r = [c for c in text if c not in set(string.punctuation)]
    rs = ''.join(r)
    rs = rs.lower()
    rs = rs.split()
    return rs

#should work for putting in a string title
def feature(datum, wordId):
        feat = [0] * len(words)
        r = text_to_wordlist(datum)
        for w in r:
                if w in words:
                        feat[wordId[w]] += 1
        feat.append(1)
        feat.append(countCaps(datum))
        feat.append(countPunct(datum))
        return feat

#Will only work for titles that are actually in the database
def feature2(datum, statsList, wordId):
        feat = []
        feat.append(countCaps(datum))
        feat.append(countPunct(datum))
        feat.append(findCBRatio(datum, statsList))
        return feat

def declareVariables():
        print "Please wait 2 minutes as the computer thinks."
               
        cBResult = getVids('https://www.googleapis.com/youtube/v3/search?part=snippet,id&type=video&channelId=UCxJf49T4iTO_jtzWX3rW_jg&maxResults=50&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU')
        cBDict = makeDict(cBResult)
        cBData = combineAllData(cBDict, 8, cBPt1, cBPt2)
        cBTitles = getAllTitles(cBData)

        normResult = getVids('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&publishedAfter=2014-06-25T00:00:00Z&publishedBefore=2014-07-01T23:59:59Z&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU')
        normDict = makeDict(normResult)
        normData = combineAllData(normDict, 15, normPt1, normPt2)
        normTitles = getAllTitles(normData)

        titleList = cBTitles + normTitles

        cBWords = wordList(cBTitles)
        normWords = wordList(normTitles)

        cBIds = getAllVidIds(cBData)
        normIds = []
        for i in range(15):
                for x in range(len(normData[i]['items'])):
                        normIds.append(normData[0]['items'][x]['id']['videoId'])

        allIds = cBIds + normIds
        statsList = makeStatsList(allIds, titleList)

        allWordsDict = makeWords(cBTitles + normTitles)
        allWords = [[allWordsDict[w], w] for w in allWordsDict.keys()]
        allWords.sort()
        allWords.reverse()
        words = [w[1] for w in allWords[:700]]
        wordId = dict(zip(words, range(700)))


        X = [feature2(d, statsList, wordId) for d in titleList]
        y = [1] * len(cBTitles) + [0] * len(normTitles) 

        print "Done"

print "Type 'defineVariables()' to declare variables"

        
#how to get vid id
#rdata['items'][0]['id']['videoId']
                
#get stats link
#https://www.googleapis.com/youtube/v3/videos?part=statistics&id=dl7CLaZFG1c&key=AIzaSyDnYJlcS_O0hzFRVvMdR2Cy
