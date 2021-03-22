import requests
import re
import time
import os

def generateImagename():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    print(time_stamp)
    stamp = ("".join(time_stamp.split()[0].split("-")) + "".join(time_stamp.split()[1].split(":"))).replace('.', '')
    print(stamp)
    return stamp + '.jpg'

url = 'https://m.baidu.com/sf/vsearch?pd=image_content&word=美女&tn=vsearch&atn=page'
ua = {
    'Host': 'imgstat.baidu.com',
    'Referer': 'https://image.baidu.com/',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not\"A\\Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36',
}
print(ua)
res = requests.get(url, headers=ua).text
print(res)
response = re.findall('"objurl":"(.*?)"', res)
os.system('rm -rf ./image/')
for url in response:
    print(url)
    img_name = generateImagename()
    img = requests.get(url).content
    if not os.path.exists('./image'):
        os.makedirs('./image')
        print('create image dir')

    with open('./image/%s'%img_name,'wb') as file:
        file.write(img)

