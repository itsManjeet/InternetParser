#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import sys
import re

URL = "https://en.wikipedia.org/wiki/"
PAGE_MISSING_LINES = "Wikipedia does not have an article with this exact name"
class wikipedia:
    def __init__(self,ask):
        ask = ask.replace(" ","_")

        self.__url__ = URL + ask
        self.__page__ = requests.get(self.__url__)
        self.__soup__ = BeautifulSoup(self.__page__.text,'html5lib')
        self.__content__ = self.__soup__.find('div',attrs={'class':'mw-body'})

    def exist(self):
        if PAGE_MISSING_LINES in self.__content__.text.strip():
            return False
        else:
            return True
    
    def infocard(self):
        tables = self.__content__.find_all('table')
        infocard = {}
        for i in tables:
            try:
                if i.get('class')[0] == 'infobox':
                    for j in i.find_all('tr'):
                        try:
                            infocard[j.find('th').text.strip()] = j.find('td').text.strip()
                        
                        except AttributeError:
                            pass
            except TypeError as e:
                if str(e) == "'NoneType' object is not subscriptable":
                    return infocard
        
        return infocard
    
    def headings(self):
        span = self.__content__.find_all('span')
        headings = {}
        for i in span:
            try :
                if str(i.get('class')[0]) == 'mw-headline':
                    data = i.text.strip()
                    headings[data] = i
            
            except TypeError as e:
                if str(e) == "'NoneType' object is not subscriptable":
                    pass
    
    def defination(self):
        return self.__content__.find_all('p')[2].text
        
    def content(self,heading):
        content = str(self.__content__)
        print(content)