# -*- coding:utf-8 -*-
import requests


def download_img(url):
    resp = requests.get(url)
    data = resp.content
    with open('i.gif', 'wb') as img:
        img.write(data)

if __name__ == '__main__':
    download_img('https://img.atobo.com/ProductImg/Phone/Big.gif?2TVTeTpzyr2w5QJkDH%2bC8w%3d%3d')

