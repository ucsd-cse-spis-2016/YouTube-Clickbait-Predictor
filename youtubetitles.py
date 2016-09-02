import json
import requests
import math
import string
import numpy
from collections import defaultdict
import pprint #make sure to do pprint.pprint("string") when printing
import sklearn
from sklearn.linear_model import LogisticRegression


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
        '''finds CBRatio of title in titleList'''
        for t in statsList:
                if t[1] == title:
                        return t[0]

def findCBRatio2(link):
        '''finds CBRatio of any link on youtube'''
        vidId = ""
        CBRatio = 0
        for i in range(len(link)):
                if link[i] == "=":
                        vidId = link[(i+1):len(link)]
        result = getVids("https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+vidId+"&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU")
        rdata = makeDict(result)
        try:
                likes = float(rdata['items'][0]['statistics']['likeCount'])
                dislikes = float(rdata['items'][0]['statistics']['dislikeCount'])
                views = float(rdata['items'][0]['statistics']['viewCount'])

                CBRatio = ((dislikes - likes)/(likes + dislikes)) / views
        except:
                CBRatio = 0

        return CBRatio

def getAPIfromLink(link):
        vidId = ""
        CBRatio = 0
        for i in range(len(link)):
                if link[i] == "=":
                        vidId = link[(i+1):len(link)]
                        break
        APILink = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id=" + vidId + "&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU"
        return APILink

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

def countChars(title):
        count = 0
        for i in range(len(title)):
                if title[i] != " ":
                        count += 1
        return count

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



print "Type 'begin()' to start the program"
def begin():
        print "Please wait for 3 minutes while the data loads."
                       
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
        

        print "Done"

        def feature(datum, wordId):
                feat = [0] * len(words)
                r = text_to_wordlist(datum)
                for w in r:
                        if w in words:
                                feat[wordId[w]] += 1
                feat.append(1)
                feat.append(countCaps(datum))
                feat.append(countChars(datum))
                feat.append(countPunct(datum))
                return feat


        def feature2(datum, statsList):
                feat = []

                feat.append(countChars(datum))
                feat.append(countCaps(datum))
                feat.append(countPunct(datum))
                feat.append(findCBRatio(datum, statsList))
                return feat

        def feature2a(link):
                feat = []
                APIData = getAPIfromLink(link)       

                feat.append(len(getTitleList(makeDict(getVids(APIData)))))
                feat.append(countCaps(getTitleList(makeDict(getVids(APIData)))))
                feat.append(countPunct(getTitleList(makeDict(getVids(APIData)))))
                feat.append(findCBRatio2(link))
                return feat
 

        
        def ownTitle(title):
                X = [feature(d, wordId) for d in titleList]
                y = [1] * len(cBTitles) + [0] * len(normTitles)
                logistic = LogisticRegression()
                lr = logistic.fit(X, y)

                titleFeat = feature(title, wordId)
                prediction = lr.predict_proba(titleFeat)[0][1] * 100
                print "The probability that your title is clickbait is: ", prediction, "%"
                return ""
        def youtubeVideo(link):
                X = [feature2(d, statsList) for d in titleList]
                y = [1] * len(cBTitles) + [0] * len(normTitles)
                logistic = LogisticRegression()
                lr = logistic.fit(X, y)

                titleFeat = feature2a(link)
                prediction = lr.predict_proba(titleFeat)[0][1] * 100
                print "The probability that this video is clickbait is: ", prediction, "%"
                return ""
        def prompts():
                response = raw_input("Type 1 to type your own title or type 2 to enter a link: ")
                if response == "1":
                        userInput = raw_input('Please type in your title: ')
                        print ownTitle(userInput)
                elif response == "2":
                        userInput = raw_input('Please type in the link: ')
                        print youtubeVideo(userInput)
                else:
                        print "Please enter either 1 or 2."
                prompts()
        
        prompts()
        return ""

        
#how to get vid id
#rdata['items'][0]['id']['videoId']
                
#get stats link
#https://www.googleapis.com/youtube/v3/videos?part=statistics&id=dl7CLaZFG1c&key=AIzaSyDnYJlcS_O0hzFRVvMdR2Cy
