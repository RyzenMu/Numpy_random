# Multi-Nomial Distribution is a generalization of binomial distribution

# Requires 3 parameters n - no. of possible outcomes (e.g. 6 for dice roll)

# pvals - list of probabilites of outcomes (e.g [1/6, 1/6,1/6,1/6,1/6,1/6] for dice roll

# size - shape of the returned array

# Draw out a sample for dice roll

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

multi_nomial_numbers = np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(multi_nomial_numbers)

print('--------..------------..------------------')
