import requests
from bs4 import BeautifulSoup
headers={

}
res = requests.get('https://www.vipdage.com/txsp')
url = BeautifulSoup(res.text,'lxml').select('header div ul li a')[1:16]
del url[7]

# print(url)

xc = 0
for x in url:
    xc += 1
    a = x.text
    print(str(xc)+'、'+''.join(a).strip())

urlj = input('请输入要查询de序号\n')
yurl = []
for x1 in range(len(url)):
    yurl.append(str(url[x1]).split('"')[1].split('/')[-1])


urll = yurl[int(urlj)-1]

res1 = requests.get('https://www.vipdage.com'+'/'+urll)
surl = BeautifulSoup(res1.text,'lxml').select('section div div header h2 a')
for tx in surl:
    url2 = requests.get(tx.get('href'))
    surl2 = BeautifulSoup(url2.text, 'lxml').select('body section div article p ')[1]
    TXT = surl2.text.split('。')[1].replace('账号', '\n账号')[1:].replace('密码', ' 密码')
    print(TXT)
# file =open(urll+".txt",'w',encoding='utf-8')
