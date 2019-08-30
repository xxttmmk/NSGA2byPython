# -*- coding: utf-8 -*-
# !/usr/bin/env python
def elitism(pop_combine_index_layer_distance_sorted,pop, xN):
    pop_combine_index_layer_distance_sorted = pop_combine_index_layer_distance_sorted[0:xN]
    # print(pop_combine_index_layer_distance_sorted)
    pop_new=[]
    pop_new_index_layer_distance=[]
    for i in range(xN):
        index=pop_combine_index_layer_distance_sorted[i][0]
        layer=pop_combine_index_layer_distance_sorted[i][1]
        distance = pop_combine_index_layer_distance_sorted[i][2]
        pop_new.append(pop[index])

        pop_new_index_layer_distance.append((i,layer,distance))

    return pop_new_index_layer_distance,pop_new
