# -*- coding: utf-8 -*-
# !/usr/bin/env python
from func import ZDT1


def non_domination_sort(pop):
    pop_index_f1_f2 = {}
    n = len(pop)
    for i in range(n):
        val = ZDT1.ZDT1(pop[i])
        pop_index_f1_f2[i] = val

    pop_index_layer_f1_f2 = control_relationship(pop_index_f1_f2)

    pop_layer_index_f1_f2 = creat_layer(pop_index_layer_f1_f2, pop_index_f1_f2)

    return pop_layer_index_f1_f2


def control_relationship(FuncValueList):
    control_1_dict = {}
    # k0就是pop的索引
    for k0, v0 in FuncValueList.items():
        control_1_dict[k0] = {"支配": [], "被支配": [], "相等": []}
        for k1, v1 in FuncValueList.items():
            if k0 == k1:
                pass
            elif v0[0] < v1[0]:
                control_1_dict[k0]["支配"].append(k1)
            elif v0[0] > v1[0]:
                control_1_dict[k0]["被支配"].append(k1)
            else:
                control_1_dict[k0]["相等"].append(k1)

    control_2_dict = {}

    for k0, v0 in FuncValueList.items():
        control_2_dict[k0] = {"支配": [], "被支配": [], "相等": []}
        for k1, v1 in FuncValueList.items():
            if v0[1] < v1[1]:
                control_2_dict[k0]["支配"].append(k1)
            elif v0[1] > v1[1]:
                control_2_dict[k0]["被支配"].append(k1)
            else:
                if k0 != k1:
                    control_2_dict[k0]["相等"].append(k1)

    control_list = {}
    for index in FuncValueList.keys():
        control_list[index] = {"被支配集合": [], "支配集合": []}
        # set.intersection 交集
        # 强支配关系
        control_list[index]["支配集合"] = set.intersection(set(control_1_dict[index]["支配"]),
                                                       set(control_2_dict[index]["支配"]))
        control_list[index]["被支配集合"] = set.intersection(set(control_1_dict[index]["被支配"]),
                                                        set(control_2_dict[index]["被支配"]))
        # set.union 并集
        # 弱支配关系
        control_list[index]["支配集合"] = set.union(set(control_list[index]["支配集合"]),
                                                set.intersection(set(control_1_dict[index]["支配"]),
                                                                 set(control_2_dict[index]["相等"])),
                                                set.intersection(set(control_1_dict[index]["相等"]),
                                                                 set(control_2_dict[index]["支配"])))
        control_list[index]["被支配集合"] = set.union(set(control_list[index]["被支配集合"]),
                                                 set.intersection(set(control_1_dict[index]["被支配"]),
                                                                  set(control_2_dict[index]["相等"])),
                                                 set.intersection(set(control_1_dict[index]["相等"]),
                                                                  set(control_2_dict[index]["被支配"])))
    for k, v in control_list.items():
        v["被支配集合"] = len(v["被支配集合"])
    return control_list


def creat_layer(control_list, pop_index_f1_f2):
    layer = 0
    control_layer = {}
    while control_list:
        # 某一层的元素
        layer_val = []
        for k in list(control_list.keys()):
            if control_list[k]['被支配集合'] == 0:
                layer_val.append((k, pop_index_f1_f2[k]))
                control_list.pop(k)
            else:
                control_list[k]['被支配集合'] -= 1
        control_layer[layer] = layer_val
        if layer_val:
            layer += 1
    return control_layer
