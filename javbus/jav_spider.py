#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LeeYY
# datetime:2020/8/14 18:20
# software: PyCharm

import requests
import time
import random
from bs4 import BeautifulSoup as bs


class JavSpider(object):

    @staticmethod
    def get_pages(page_url):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/84.0.4147.125 Safari/537.36"
        }
        response = requests.get(url=page_url, headers=headers)
        page_soup = bs(response.text, 'lxml')
        return page_soup


if __name__ == '__main__':
    soup_html = bs(open('test.html', encoding='utf-8'), features='lxml')
    data_list = []
    context = soup_html.find("div", id="waterfall")
    movies_list = context.find_all(class_="movie-box")
    for movie in movies_list:
        import pdb;pdb.set_trace()
        # movie_cover = movie.select('.photo-frame > img')[0]["src"]
        movie_title = movie.select('.photo-info > span')[0].text
        # movie_id = movie.select('.photo-info > date')[0].text
        # movie_release_date = movie.select('.photo-info > date')[1].text
        # print(movie_cover)
        print(movie_title)
        # print(movie_id)
        # print(movie_release_date)
        print("===================")