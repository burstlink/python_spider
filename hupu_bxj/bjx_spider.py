#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LeeYY
# datetime:2020/8/14 16:16
# software: PyCharm


import requests
import time
import random
from bs4 import BeautifulSoup as bs


class hupuSpider(object):

    @staticmethod
    def get_pages(page_url):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/84.0.4147.125 Safari/537.36"
        }
        response = requests.get(url=page_url, headers=headers)
        page_soup = bs(response.text, 'lxml')
        return page_soup

    @staticmethod
    def parse_pages(page_soup):
        # soup_html = bs(open('1.html', encoding='utf-8'), features='lxml')
        data_list = []
        all_list = page_soup.find("ul", class_="for-list")
        post_list = all_list.find_all('li')
        for post in post_list:
            # 帖子名称
            post_title = post.find('a', class_='truetit').text
            # print(post_title)
            # 帖子链接
            post_url = 'https://bbs.hupu.com' + post.find('a', class_='truetit')['href']
            # print(post_url)
            # 作者
            author = post.select('.author > a')[0].text
            # print(author)
            # 作者主页
            author_url = post.select('.author > a')[0]['href']
            # print(author_url)
            # 发布日期
            post_date = post.select('.author > a')[1].text
            # print(post_date)
            reply_view = post.find('span', class_='ansour').text
            # 回复数
            post_reply = reply_view.split('/')[0].strip()
            # print(post_reply)
            # 浏览量
            post_view = reply_view.split('/')[1].strip()
            # print(post_view)
            # 最后回复时间
            last_data = post.select('.endreply > a')[0].text
            # print(last_data)
            # 最后回复用户
            last_user = post.select('.endreply > span')[0].text
            # print(last_user)

            data_list.append(
                {"post_title": post_title, "post_url": post_url, "author": author,
                 "author_url": author_url, "post_date": post_date, "post_reply": post_reply,
                 "post_view": post_view, "last_data": last_data, "last_user": last_user})
        return data_list


if __name__ == '__main__':
    hupuSpider.get_pages()