#!/usr/bin/env python3
# coding:utf-8

from setuptools import setup


setup(
    name='myrequests', 
    version='1.0', 
    description='This is my requests',
    author='zzzzer', 
    author_email='zzzzer91@gmail.com',
    url='https://github.com/zzzzer91/myrequests',
    packages=['myrequests'], 
    install_requires=[
        'requests>=2.10.0',
    ],
    zip_safe=False,
)
