import requests
import time

'''
****************
CONFIG
****************
'''

dataURL = "http://pulsedata57.hkustvis.org/data"
allowedPeopleLessThan = 400
attemptsMax = 100
watchKeyword = "ct1"
from barkKey import barkKey
barkURL = "https://api.day.app/" + barkKey + "/"

MSGtitle = "Eating Time"
MSGbody = "Less people than your setting"

barkURL += MSGtitle + "/" + MSGbody

'''
****************
END OF CONFIG
****************
'''

def getRawDate():
    try:
        response= requests.get(dataURL)
        if response.status_code!=200:
            return None
    except RequestException:
        return None
    raw = response.json()
    return raw['count']['zones'][watchKeyword]

def main():
    attempts = 0
    rev = getRawDate()
    while rev == None:
        attempts += 1
        time.sleep(3)
        rev = getRawDate()
        if attempts > attemptsMax:
            return -1
    if rev <= allowedPeopleLessThan:
        while rev != 200:
            response = requests.get(barkURL)
            rev = response.json()["code"]

if __name__ == "__main__":
    main()
