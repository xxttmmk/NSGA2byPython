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
import time

gen = 500  # 迭代次数
xN = 200  # 种群数量
yN = 30  # 变量个数
alfa = 0.9
belta = 0.04


pop = np.random.rand(xN * yN).reshape(xN, yN) * 1.0  # 初始化种群

pop_index_layer_f1_f2 = non_domination_sort(pop)
pop_index_layer_distance_sorted = crowding_distance_sort(pop_index_layer_f1_f2)

start=time.time()

for i in range(gen):
    # 二进制锦标赛
    print(i)
    pop_parant = tournament_selection(pop_index_layer_distance_sorted, pop)
    # tour_time=time.time()
    # print("tour_time",tour_time-start)
    # 交叉变异，生成子代
    pop_offspring = cross_mutation(pop_parant, yN,alfa, belta)
    # 子代和上一代合并
    pop = combine(pop, pop_offspring)
    # 非支配排序
    pop_combine_index_layer_f1_f2 = non_domination_sort(pop)
    # 拥挤度排序
    pop_combine_index_layer_distance_sorted = crowding_distance_sort(pop_combine_index_layer_f1_f2)
    # 精英保留产生下一代种群
    pop_index_layer_distance_sorted,pop = elitism(pop_combine_index_layer_distance_sorted, pop,xN)

    pop_index_f1_f2 = []
    if i==gen-1:
        for i in pop_index_layer_distance_sorted:
            index=i[0]
            if i[1]==0:
                pop_index_f1_f2=ZDT1(pop[index])
                print(pop_index_f1_f2[0],pop_index_f1_f2[1])
