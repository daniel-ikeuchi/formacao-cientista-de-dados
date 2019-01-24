# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:11:02 2019

@author: Daniel

Aula 22 - Medidas de Centralidade e Variabilidade
"""

import numpy as np
from scipy import stats

salarios = [40, 18, 12, 250, 30, 140, 40, 800]
salarios.sort()
salarios

np.mean(salarios)
np.median(salarios)

np.quantile(salarios, [0, 0.25, 0.5, 0.75, 1])

stats.describe(salarios)

