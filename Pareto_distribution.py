# pareto distribution also called 80-20 distribution
# 20% factors cause 80% outcome

# it has two parameter: a- shape parameter and size - The shape of he returned array

import numpy as np

# Draw out a sample for pareto distribution with shape of 2 with size 2*3:

pareto_numbers = np.random.pareto(a=2, size=(2, 3))

print(pareto_numbers)

print('__________________________________________________')

# Visualization of pareto distribution

import matplotlib.pyplot as plt
import seaborn as sns

pareto_numbers = np.random.pareto(a=2, size=1000)
sns.distplot(pareto_numbers, kde=False)
plt.show()

print('-----------------...--------------------------------')
