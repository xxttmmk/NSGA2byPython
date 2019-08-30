# -*- coding: utf-8 -*-
# !/usr/bin/env python
from collections import OrderedDict


def crowding_distance_sort(pop_layer_index_f1_f2):
    pop_layer_index_distance = {}
    for k, v in pop_layer_index_f1_f2.items():
        pop_index_distance = OrderedDict()
        f1 = sorted(v, key=lambda x: x[1][0])
        f2 = sorted(v, key=lambda x: x[1][1])
        f1_max = f1[-1][1][0]
        f1_min = f1[0][1][0]
        f2_max = f2[-1][1][1]
        f2_min = f2[0][1][1]
        f1_l = len(f1)

        if f1_l == 1:
            pop_index_distance[f1[0][0]] = (float("inf"))
        elif f1_l == 2:
            pop_index_distance[f1[0][0]] = (float("inf"))
            pop_index_distance[f1[1][0]] = (float("inf"))
        else:
            pop_index_distance[f1[0][0]] = (float("inf"))
            pop_index_distance[f1[-1][0]] = (float("inf"))
            for j in range(f1_l - 2):
                if f1_max - f1_min == 0:
                    f1_d = 0
                else:
                    f1_d = (f1[j + 2][1][0] - f1[j][1][0]) / (f1_max - f1_min)
                pop_index_distance[f1[j + 1][0]] = f1_d

            for i in range(f1_l - 2):
                if f2_max - f2_min == 0:
                    f2_d = 0
                else:
                    f2_d = (f2[i + 2][1][1] - f2[i][1][1]) / (f2_max - f2_min)
                pop_index_distance[f1[i + 1][0]] += f2_d

        pop_layer_index_distance[k] = pop_index_distance

    for k in list(pop_layer_index_distance.keys()):
        pop_layer_index_distance[k] = sorted(pop_layer_index_distance[k].items(), key=lambda x: x[1], reverse=True)

    pop_index_layer_distance_sorted = []
    for k, v in pop_layer_index_distance.items():
        for i in v:
            index_distance_layer = [0, 0, 0]
            index_distance_layer[0] = i[0]
            index_distance_layer[1] = k
            index_distance_layer[2] = i[1]
            pop_index_layer_distance_sorted.append(index_distance_layer)

    return pop_index_layer_distance_sorted
