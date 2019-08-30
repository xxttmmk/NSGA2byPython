# -*- coding: utf-8 -*-
# !/usr/bin/env python
import random
import numpy as np
import math

def champion_chioce(index_layer_distance, population_index_list):
    population_index_list=np.array(population_index_list)
    l = int(math.ceil(len(population_index_list) / 2))

    winer = []
    for i in range(l):
        tem = np.random.choice(population_index_list, 2, replace=True)
        a = index_layer_distance[tem[0]]
        b = index_layer_distance[tem[1]]
        if a[0] < b[0]:
            winer.append(tem[0])
        elif a[0] > b[0]:
            winer.append(tem[1])
        elif a[1] + a[2] >= b[1] + b[2]:
            winer.append(tem[0])
        else:
            winer.append(tem[1])

    return winer
