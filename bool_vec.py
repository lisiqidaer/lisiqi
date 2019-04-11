# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:16:19 2019

@author: 50635
"""

import numpy as np
#形成的r数组中有N个数值
N=int(input('请输入一个大额整数'))
r=np.random.random(N)
print(r)
#把小于等于0.5的数从r中挑出来并打印
print(r[r<=0.5])
#打印出数量
print(len(r[r<=0.5]))

#将数字进行转化
r[r<=0.5]=0
r[r>0.5]=1
print(r)

