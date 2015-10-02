from bs4 import BeautifulSoup as Soup
import random
import pyperclip

random.seed()

sourceFile = 'RandomWords.html'
openFile = open(sourceFile)

soup = Soup(openFile, 'html.parser')

randList = []

for li in soup.findAll('li'):
    randList += li

result = random.choice(randList)
pyperclip.copy(result)
print("added %s to clipboard" % result)
