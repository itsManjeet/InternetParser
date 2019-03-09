#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import sys
_URL_ = "https://en.wikipedia.org/wiki/"

# 2 : article not found on wikipedia
#
#
# 5 : InfoCard is not present
#

class Wikipedia:
    def Start(self,word):
        if " " in word:
            word.replace(" ","_")
        page = requests.get(_URL_ + word)
        self.soup = BeautifulSoup(page.text, 'html5lib')
        self.content = self.soup.find('div',attrs={'class':'mw-body'})
        if "Wikipedia does not have an article with this exact name" in self.content.text.strip():
            return 2

    def GetInfoCard(self):
        infocard = self.content.find_all('table')
        self.InfoCard = {}
        for i in infocard:
            try:
                if i.get('class')[0] == 'infobox':
                    for j in i.find_all('tr'):
                        try:
                            self.InfoCard[j.find('th').text.strip()] = j.find('td').text.strip()
                        except AttributeError:
                            pass
            except TypeError as e:
                if str(e) == "'NoneType' object is not subscriptable":
                    return 5
                
        return 5

    def GetContentHeadings(self):
        headings = self.content.find_all('span')
        for i in headings:
            if i.get('title') == None:
                continue
            print(i.get('title'))
