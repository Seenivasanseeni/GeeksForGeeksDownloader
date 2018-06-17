import bs4
from tools import *
import os

def getCompanyUrl():
    comapanyName="microsoft"
    root_url="https://www.geeksforgeeks.org/"+comapanyName+"-topics-interview-preparation/"
    return comapanyName,root_url
   


def getAllLinks(url):
    html=downloadString(url)
    soup=bs4.BeautifulSoup(html,'html.parser')
    listsOfLinks=soup.findAll("div",{"id":"content"})
    requiredList=listsOfLinks[0].find_all("li")
    downloadLinks=[]
    for listItem in requiredList:
        anchor=listItem.a
        link=anchor["href"]
        downloadLinks.append(link)
  
    return downloadLinks


def downloadAll():

    downloadDir,root_url=getCompanyUrl()
    
    os.makedirs(downloadDir,exist_ok=True)

    for link in getAllLinks(root_url):
        link=link.split("\\")[1][1:]
        print("Downloading",link)
        try:
            downloadAndSave(link,fileName=downloadDir+"/"+getFileNameFromURL(link))
        except:
            print("Error in downloading HTML file")

    print("Download Complete")

if(__name__=="__main__"):
    downloadAll()