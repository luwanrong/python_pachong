#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 10:44
# @Author  : JUNE20
# @Site    : 
# @File    : init.py
# @Software: PyCharm
class Rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getPeri(self):
        return (self.x + self.y) * 2
    def getArea(self):
        return self.x * self.y
rect = Rectangle(4,3)#实例化对象时 会制动调用__init__(),并且可以把参数自动传入该方法中
print(rect.getArea())
print(rect.getPeri())