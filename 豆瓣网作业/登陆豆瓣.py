#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import requests,time
from bs4 import BeautifulSoup
from selenium import webdriver
session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

data = {
    'source': 'movie',
    'redir': 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=',
    'form_email': '18221212817',
    'form_password': 'liuyang1',
    'login': '登录'
}
log_url = 'https://accounts.douban.com/login'
r1 = session.post(url=log_url, headers=headers, data=data)


url = 'https://www.douban.com/people/186752792/'
r2 = session.get(
    url=url,
    headers=headers
)
with open('2.html','w',encoding='utf-8') as f:
    f.write(r2.text)
r3 = session.get(url='https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action=',
                 headers=headers)

# bro = webdriver.PhantomJS(executable_path='driver/phantomjs-2.1.1-windows/bin/phantomjs')
# bro.get('https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=')
#
#
# js = 'window.scrollTo(0,2000)'
# bro.execute_script(js)
#
# page_text = bro.page_source
# soup = BeautifulSoup(page_text, 'html.parser')
#
# div = soup.find(name='div', attrs={'class': 'movie-list-panel'})
#
# a_list = div.find_all(name='div',attrs={'class':'movie-info'})
#
#
# def get_content(url):
#     res = requests.get(url=url,headers=headers).text
#     soup = BeautifulSoup(res,'html.parser')
#     content = soup.find(name='div',attrs={'id':'content'})
#     title = content.find(name='h1')
#     info = content.find(name='div',attrs={'id':'info'})
#     img_obj = content.find(name='a',attrs={'class':'nbgnbg'})
#     img_url = img_obj.find(name='img').get('src')
#     return title.text,img_url,info.text,
#
#
# f = open('2.json','w',encoding='utf-8')
# for tag in a_list:
#     span_txt = tag.find(name='span',attrs={'class':'movie-name-text'})
#     a_url = span_txt.find('a').get('href')
#     rating_num= tag.find(name='span',attrs={'class':'rating_num'}).text
#     title,img,info = get_content(a_url)
#     print(title,info,img)
#     print(rating_num)
#
#     f.write(title+info+'海报url:'+img+'\n'+'豆瓣评分'+rating_num+'\n\n')
