import json
import requests
import pprint #make sure to do pprint.pprint("string") when printing


#After getting stuff from API, turns into code and stuff
result = requests.get("insert link here")

#makes into a dict
rdata = json.loads(result.text)

#how to print the titles
for i in range(totalResults):
	pprint.pprint(rdata['items'][i]['snippet']['title'])

