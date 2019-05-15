#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Lin Lehao 林乐昊 2019-05-10 19:33:40
import time      

#第一部分:“野人君子”的之分
man = []

#第二部分:“先进后进”之分
do = []

#第三部分:“如用之”之别
use = []

#输入
a = 0
while True:
    z1 = input("请输入“粗人”的解释"+ str(a+1) +"(请输入名词，例如“粗俗的人”，“平民”，若不再输入，请输入”ok“): ")
    z1.replace(" ", "")
    if z1 == 'ok':
        break
    elif (isinstance(z1, str) == False) or (z1 == ""):
        print("格式错误，请重新输入。")
        continue
    else:
        while True:
            z2 = input("请输入相应“君子”的解释"+ str(a+1) +"(请输入名词，例如“高雅的人”，“卿大夫”): ")
            z2.replace(" ", "")
            if (isinstance(z2, str) == False) or (z2 == ""):
                print("格式错误，请重新输入。")
                continue
            else:
                man.append([z1, z2])
                print("已输入“野人君子”的解释" + str(a+1) +": "+ man[a][0] +", "+ man[a][1])
                a += 1 
                break

b = 0
while True:
    z3 = input("请输入“先进”的解释"+ str(b+1) +"(请输入类似如下的搭配，例如“先学习”，“先做官”，若不再输入，请输入”ok“): ")
    z3.replace(" ", "")
    if z3 == 'ok':
        break
    elif (isinstance(z3, str) == False) or (z3 == ""):  
        print("格式错误，请重新输入。")
        continue
    else:
        while True:
            z4 = input("请输入相应“后进”的解释"+ str(b+1) +"(请输入类似如下的搭配，例如“后学习”，“后做官”): ")
            z4.replace(" ", "")
            if (isinstance(z4, str) == False) or (z4 == ""):
                print("格式错误，请重新输入。")
                continue
            else:
                do.append([z3, z4])
                print("已输入“先进后进”的解释" + str(b+1) +": "+ do[b][0] +", "+ do[b][1])
                b += 1 
                break

c = 0
while True:
    print("以下输入”如用之“的搭配，分为”用“和”之“，分别输入相应的动词和名词。")
    z5 = input("请输入“如用之”的”用“解释"+ str(c+1) +"(请输入类似如下动词，例如“选用”，“推崇”，若不再输入，请输入”ok“): ")
    z5.replace(" ", "")
    if z5 == 'ok':
        break
    elif (isinstance(z5, str) == False) or (z5 == ""):
        print("格式错误，请重新输入。")
        continue
    else:
        while True:
            z6 = input("请输入和前面搭配的”如用之“的”之“解释"+ str(c+1) +"(请输入类似如下名词，例如“人才”，“做法”): ")
            z6.replace(" ","")
            if (isinstance(z6, str) == False) or (z6 == ""):
                print("格式错误，请重新输入。")
                continue
            else:
                use.append([z5, z6])
                print("已输入“如用之”的解释" + str(c+1) +": "+ use[c][0] +", "+ use[c][1])
                c += 1 
                break

#组合部分
a = len(man)
b = len(do)
c = len(use)

start = time.time()
print("--------------------------------------------------------------------------")
print("组合开始！")
i = 0  #man
j = 0  #do
k = 0  #use
n = 1  #numer
print("以下是组合结果：")
while i < a :  
    while j < b:
        while k < c:
            print(str(n) + ': ' + do[j][0]+'的'+'，是'+ man[i][0]+'；'
            + do[j][1]+'的'+ '，是' + man[i][0] + '。' + '如果我要'+use[k][0] 
            + use[k][1] + '，我选择' + do[j][0] + '的'+ use[k][1] + '。')
            k += 1
            n += 1
        k = 0
        j += 1
    j = 0   
    i += 1 
print("完成组合！")
end = time.time()
print('组合程序运行时长: %s 秒'%(end-start))
