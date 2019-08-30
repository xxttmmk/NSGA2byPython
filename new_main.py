# -*- coding: utf-8 -*-
# !/usr/bin/env python

from operation.non_domination_sort import non_domination_sort
from operation.crowding_distance_sort import crowding_distance_sort
from operation.elitism import elitism
from operation.tournament_selection import tournament_selection
from operation.cross_mutation import cross_mutation
from operation.combine import combine
import numpy as np
from func.ZDT1 import ZDT1
import matplotlib.pyplot as plt
import zdt1_val

val=np.array(zdt1_val.data)

gen = 500 # 迭代次数
xN = 200  # 种群数量
yN = 30  # 变量个数
alfa = 0.9
belta = 0.04

pop = np.random.rand(xN * yN).reshape(xN, yN) * 1.0  # 初始化种群

pop_index_layer_f1_f2 = non_domination_sort(pop)
pop_index_layer_distance_sorted = crowding_distance_sort(pop_index_layer_f1_f2)

pop_index_f1_f2 = []

for i in range(gen):
    if i%10==0:
        print("第{}代".format(i))
    # 二进制锦标赛
    pop_parant = tournament_selection(pop_index_layer_distance_sorted, pop)
    # tour_time=time.time()
    # print("tour_time",tour_time-start)
    # 交叉变异，生成子代
    pop_offspring = cross_mutation(pop_parant, yN, alfa, belta)
    # 子代和上一代合并
    pop = combine(pop, pop_offspring)
    # 非支配排序
    pop_combine_index_layer_f1_f2 = non_domination_sort(pop)
    # 拥挤度排序
    pop_combine_index_layer_distance_sorted = crowding_distance_sort(pop_combine_index_layer_f1_f2)
    # 精英保留产生下一代种群
    pop_index_layer_distance_sorted, pop = elitism(pop_combine_index_layer_distance_sorted, pop, xN)

    #最后一代，输出最前沿结果集
    if i == gen - 1:
        print("第{}代".format(i))
        for i in pop_index_layer_distance_sorted:
            index = i[0]
            if i[1] == 0:
                pop_index_f1_f2.append(ZDT1(pop[index]))

pop_index_f1_f2 = np.array(pop_index_f1_f2)

x = pop_index_f1_f2[:, 0]
y = pop_index_f1_f2[:, 1]
x1 = val[:, 0]
y1 = val[:, 1]
plt.figure(figsize=(7, 4))  # 创建一幅图，长宽7,4英寸，可创建多副图，也可以用plt.subplot创建多副子图
plt.plot(x, y, 'ro')  # 点状图
plt.plot(x1, y1,'ro',c='b')  # 点状图
plt.grid(True)  # 显示网格
plt.axis('tight')  # 紧凑坐标轴，查阅坐标轴选项，既plt.axis()参数
plt.xlabel("X轴索引")
plt.ylabel("y轴")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title("标题能吃吗")

plt.show()
