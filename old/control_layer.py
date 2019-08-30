# -*- coding: utf-8 -*-
# !/usr/bin/env python

def creat_layer(control_list, population_index_list, function_dict):
    # index:基因索引
    # 输入population_index_list[index]
    # 输入control_list,{index: {'被支配集合': 0, '支配集合': []}}
    # 输出control_layer{index:[(层号,距离1,距离2)]}
    control_layer = {}
    control_layer = control_layer.fromkeys(population_index_list)
    layer_index = {}

    layer = 0
    while control_list:
        # print("层数", layer)
        temp = []
        for k in list(control_list.keys()):  # print(k, v)
            # print("==============")

            if control_list[k]['被支配集合'] == 0:
                # print("key",k,control_list[k]['被支配集合'])
                control_layer[k] = [layer]
                temp.append(k)
                # print(k, control_layer[k])
                control_list.pop(k)
            else:
                control_list[k]['被支配集合'] -= 1
        if temp:
            layer_index[layer] = temp
            layer += 1

    # 按层迭代，k是层
    for k in list(layer_index.keys()):
        f1_layer = sorted(layer_index[k], key=lambda x: (function_dict[x][0], -1 * function_dict[x][1]))
        f2_layer = sorted(layer_index[k], key=lambda x: (function_dict[x][1], -1 * function_dict[x][0]))
        # print("f1_layer",f1_layer)
        # print("f2_layer", f2_layer)
        f1_max = function_dict[max(f1_layer, key=lambda x: function_dict[x][0])][0]
        f1_min = function_dict[min(f1_layer, key=lambda x: function_dict[x][0])][0]
        f2_max = function_dict[max(f2_layer, key=lambda x: function_dict[x][1])][1]
        f2_min = function_dict[min(f2_layer, key=lambda x: function_dict[x][1])][1]
        # print("f2_max",f2_max)

        if f1_layer and len(f1_layer) == 1:
            control_layer[f1_layer[0]].append(float("inf"))
            control_layer[f1_layer[0]].append(float("inf"))
            # control_layer[f1_layer[-1]].append(float("inf"))
        else:
            control_layer[f1_layer[0]].append(float("inf"))
            control_layer[f1_layer[-1]].append(float("inf"))
            control_layer[f2_layer[0]].append(float("inf"))
            control_layer[f2_layer[-1]].append(float("inf"))

        if f1_layer and len(f1_layer) > 2:
            for i in range(len(f1_layer) - 2):
                if f1_max - f1_min == 0:
                    f1_d = float("inf")
                    control_layer[f1_layer[i + 1]].append(f1_d)
                else:
                    f1_d = (function_dict[f1_layer[i + 2]][0] - function_dict[f1_layer[i]][0]) / (f1_max - f1_min)
                    control_layer[f1_layer[i + 1]].append(f1_d)

        if f2_layer and len(f2_layer) > 2:

            for i in range(len(f2_layer) - 2):
                if f2_max - f2_min == 0:
                    f2_d = float("inf")
                    control_layer[f2_layer[i + 1]].append(f2_d)
                else:
                    f2_d = (function_dict[f2_layer[i + 2]][1] - function_dict[f2_layer[i]][1]) / (f2_max - f2_min)
                    control_layer[f2_layer[i + 1]].append(f2_d)

    return control_layer
