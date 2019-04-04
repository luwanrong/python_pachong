#！-*-coding:UTF-8 -*-
#！@Author:JUNE20
#任务要求：将record.txt中的内容进行分割并按要求保存:
#1.将小甲鱼的话单独保存，2.将小客服的话单独保存,3.分别保存三段对话
f = open(r'F:\python 学习代码\record.txt')#打开文件
boy = []#创建一个空列表
girl = []
count = 1
for each_line in f:#读每一行
    #print(each_line)
    if each_line[:5] != '=====':#判断前面五个字符是不是‘=====’
        #split函数作用：分割语句根据某些符号
        (role,line_spoken) = each_line.split(':',1)#返回值有两个，:左边和右边的内容
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)
    else:
        file_name_boy = 'boy_'+str(count)+'.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'
        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl, 'w')
        boy_file.writelines(boy)
        girl_file.writelines(girl)
        boy = []
        girl = []
        count += 1
file_name_boy = 'boy_'+str(count)+'.txt'
file_name_girl = 'girl_' + str(count) + '.txt'
boy_file = open(file_name_boy,'w')
girl_file = open(file_name_girl, 'w')
boy_file.writelines(boy)
girl_file.writelines(girl)
boy_file.close()
girl_file.close()
f.close()
import os#导入os模块
os.system('calc')




