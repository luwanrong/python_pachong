#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 15:09
# @Author  : JUNE20
# @Site    : 
# @File    : Exercise.py
# @Software: PyCharm
def c2f(cel):
    fah = cel * 1.8 + 32
    return fah
def f2c(fah):
    cel = (fah - 32)/1.8
    return cel
def text():
    print('测试，0摄氏度 = %.2f华氏度' % c2f(0))
    print('测试，0华氏度 = %.2f摄氏度' % f2c(0))
if __name__ == '__main__':
    text()
import sys
print(sys.path)