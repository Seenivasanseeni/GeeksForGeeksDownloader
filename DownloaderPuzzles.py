import bs4
from tools import *
import os

def getAllLinks(url):
        html=downloadString(url)
        soup=bs4.BeautifulSoup(html,'html.parser')
        listsOfLinks=soup.find_all("ol")
        requiredList=listsOfLinks[0]
        downloadLinks=[]
        for item in requiredList.find_all("li"):
            link=item.a["href"]
            downloadLinks.append(link)

        return downloadLinks


def downloadPuzzles():
    root_url="https://www.geeksforgeeks.org/puzzles/"
    puzzleNo=1
    downloadDir="Puzzles"
    os.makedirs(downloadDir,exist_ok=True)

    for puzzleLink in getAllLinks(root_url):
        print("Dowloading ",puzzleLink)
        downloadAndSave(puzzleLink,fileName=downloadDir+"/Puzzle"+str(puzzleNo)+".html")
        puzzleNo+=1
    return

downloadPuzzles()
