import bs4
import requests

def getamazonprice(productURL):
    res=requests.get('https://www.amazon.in/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_2?crid=13F2JHDW6TFL8&keywords=automate+the+boring+stuff+with+python&qid=1582268193&sprefix=automate+%2Caps%2C267&sr=8-2')
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text, 'html.parser')
    elems=soup.select('.inlineBlock-display')
    return elems[0].text.strip()





price = getamazonprice('https://www.amazon.in/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_2?crid=13F2JHDW6TFL8&keywords=automate+the+boring+stuff+with+python&qid=1582268193&sprefix=automate+%2Caps%2C267&sr=8-2')
print('price is ' + price)




