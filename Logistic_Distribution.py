# Logistic distribution is used to describe growth

# Used extensively in machine learning in logistic regression, neural networks etc

# it has three parameters loc - mean, scale - standard deviation, size - shape of a array

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

logistic_numbers = np.random.logistic(loc=10, scale=2, size=(2, 3))
print(logistic_numbers)
print('------------------------------------------')

# Visualization of Logistic Distribution

logistic_numbers = np.random.logistic(loc=2, scale=2, size=1000)

sns.distplot(logistic_numbers, hist=False, label='Logistic numbers')

plt.legend()
#plt.show()

print('----------------------------------------------')

# Difference between Logistic and normal distribution

normal_numbers = np.random.normal(loc=2, scale=2.0, size=1000)
logistic_numbers = np.random.logistic(loc=2, scale=2, size=1000)

sns.distplot(normal_numbers, hist=False, label='normal')
sns.distplot(logistic_numbers, hist=False, label='Logistic')

plt.legend()
plt.show()
print('-------------------------------------------')

