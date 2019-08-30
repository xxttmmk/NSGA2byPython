# -*- coding: utf-8 -*-
# !/usr/bin/env python
from func import ZDT1
from old import champion, change, control_relationship, control_layer, coss
import numpy as np
#
# random.seed(0)
# np.random.seed(0)

gen = 500 # 迭代次数
xN = 300  # 种群数量
yN = 30 # 变量个数
alfa = 0.8
belta = 12
# tem_population=[]



population = np.random.rand(xN, yN) #初始化种群
# population=np.array([[1]*30 for i in range(5)])
# best=np.array([[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]])
tem_population = coss.coss_fun(population)
print("初始种群",len(population))
# population = np.vstack((population,best))
# for i in population:
#     # print("new_population", i)

for i in range(gen):
    # 计算f1,f2的值[(index,(f1,f2))]
    function_list = []
    function_dict = {}
    population_index = 0
    population_index_list = []
    population_index_dict = {}

    for p in population:
        population_index_dict[population_index] = p
        population_index += 1
    for k, v in population_index_dict.items():
        re = ZDT1.ZDT1(v)
        function_dict[k] = re
        population_index_list.append(k)
        function_list.append((k, re))

    control_list = control_relationship.control_relationship(function_list)
    # print("index_layer_distance", control_list)
    index_layer_distance = control_layer.creat_layer(control_list, population_index_list, function_dict)
    # print("index_layer_distance", index_layer_distance)

    winer = champion.champion_chioce(index_layer_distance, population_index_list)  # 获胜的索引
    print("winer",len(winer))
    new_population = []
    for w in winer:
        # print("添加pop",population[w])
        new_population.append(population[w])

    c=np.random.rand()

    np.random.shuffle(np.array(new_population))
    l=int(0.9*len(new_population))

    coss_population = coss.coss_fun(new_population[:l])

    # print("new_population_coss", len(new_population))
    change_population = change.change_fun(new_population[l:], 1)
    # print("new_population_change", new_population)

    new_population = np.vstack((coss_population, change_population))

    index_layer_distance_list = []
    for k, v in index_layer_distance.items():
        v.append(k)
        # print("56", v)
        index_layer_distance_list.append(v)
        # print("58", index_layer_distance_list)

    # print("index_layer_distance", index_layer_distance)

    l = sorted(index_layer_distance_list, key=lambda x: (x[0], -1*(x[1] + x[2])))
    print(l[-1])
    # print(l[1])
    # print(l)
    tem_population = []
    for x in range(xN):
        tem_population.append(population[l[x][3]])

    # print("new_population", len(new_population))
    # print("tem_population", len(tem_population))

    population = np.vstack((tem_population, new_population))

    print("gen",i)

function_list = []
function_dict = {}
population_index = 0
population_index_list = []
population_index_dict = {}

for p in tem_population:
    population_index_dict[population_index] = p
    population_index += 1
for k, v in population_index_dict.items():
    re = ZDT1.ZDT1(v)
    function_dict[k] = re
    population_index_list.append(k)
    function_list.append((k, re))

control_list = control_relationship.control_relationship(function_list)
index_layer_distance = control_layer.creat_layer(control_list, population_index_list, function_dict)

layer0_index_list=[]
for k,v in index_layer_distance.items():
    if v[0]==0:
        layer0_index_list.append(k)

layer0_pop_list=[]
for layer0 in layer0_index_list:
    layer0_pop_list.append(tem_population[layer0])

re=[]

for res in layer0_pop_list:
    print(ZDT1.ZDT1(res)[0],ZDT1.ZDT1(res)[1])

# print("re",re)







# print(function_list)
# print(control_list)

