#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/18 15:55
# @Author  : JUNE20
# @Site    : 
# @File    : class.py
# @Software: PyCharm
class Super():
    name = 'super Man'

    def objFun(self): #对象方法
        print(self)

    def staFun(): #类方法
        print('staFun')
    #绑定方法之“类方法”
    @classmethod
    def clsFun(cls):
        print(cls)
    #非绑定方法之“静态方法”
    @staticmethod
    def staticFun():
        print('staticFun')

obj = Super() #实例化对象
obj.objFun() #对象调用对象方法
# ==> <__main__.Super object at 0x0000000001E84278> 默认传参时当前对象

#类调用对象方法  失败
#Super.objFun()
# ==> Traceback (most recent call last):
#   File "F:/python 学习代码/project_class/class.py", line 28, in <module>
#     Super.objFun()
# TypeError: objFun() missing 1 required positional argument: 'self'

#对象 调用 没有装饰器的类方法
# 失败
try:
    obj.staFun()
except Exception as e:
    print('对象不能调用没有装饰器的类方法')

#类 调用没有装饰器的 类方法
Super.staFun() #成功调用

#对象 调用有装饰器的类方法
obj.clsFun() #调用成功
print('绑定关系：%s' % obj.clsFun)
# ==> <class '__main__.Super'>默认传参还是 类
#绑定关系：<bound method Super.clsFun of <class '__main__.Super'>> 绑定到类方法

#类 调用有装饰器的 类方法
Super.clsFun()
print('绑定关系：%s' % Super.clsFun)
#<class '__main__.Super'>
#绑定关系：<bound method Super.clsFun of <class '__main__.Super'>>

#对象/类 调用有static装饰的 静态方法
obj.staticFun()
print(obj.staticFun)
#staticFun 正常调用
#<function Super.staticFun at 0x00000000024FE048> 当做函数调用 没有绑定关系

Super.staticFun()
print(Super.staticFun)
#staticFun 正常调用
#<function Super.staticFun at 0x00000000024F4048> 无绑定关系，当做函数调用

#总结：。。。
'''
当实例调用classmethod方法时（类方法，绑定，参数cls），默认会把当前实例所对应的类传进去
当类调用classmethod方法时（类方法，绑定，参数cls），默认把此类传进去
对于staticmethod方法（静态方法 ，非绑定，无参数） 实例和类都可调用，没有默认的参数传进，当做 普通函数调用
对于普通方法/对象方法（绑定，带参数）, 当实例调用时，默认将当前实例传进去。（类不可直接调用，需要将对象当实参，这个没意义）
对于类函数（绑定，无参数，无装饰器），只有类能调用，类调用的时候 当做 普通函数调用
静态方法和类方法都是可以通过类对象和类对象实例访问。
静态方法、类方法、普通方法（对象方法）、类函数（普通函数？） 都可以访问 类属性。'''



