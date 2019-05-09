#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

_URL_ = "https://www.youtube.com/results?search_query="

class Youtube:
    def Search(self,word):
        if " " in word:
            word.replace(" ","+")
        page = requests.get(_URL_ + word)
        soup = BeautifulSoup(page.text, 'html.parser')
        vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
        videoList = {}
        for v in vids:
            videoList[v['title']] = 'https://www.youtube.com' + v['href']

        return videoList
