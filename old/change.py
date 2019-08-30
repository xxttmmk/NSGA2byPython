# -*- coding: utf-8 -*-
# !/usr/bin/env python
import numpy as np


def change_fun(population, belta):
    # new_population = []
    # l=len(population)
    # v=len(population[0])
    # if np.random.rand() <= belta:
    for p in population:
        for j in range(belta):
            u = np.random.rand()
            i = np.random.randint(0, 29)
            if u < 0.5:
                bq = (2 * u) ** (1 / 2) - 1
            else:
                bq = 1 - (2 * (1 - u)) ** (1 / 2)
            # print(p, bq,p[i] + bq)
            if p[i] + bq < 0:
                p[i] = 0
            elif p[i] + bq > 1:
                p[i] = 1
            else:
                p[i] = bq + p[i]
                # p[i] = 3.1
                # print("==", i,p[i])
            # print(bq,p[i])

    """
    for i in population:
        if np.random.rand() <= belta:
            # u = np.random.rand()
            # bq=0
            # if u < 0.5:
            #     bq = (2 * u) ** (1 / 3) - 1
            # else:
            #     bq = 1 - (2 * (1 - u)) ** (1 / 3)
            #
            # c1 = i*bq
            c1=[]
            # print("p",i)

            for j in i:
                u = np.random.rand()
                if u < 0.5:
                    bq = (2 * u) ** (1 / 30) - 1
                else:
                    bq = 1 - (2 * (1 - u)) ** (1 / 30)
                # print("bq",bq)
                if j + bq < 0:
                    c1.append(0)
                elif j + bq > 1:
                    c1.append(1)
                else:
                    c1.append(j + bq)
            # print("c",c1)

            new_population.append(c1)
        # else:
        #     new_population.append(i)
"""
    # if new_population:
    #
    #     new_population = np.array(new_population)
    #     tempopulation = np.vstack((population, new_population))
    # else:
    #     tempopulation=population
    # # tempopulation[tempopulation > 1] = 1
    # # tempopulation[tempopulation < 0] = 0
    return population


if __name__ == "__main__":
    population = np.array([[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]])
    # print(population)

    ###运行函数
    population = change_fun(population, 2)
    print(population)
