# -*- coding: utf-8 -*-
# !/usr/bin/env python
import random


def tournament_selection(pop_combine_index_layer_distance_sorted, pop):
    # 二元竞赛
    select_pop = []
    n = len(pop_combine_index_layer_distance_sorted)
    while len(select_pop) < n:
        a, b = random.randint(0, n - 1), random.randint(0, n - 1)
        if pop_combine_index_layer_distance_sorted[a][1] < pop_combine_index_layer_distance_sorted[b][1]:
            select_pop.append(pop[pop_combine_index_layer_distance_sorted[a][0]])
        elif pop_combine_index_layer_distance_sorted[a][1] == pop_combine_index_layer_distance_sorted[b][1]:
            if pop_combine_index_layer_distance_sorted[a][2] > pop_combine_index_layer_distance_sorted[b][2]:
                select_pop.append(pop[pop_combine_index_layer_distance_sorted[a][0]])
        else:
            select_pop.append(pop[pop_combine_index_layer_distance_sorted[b][0]])

    return select_pop
