#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from aip import AipOcr
import time

#获取验证码
def getCode(imgpath):
    """ 你的 APPID AK SK """
    APP_ID = '14713376'
    API_KEY = 'FUgwKMRxLv0zqkH6G8lOzD2F'
    SECRET_KEY = 'UgYdGQGvTH98sFaoNW8fWBMwQDsTMGVw'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    with open(imgpath, 'rb') as f:
        image = f.read()

    """ 调用通用文字识别（高精度版） """
    code_text = client.basicAccurate(image)

    img_txt = code_text['words_result'][0]['words']

    return img_txt

session = requests.session()

#登陆个人中心
def login(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    }
    url = url
    ret = session.get(url=url, headers=headers).text
    soup = BeautifulSoup(ret, 'html.parser')
    print(soup)
    code_div = soup.select('.item-captcha')
    print(code_div)
    if code_div in soup:
        img_url = soup.find(name='img', attrs={'id': 'captcha_image'}).get('src')
        captcha_id = soup.find(name='input', attrs={'name': 'captcha-id'}).get('value')

        img = requests.get(url=img_url, headers=headers)

        with open('1.jpg', 'wb') as f:
            f.write(img.content)

        code = getCode('1.jpg')

        data = {
            'source': 'movie',
            'redir': 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action=',
            'form_email': '18221212817',
            'form_password': 'liuyang1',
            'captcha-solution': code,
            'captcha-id': captcha_id,
            'login': '登录'
        }
        response = session.post(url='https://accounts.douban.com/login', data=data, headers=headers, )
    else:
        data = {
            'source': 'movie',
            'redir': 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action=',
            'form_email': '18221212817',
            'form_password': 'liuyang1',
            'login': '登录'
        }
        response = session.post(url='https://accounts.douban.com/login', data=data, headers=headers, )

    get_movie(response)

# 获取电影详情
def get_movie(response):
    bro = webdriver.PhantomJS(executable_path='driver/phantomjs-2.1.1-windows/bin/phantomjs')
    bro.get('https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=')
    js = 'window.scrollTo(2000,document.body.scrollHeight)'
    time.sleep(3)
    bro.execute_script(js)
    time.sleep(10)
    page_text = bro.page_source
    soup = BeautifulSoup(page_text, 'html.parser')

    div = soup.find(name='div', attrs={'class': 'movie-list-panel'})

    a_list = div.find_all(name='div', attrs={'class': 'movie-info'})
    f = open('2.json', 'w', encoding='utf-8')
    for tag in a_list:
        span_txt = tag.find(name='span', attrs={'class': 'movie-name-text'})
        a_url = span_txt.find('a').get('href')
        rating_num = tag.find(name='span', attrs={'class': 'rating_num'}).text
        title, img, info = get_content(a_url)
        print(title, info, img)
        print(rating_num)
        f.write(title + info + '海报url:' + img + '\n' + '豆瓣评分' + rating_num + '\n\n')

#解析电影详情里的URL拿到电影详情
def get_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    }
    res = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(res, 'html.parser')
    content = soup.find(name='div', attrs={'id': 'content'})
    title = content.find(name='h1')
    info = content.find(name='div', attrs={'id': 'info'})
    img_obj = content.find(name='a', attrs={'class': 'nbgnbg'})
    img_url = img_obj.find(name='img').get('src')
    return title.text, img_url, info.text,


login('https://www.douban.com/accounts/login?source=movie')
