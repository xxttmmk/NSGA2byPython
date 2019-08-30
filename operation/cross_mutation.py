# -*- coding: utf-8 -*-
# !/usr/bin/env python
import random
import numpy as np


def cross_mutation(pop_parant, yN, alfa, belta):
    n = len(pop_parant)
    pop_offspring = []

    while len(pop_offspring) <= n:
        a, b = random.randint(0, n - 1), random.randint(0, n - 1)
        p1, p2 = pop_parant[a], pop_parant[b]
        if (p1 == p2).all():
            pass
        # 交叉
        elif random.random() < alfa:
            pop_bq = []
            for i in range(int(yN)):
                u = random.random()
                if u < 0.5:
                    bq = (2 * u) ** (1 / 3)
                else:
                    bq = (1/(2 * (1 - u))) ** (1 / 3)
                pop_bq.append(bq)
            pop_bq = np.array(pop_bq)
            c1 = 0.5 * ((1 + pop_bq) * p1 + (1 - pop_bq) * p2)
            c2 = 0.5 * ((1 + pop_bq) * p2 + (1 - pop_bq) * p1)
            c1[c1 > 1] = 1
            c2[c2 > 1] = 1
            c1[c1 < 0] = 0
            c2[c2 < 0] = 0
            pop_offspring.append(c1)
            pop_offspring.append(c2)
        # 变异
        elif random.random() > 1 - belta:
            c1 = p1[:]
            c2 = p2[:]
            for j in range(yN):
                u = np.random.rand()
                if u < 0.5:
                    bq = (2 * u) ** (1 / 6) - 1
                else:
                    bq = 1 - (2 * (1 - u)) ** (1 / 6)
                if c1[j] + bq < 0:
                    c1[j] = 0
                elif c1[j] + bq > 1:
                    c1[j] = 1
                else:
                    c1[j] = bq + c1[j]

            for j in range(yN):
                u = np.random.rand()
                if u < 0.5:
                    bq = (2 * u) ** (1 / 2) - 1
                else:
                    bq = 1 - (2 * (1 - u)) ** (1 / 2)
                if c2[j] + bq < 0:
                    c2[j] = 0
                elif c2[j] + bq > 1:
                    c2[j] = 1
                else:
                    c2[j] = bq + c2[j]
            pop_offspring.append(c1)
            pop_offspring.append(c2)

    return pop_offspring
