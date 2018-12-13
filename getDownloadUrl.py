import requests
import json
import sys
import time

BASE_URL = " https://www.ximalaya.com/revision/play/album?albumId=%s&pageNum=%s&sort=0&pageSize=30"
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) \
        Gecko/20100101 Firefox/58.0',
    'Referer':'https://www.ximalaya.com'    
}

resultJson = []


albumId = input("[~] Enter your albumId: ")
pageStartNum = int(input("[~] Enter startPage: "))
pageEndNum = int(input("[~] Enter endPage: "))


for page in range(pageStartNum, pageEndNum):

    url = BASE_URL%(albumId, page)
    response = requests.get(url, headers=HEADERS)
    response = response.json()

    for musicData in response["data"]["tracksAudioPlay"]:

        musicUrl = musicData["src"]
        musicIndex = musicData["index"]

        resultJson.append({
            "musicUrl":musicUrl,
            "musicIndex":musicIndex,
            })
    done = int(pageEndNum * page / pageEndNum)
    sys.stdout.write("\r[%s%s]下载进度: %s%%" % ('█' * done, ' ' * (pageEndNum - done), float(page/pageEndNum*100)))
    sys.stdout.flush()
    time.sleep(1)


fp = open("result-json-{}.txt".format(albumId), "w+", encoding="UTF-8")
fp.write(json.dumps(resultJson))
fp.close()
