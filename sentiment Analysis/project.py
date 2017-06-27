from bs4 import BeautifulSoup
from selenium import webdriver
import codecs
import tweetSearchAndAnalysis

def imdbWebScraping():
    nameOfCelebrities = []
    celebrityKeyValue = {}
    counter = 0
    URL = "http://m.imdb.com/feature/bornondate"
    driver = webdriver.Firefox()
    driver.get(URL)
    html = driver.page_source
    soup = BeautifulSoup(html, "html5lib")

    res = soup.find("section", "posters list")
    bornDate = res.findChild("h1").text
    celebrityNameList = []
    for i in res.findAll("a", "poster "):
        celebrityKeyValue[counter] = {}
        celebrityName = i.find("span", "title").text
        celebrityNameList.append(celebrityName)
        celebrityKeyValue[counter]["celebrityName"] = celebrityName
        celebrityKeyValue[counter]["celebrityImg"] = i.img["src"]
        profession, bestMovie = i.find("div", "detail").text.split(",")
        celebrityKeyValue[counter]["profession"] = profession
        celebrityKeyValue[counter]["bestMovie"] = bestMovie
        counter += 1

    return nameOfCelebrities, celebrityKeyValue

if __name__ == '__main__':
    nameOfCelebrities, celebrityKeyValue = imdbWebScraping()
    celebrity = tweetSearchAndAnalysis.tweetSearchAndAnalysis()
    outputFile = codecs.open("finalOutput.txt", 'w', "utf-8")


for i in range(10):
    celebrityName = celebrityKeyValue[i]["celebrityName"]
    celebrity.tweetSearch(celebrityName)
    celebrityKeyValue[i]["tSentiment"] = celebrity.tweetSentimentAnalysis()
    outputFile.write("Name of the celebrity: " + celebrityKeyValue[i]["celebrityName"] + "\n")
    outputFile.write("Celebrity Image: " + celebrityKeyValue[i]["celebrityImg"] + "\n")
    outputFile.write("Profession: " + celebrityKeyValue[i]["profession"] + "\n")
    outputFile.write("Best Work: " + celebrityKeyValue[i]["bestMovie"] + "\n")
    outputFile.write("Overall Sentiment on Twitter: " + celebrityKeyValue[i]["tSentiment"] + "\n")
    outputFile.write("\n\n")


outputFile.close()