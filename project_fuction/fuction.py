#！-*-coding:UTF-8 -*-
#！@Author:JUNE20
def exchangeRate(dollar):
   """美元汇率为6.5"""
   return dollar * 6.5
y = exchangeRate(10)
print(y)
help(exchangeRate)#查看 函数文档
def hello():
   print("你好!")
hello()#调用函数
m = hello()
print(m)
def Fun1(x):
   def Fun2(y):
      return x*y
   return Fun2
i = Fun1(8)
j=i(4)
print(j)
#匿名函数lambda
g = lambda x,y : 2*x + 3*y + 3
c = g(2,3)
print(c)
#filter过滤器
def odd(x):
   return x%2
temp1 = filter(odd,range(10))
a=list(temp1)
print(a)

#汉诺塔
def hanoi(n,x,y,z):
   if n==1:#只有一层
      print(x,'-->',z)
   else:
      hanoi(n-1,x,z,y)
      print(x,'-->',z)
      hanoi(n-1,y,x,z)
n = int(input('请输入层数：'))
hanoi(n,'X','Y','Z')

