import os
import re
import requests
import urllib
import time
import random

ROOT = ""
HEADERS = {
    "Accept":"text/plain, */*; q=0.01",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}
SLEEP_LIST = [0.8,1.35,1.8]

def findImageURL(file):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    with open(file, 'r', encoding="utf-8", errors="ignore") as fin:
        passage = fin.read()
    URL_list = re.findall(pattern, passage, re.I)
    t = []
    for name,url in URL_list:
        t.append([name,url])
    URL_list = t
    plus = 1
    for index,(name,url) in enumerate(URL_list):
        if not name:
            type = findImageType(url)
            new_name = "random_name_%d.%s" % (plus,type)
            plus = plus+1
            URL_list[index][0] = new_name
    return URL_list

def findImageType(image):
    pattern = r".*?\.(jpg)|(png)|(gif)|(jpeg)"
    return re.search(pattern, image).group()


class Downloader(object):
    def __init__(self):
        self._root = ROOT
        self.passage_list = []
        self.passage_type = "md"

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self,root):
        if not os.path.isdir(root) or not os.path.exists(root):
            raise "ROOT path is wrong or does not exists"
        if not os.path.exists(os.path.join(root,"image")):
            os.mkdir(os.path.join(root,"image"))
        self._root = root

    @root.deleter
    def root(self):
        print("You deleted the root file path")
        del self._root

    def getPassageList(self):
        for passage in os.listdir(self._root):
            name,type = os.path.splitext(passage)
            if type[1:]==self.passage_type:
                self.passage_list.append(passage)

    def download(self):
        for passage in self.passage_list:
            image_URL_list = findImageURL(os.path.join(self._root,passage))
            if not len(image_URL_list):
                continue
            image_dir =  os.path.join(self._root,"image",passage.split(".")[0])
            if not os.path.exists(image_dir):
                os.mkdir(image_dir)
            flag = True
            for name,URL in image_URL_list:
                image_path = os.path.join(image_dir,name)
                try:
                    downloadImageURL(name,URL,image_path)
                except Exception as error:
                    print("reason:",error)
                    print("error:",image_dir,"\n",name,URL,image_path)
                    flag = False
                    break
            if flag:
                self.replaceURL(passage)
            time.sleep(random.choice(SLEEP_LIST))

    def replaceURL(self,file):
        with open(os.path.join(self._root,file),'r',encoding="utf-8") as fin:
            passage = fin.read()

        pattern = r"!\[.*?\]\(.*?\)"
        URL_list = re.findall(pattern,passage)
        for URL in URL_list:
            start = URL.index("(")+1
            end = URL.index(")")
            old_url = URL[start:end]
            start = URL.index("[") + 1
            end = URL.index("]")
            name = URL[start:end]
            new_url = os.path.join(".","image",file.split(".")[0],name)
            passage = passage.replace(old_url,new_url)
        passage = passage.replace("\\","/")
        with open(os.path.join(self._root,file),'w',encoding="utf-8") as fout:
            fout.write(passage)

def downloadImageURL(name,URL,path):
    content =  requests.get(url=URL,headers=HEADERS).content
    with open(path,'wb') as fout:
        fout.write(content)


if __name__=='__main__':
    for dir in os.listdir("."):
        if os.path.isdir(dir):
            print(dir,"start!!!")
            downloader = Downloader()
            downloader.root = dir
            downloader.getPassageList()
            downloader.download()
            print(dir,"end")


