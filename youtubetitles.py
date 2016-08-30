import json
import requests
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
        wordList.sort()
        wordList.reverse()
        return wordList

def questCount(wordList):
        count = 0
        for i in range(len(wordList)):
                       for x in range(len(wordList[i][0])):
                               if wordList[i][0][x] == '?':
                                       count += 1
        return count
      
def exCount(wordList):
        count = 0
        for i in range(len(wordList)):
                       for x in range(len(wordList[i][0])):
                               if wordList[i][0][x] == '!':
                                       ount += 1
        return count


def countCaps(titleList):
        caps = []
        for i in range(len(titleList)):
                percent = 0.0
                capCount = 0.0
                for x in range(len(titleList[i])):
                            if titleList[i][x] == titleList[i][x].upper():
                               capCount += 1
                percent = capCount / len(titleList[i])
                caps.append(percent)
        return caps

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


def clickBaitPercentage(title, wordList):
        percent = 0.0
        tsum = 0.0
        words = title.split()
        for i in range(len(words)):
                if words[i] == words[i].upper():
                        tsum += 1
        percent = tsum/len(words)
        print percent

        CBWordCount = 0
        for i in range(len(words)):
                for w in range(len(wordList)):
                        if words[i] == wordList[w][1]:
                                CBWordCount += 1
        CBPercent = float(CBWordCount)/len(words)
        print CBPercent

        return percent * CBPercent
        
cBResult = getVids('https://www.googleapis.com/youtube/v3/search?part=snippet,id&type=video&channelId=UCxJf49T4iTO_jtzWX3rW_jg&maxResults=50&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU')
cBDict = makeDict(cBResult)
cBData = combineAllData(cBDict, 8, cBPt1, cBPt2)
cBTitles = getAllTitles(cBData)
cBWords = wordList(cBTitles)

normResult = getVids('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&publishedAfter=2014-06-25T00:00:00Z&publishedBefore=2014-07-01T23:59:59Z&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU')
normDict = makeDict(normResult)
normData = combineAllData(normDict, 15, normPt1, normPt2)
normTitles = getAllTitles(normData)
normWords = wordList(normTitles)

print "cBDict, cBData, cBTitles, cBWords, normDict, normData, normTitles, normWords"


        
#how to get vid id
#rdata['items'][0]['id']['videoId']
                
#get stats link
#https://www.googleapis.com/youtube/v3/videos?part=statistics&id=dl7CLaZFG1c&key=AIzaSyDnYJlcS_O0hzFRVvMdR2Cy
