# -*- coding: utf-8 -*-
# !/usr/bin/env python

def control_relationship(FuncValueList):
    #输入 FuncValueList[(index,[f1,f2])]
    #输出{index: {'被支配集合': 0, '支配集合': []}}
    func1 = sorted(FuncValueList, key=lambda x: x[1][0])
    func2 = sorted(FuncValueList, key=lambda x: x[1][1])
    control_1_dict = {}
    for i in FuncValueList:
        index = i[0]
        control_1_dict[index] = {"支配": [], "被支配": [], "相等": []}
        for j in func1:
            if i[1][0] < j[1][0]:
                control_1_dict[index]["支配"].append(j[0])
            elif i[1][0] > j[1][0]:
                control_1_dict[index]["被支配"].append(j[0])
            else:
                if index != j[0]:
                    control_1_dict[i[0]]["相等"].append(j[0])

    control_2_dict = {}

    for i in FuncValueList:
        index = i[0]
        control_2_dict[index] = {"支配": [], "被支配": [], "相等": []}
        for j in func2:
            if i[1][1] < j[1][1]:
                control_2_dict[index]["支配"].append(j[0])
            elif i[1][1] > j[1][1]:
                control_2_dict[index]["被支配"].append(j[0])
            else:
                if index != j[0]:
                    control_2_dict[index]["相等"].append(j[0])

    control_list = {}
    for i in FuncValueList:
        index = i[0]
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
    for k,v in control_list.items():
        # print("key", k, len(v["被支配集合"]))
        v["被支配集合"]=len(v["被支配集合"])
    return control_list


