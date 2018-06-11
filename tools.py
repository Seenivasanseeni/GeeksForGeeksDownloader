import requests

def downloadAndSave(url,fileName="download.html"):
    response=requests.request("GET",url)
    with open(fileName,"wb") as file:
        file.write(response.content)


def downloadString(url):
    response=requests.request("GET",url)
    return str(response.content)
