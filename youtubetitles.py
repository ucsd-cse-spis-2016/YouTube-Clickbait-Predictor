import json
import requests
import pprint #make sure to do pprint.pprint("string") when printing

#https://www.googleapis.com/youtube/v3/search?part=snippet&key=[API_KEY]
#After getting stuff from API, turns into code and stuff

def getVids(link):
        result = requests.get(link)
        return result

linkPt1 = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&publishedAfter=2014-06-25T00:00:00Z&"
linkPt2= "&publishedBefore=2014-07-01T23:59:59Z&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU"
def getNextVids(rdata):
        link = linkPt1 + "pageToken=" + str(rdata['nextPageToken']) + linkPt2
        result = getVids(link)
        newData = makeDict(result)
        return newData

def combineAllRdata(rdata, numPages):
        newData = []
        tempData = {}
        for i in range(numPages):
                if i == 0:
                        newData.append(rdata)
                        tempData = rdata
                else:
                        tempData = getNextVids(tempData)
                        newData.append(tempData)
        return newData

        
def makeDict(result):
        #makes into a dict
        rdata = json.loads(result.text)
        return rdata

def getVidIds(rdata):
        ids = []
        for i in range (50):
                ids.append(rdata['items'][i]['id']['videoId'])
        return ids

def getAllVidIds(dictList):
        ids = []
        for i in range(len(dictList)):
                ids = ids + getVidIds(dictList[i])
        return ids

def getTitleList(rdata):
        titles = []
        for i in range (50):
                titles.append(rdata['items'][i]['snippet']['title'])
        return titles

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

                tempList['Likes'] = (rdata['items'][0]['statistics']['likeCount'])
                tempList['Dislikes'] = (rdata['items'][0]['statistics']['dislikeCount'])
                tempList['Views'] = (rdata['items'][0]['statistics']['viewCount'])

                likes = float(rdata['items'][0]['statistics']['likeCount'])
                dislikes = float(rdata['items'][0]['statistics']['dislikeCount'])
                views = float(rdata['items'][0]['statistics']['viewCount'])
                
                tempList['CBRatio'] = ((dislikes - likes)/(likes + dislikes)) / views
                
                statsDict[titleList[i]] = tempList

        return statsDict

def makeCBList(statsDict):
        CBList = []
        titleList = statsDict.keys()
        for i in range (len(titleList)):
                tempList = []

                tempList.append(statsDict[titleList[i]]['CBRatio'])
                tempList.append(titleList[i])
                
                CBList.append(tempList)
        return CBList
                
        

        

print "result = getVids('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&publishedAfter=2014-06-25T00:00:00Z&publishedBefore=2014-07-01T23:59:59Z&key=AIzaSyDnYJlcS_O0hzFRVvMdR2CympAqFS4ClLU')"
print "rdata = makeDict(result)"
print "titleList = getTitleList(rdata)"
print "idList = getVidIds(rdata)"
print "statsDict = makeStatsDict(idList, titleList)"
        
#how to get vid id
#rdata['items'][0]['id']['videoId']
                
#get stats link
#https://www.googleapis.com/youtube/v3/videos?part=statistics&id=dl7CLaZFG1c&key=AIzaSyDnYJlcS_O0hzFRVvMdR2Cy
