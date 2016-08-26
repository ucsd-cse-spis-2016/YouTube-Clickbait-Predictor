import json
import requests
import pprint #make sure to do pprint.pprint("string") when printing

#https://www.googleapis.com/youtube/v3/search?part=snippet&key=[API_KEY]
#After getting stuff from API, turns into code and stuff

def getVids(link):
        result = requests.get(link)
        return result

def makeDict(result):
        #makes into a dict
        rdata = json.loads(result.text)
        return rdata

def printAllTitles(rdata):
        #how to print the titles
        for i in range(50):
                pprint.pprint(rdata['items'][i]['snippet']['title'])
                

def getVidIds(rdata):
        ids = []
        for i in range (50):
                ids.append(rdata['items'][i]['id']['videoId'])
        return ids

def getTitleList(rdata):
        titles = []
        for i in range (50):
                titles.append(rdata['items'][i]['snippet']['title'])
        return titles

def makeStatsDict(idList, titleList):
        statsDict = {}
        for i in range(50):
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
