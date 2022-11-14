#! /usr/bin/python
# -*- coding: UTF-8 -*-


x = "20";
print (x);

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print (list)               # 输出完整列表
print (list[0])            # 输出列表的第一个元素
print (list[1:3] )         # 输出第二个至第三个的元素 
print (list[2:]  )         # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2 )      # 输出列表两次
print (list + tinylist)    # 打印组合的列表

print ("-----------------")

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print (tuple)               # 输出完整元组
print (tuple[0] )           # 输出元组的第一个元素
print (tuple[1:3])          # 输出第二个至第三个的元素 
print (tuple[2:]  )         # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2 )      # 输出元组两次
print (tuple + tinytuple)   # 打印组合的元组

flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print ('welcome boss')    # 并输出欢迎信息
else:
    print (name)            # 条件不成立时输出变量名称


var1 = "return"

while   var1 == "return ok":
    print ("-------is ok-------")
print ("-----is not ok--------")


for letter in 'Python':     # 第一个实例
   print ('当前字母 :', letter)
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print ('当前水果 :', fruit)
 
print ("Good bye!")

var1 = 'Hello World!'
var2 = "Python Runoob"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])


import time;  # 引入time模块

ticks = time.time()
print ("当前时间戳为:", ticks)

import time

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) )
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


import calendar

cal = calendar.month(2017, 7)
print ("以下输出2017年7月份的日历:")
print (cal);