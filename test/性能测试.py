#!/usr/bin/env python3
# coding:utf-8

'''requests 和 myrequests 性能测试'''

import requests

import myrequests
from finished import finished # 我写的一个打印函数运行时间的小库


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}


@finished
def test_myrequests1(url):

    for n in range(100):
        r = myrequests.get(url)
        #print(r.request.headers)


@finished
def test_myrequests2(url):

    for n in range(100):
        r = myrequests.get(url, headers=headers)
        #print(r.request.headers)


@finished
def test_myrequests3(url):

    with myrequests.Session() as session:
        for n in range(100):
            r = session.get(url)
            #print(r.request.headers)


@finished
def test_requests1(url):

    for n in range(100):
        r = requests.get(url, headers=headers)


@finished
def test_requests2(url):

    for n in range(100):
        r = requests.get(url, headers=headers, timeout=3)
        

@finished
def test_requests3(url):
    
    with requests.Session() as session:
        for n in range(100):
            r = session.get(url, headers=headers)


def main():
    url = 'https://www.baidu.com'
    test_myrequests1(url)
    test_myrequests2(url)
    test_myrequests3(url)
    test_requests1(url)
    test_requests2(url)
    test_requests3(url)


if __name__ == '__main__':
    main()