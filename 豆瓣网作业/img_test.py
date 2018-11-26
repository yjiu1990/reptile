#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '14713376'
API_KEY = 'FUgwKMRxLv0zqkH6G8lOzD2F'
SECRET_KEY = 'UgYdGQGvTH98sFaoNW8fWBMwQDsTMGVw'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('1.png')

""" 调用通用文字识别（高精度版） """
client.basicAccurate(image)

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（高精度版） """
r = client.basicAccurate(image, options)
print(r)
print(r['words_result'][0]['words'])




