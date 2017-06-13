#!/usr/bin/env python3
# coding:utf-8

import unittest

import myrequests


class TestMyRequests(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_invald_url(self):
        r = myrequests.get('http://wwwwwwww')
        self.assertEqual(r, None)

    def test_HTTP_200_OK_GET(self):
        r = myrequests.get('http://www.baidu.com')
        self.assertEqual(r.status_code, 200)

    def test_HTTPS_200_OK_GET(self):
        r = myrequests.get('https://www.baidu.com')
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
