# -*- coding: utf8 -*-
#grep -rl 'error' /dir/
#第一阶段：找到文件的绝对路径
import os
def init(func):
    def li(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return li



@init
def serect_dir(name):
    while True:
        filepath=yield
        g=os.walk(filepath)
        for fudir,_,files in g:
            for file in files:
                res='%s\%s' %(fudir,file)
                open_file(name).send(res)







#第二阶段：打开文件
@init
def open_file(name):
    while True:
        file=yield
        with open(file,encoding='utf-8') as f:
            cat(name).send((file,f))



#第三阶段：循环读取每一行内容
@init
def cat(name):
    while True:
        file,f=yield
        for line in f:
            #print(line)
            a=grep(name).send((file,line))
            grep(name).send((file,line))
            if a : break





#第四阶段：过滤
@init
def grep(patt):
    tag=False
    while True:
        file,line=yield tag
        tag =False
        if patt in line:
            print(file)
            tag=True
g=serect_dir('26')
g.send('E:\python-lianxi\day3\db1')

#第五阶段：打印该行属于的文件