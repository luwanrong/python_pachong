#！-*-coding:UTF-8 -*-
#！@Author:JUNE20
print('i love you')
a1 = "{0}{{0}}1{b}".format("555",b = "love")
print(a1)
m="%c%c%c" % (70,105,67) #引号内的%号字符表示最终转化为的格式，中间的%表示进行格式转化操作，后边（）为要转化的参数
print(m)
#序列
list1 = [1,2,3,]
tuple1 = (2,8,5,7,8)
str1 = "love"#长度不一样时以最短的为准
for each in zip(list1,tuple1,str1):
    print(each)