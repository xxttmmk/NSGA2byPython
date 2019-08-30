# -*- coding: utf-8 -*-
# !/usr/bin/env python
import numpy as np

def coss_fun(population):
    # np.random.shuffle(population)
    # print("shuffle",population)
    l = len(population)
    v = len(population[0])
    new_population = []

    # if l % 2 == 0:
    p1_p2=[]
    for i in range(l // 2):
        p1_p2.append(list(np.random.choice(l,2)))
    # else:
    #     for i in range(l // 2):
    #         p1_p2.append([2 * i, 2 * i + 1])
    #     p1_p2.append([-1, -2])
    # print(p1_p2[0])
    # p1_p2=list(set(p1_p2))

    for i in p1_p2:
        # print("i",i[0],i[1])
        bqs=[]
        for j in range(v):
            u = np.random.rand()
            if u < 0.5:
                bq = (2 * u) ** (1 / 2)
            else:
                bq = (2 * (1 - u)) ** (1 / 2)
            bqs.append(bq)
        bqs=np.array(bqs)
        p1 = population[i[0]]
        p2 = population[i[1]]
        if (p1 == p2).all():
            pass
            # print(p1)
            # print(p2)
        else:
            # c3= bqs
            # print(c3)
            c1 = 0.5 * ((1 + bqs) * p1 + (1 - bqs) * p2)
            c2 = 0.5 * ((1 + bqs) * p2 + (1 - bqs) * p1)
            # print("p1",p1)
            # print("p2", p2)
            # print("c1",c1)
            # print("c2",c2)
            new_population.append(c1)
            new_population.append(c2)

        '''
        u = np.random.rand()
        if u < 0.5:
            bq = (2 * u) ** (1 / 2)
        else:
            bq = (2 * (1 - u)) ** (1 / 2)
        p1 = population[i[0]]
        p2 = population[i[1]]
        # print("p1", p1, bq)
        # print("p2", p2, bq)
        if (p1==p2).all():
            print(p1)
            print(p2)
        else:
            c1 = 0.5 * ((1 + bq) * p1 + (1 - bq) * p2)
            c2 = 0.5 * ((1 + bq) * p2 + (1 - bq) * p1)
            new_population.append(c1)
            new_population.append(c2)
    '''
    new_population=np.array(new_population)
    new_population[new_population > 1] = 1
    new_population[new_population < 0] = 0

    # if len(new_population)>len(population):
    #     new_population.pop(-1)

    # population=np.vstack((population,new_population))

    return new_population

if __name__=="__main__":
    population=np.array([[0,0,0,0],[1,1,1,1],[2,2,2,2]])
    # print(population)

    ###运行函数
    population=coss_fun(population)
    print(population)
