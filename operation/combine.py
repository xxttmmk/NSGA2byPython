# -*- coding: utf-8 -*-
#!/usr/bin/env python
import numpy as np
def combine(pop,pop_offspring):
    pop_offspring=np.array(pop_offspring)

    pop_combine= np.vstack((pop, pop_offspring))

    return pop_combine
