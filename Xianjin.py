#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Lin Lehao 林乐昊 2019-05-09 13:09:23
import time      
start = time.time()
#第一部分:“野人君子”的之分
man = [['粗俗的人','高雅的人'],['平民','卿大夫'],['殷遗民','周人']]

#第二部分:“先进后进”之分
do = [['学习的先后','先学习','后学习'],
    ['做官的先后','先做官','后做官'],
    ['学习儒学的先后','先学习儒学','后学习儒学'],
    ['文明进步和落后','文明进步','文明落后'],
    ['创立礼乐制度的先后','先于创立礼乐','后于创立礼乐']]

#第三部分:“如用之”之别
use = [['选用','人才'],['实用','做法'],['推崇','做法']]

i = 0  #man
j = 0  #do
k = 0  #use
n = 1  #numer
print("以下是组合结果：")
while i < 3 :  
    while j < 5:
        while k < 3:
            print(str(n) + ': ' + do[j][1]+'的'+'，是'+ man[i][0]+'；'
            + do[j][2]+'的'+ '，是' + man[i][1] + '。' + '如果我要'+use[k][0] 
            + use[k][1] + '，我选择' + do[j][1] + '的'+ use[k][1] + '。')
            k += 1
            n += 1
        k = 0
        j += 1
    j = 0   
    i += 1 
print("完成组合！")
end = time.time()
print('组合程序运行时长: %s 秒'%(end-start))
