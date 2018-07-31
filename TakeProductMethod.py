#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# 商品的 rows行 cols列 kinds种类
rows = 10
cols = 5
kinds = 9

# 商品
goods = np.round(np.random.rand(rows, cols) * kinds)
print('goods =')
print(goods)


# 购物清单 maxNum单个商品最大数量 classNum商品种类
maxNum = 3
classNum = 3

commodities = {np.random.randint(0, 9):np.random.randint(1, maxNum) for x in range(classNum)}
print('commodities =')
print(commodities)


# 查找存在商品的行
table = np.zeros(goods.shape)
for k, v in commodities.items():
    table[goods == k] = 1
hasRow = [k for k, v in enumerate(np.count_nonzero(table, axis = 1)) if v]
print('hasRow =')
print(hasRow)

# 循环查找最优解
best = []
minRows = 1 << len(hasRow)
combination = 1 << len(hasRow)

for i in range(combination):
    bits=[i>>offset&1 for offset in range(len(hasRow)-1,-1,-1)]
    current = [hasRow[index] for (index,bit) in enumerate(bits) if bit==1]
    # 统计数量
    unique, counts = np.unique(goods[current, :], return_counts=True)
    sets = dict(zip(unique, counts))
    # 检测是否合格
    flag = True
    for key, value in commodities.items():
        if key in sets:
            if commodities[key] > sets[key]:        # 商品不够数
                flag = False
        else:
            flag = False
    if flag and len(current) < minRows:
        best = current
        minRows = len(current)

print('The best choice = ')
print(best)

