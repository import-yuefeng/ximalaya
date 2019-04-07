import json
import requests
import time

albumId = input("[~] Enter your albumId: ")

fp = open("result-json-{}.txt".format(albumId), "r", encoding="UTF-8")
content = eval(fp.read())

HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) \
        Gecko/20100101 Firefox/58.0',
    'Referer':'https://www.ximalaya.com'    
}

for item in content:
    try:
        with open('./%s.m4a' % str(item["musicIndex"]), 'wb') as f:
            response = requests.get(url=item["musicUrl"], headers=HEADERS)
            f.write(response.content)
            time.sleep(1)
    except:
        print("[-] 出错!, 最后一个下载的内容为%s")
        exit(1)
    else:
        print("\r已下载-> ".format(item["musicIndex"])+str(item["musicIndex"]), end="")

