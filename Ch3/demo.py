import requests, json, pyprind, sys, shutil, re
from bs4 import BeautifulSoup

def replace_characterName(i):
    text = i.text.replace('\n','').strip()
    return re.sub(r'(.)*má(.)*','mmmm',text)

def savetext(url):
    text=requests.get(url)
    soup = BeautifulSoup(text.text)
    num = 0
    with open('test.json', 'w', encoding='utf-8') as f:
        tmp = ""
        for i, counter in zip(soup.select('table tr tbody td'), range(1, len(soup.select('table tr tbody td'))+1)):
            tmp += replace_characterName(i)
            if counter % 2 == 0:
                f.write(tmp+'\n')
                tmp = ""
            num+=1
        print("total amounts is:" + str(num))

savetext("http://www.tiengvietonline.com.vn/index.php/component/elearning/?section=contentlesson&task=view&id=1&Itemid=145")