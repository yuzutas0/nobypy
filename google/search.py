# -*- coding: utf-8 -*-

import requests, bs4, time, random, re


class Search:

    @staticmethod
    def get_sentence(keyword):
        searched = requests.get('https://www.google.co.jp/search?q=' + keyword)
        time.sleep(1)
        soup_searched = bs4.BeautifulSoup(searched.text, "html.parser")
        
        sites = soup_searched.select('.r a')
        site = random.choice(sites)
        url = site.get('href').split('q=')[1].split('&')[0]

        res = requests.get(url)
        time.sleep(1)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        p = soup.select('p')

        words = []
        num = random.choice(range(len(p)))
        items = re.split('[？?！!\n\s。\.「」]', p[num].getText())
        for item in items:
            if len(item) > 3:
                words.append(item)
        return random.choice(words)
