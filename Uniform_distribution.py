# Uniform Distribution

# Used to describe probability where every event has equal chances of occuring

# it has three parameters : a - lower bound(default 0.0)

# b - higher bound(default 1.0), size - The shape of the returned array

# size - The shape of the returned array

# create a 2 * 3 uniform distrubution sample

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

uniform_numbers = np.random.uniform(size=(2, 3))
print(uniform_numbers)
print('--------------------------------------')

uniform_numbers = np.random.uniform(5.0, 10.0, size=(2, 3))
print(uniform_numbers)
print('--------------------------------------')

# Visualization of Uniform distribution

uniform_numbers = np.random.uniform(50, 100, size=1000)

sns.distplot(uniform_numbers, hist=False, label='Uniform')

plt.legend()
plt.show()

print('-----------------------------------')

