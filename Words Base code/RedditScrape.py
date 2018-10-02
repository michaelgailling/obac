import urllib.request
import json

subreddit = "announcements"
url = "https://www.reddit.com/r/"+subreddit+"/.json"
hdr = { 'User-Agent' : 'metaprinter' }
req = urllib.request.Request(url, headers=hdr)
resp = urllib.request.urlopen(req).read()

resp = resp.decode('utf8')

resp = json.loads(resp)

print(json.dumps(resp,indent=4,sort_keys=True))

for i in resp["data"]["children"]:
    print("Title: " + i["data"]["title"])
    print("Selftext: " + i["data"]["selftext"])
    print("Comments url: " + i["data"]["url"])