# Use the random.normal() method to get a Normal Data Distribution

# generate a random normal distribution

import numpy as np

x = np.random.normal(100, size=(2, 3))

print(x)
print('----------------------------------')

# Generate a random normal distribution of size 2*3 with mean at 1 and standard deviation of 2:

random_number = np.random.normal(loc=1, scale=2, size=(2, 3))
print(random_number)
print('----------------------------------')

# visualization of Normal Distribution

import matplotlib.pyplot as plt
import seaborn as sns

random_normal_numbers = np.random.normal(loc=1, scale=2, size=(2, 3))
print(random_normal_numbers)
sns.distplot(random_normal_numbers, hist=False)
plt.show()
print('--------------------------------------')

# visualization of Normal Distribution of a bell curve

import matplotlib.pyplot as plt
import seaborn as sns

random_normal_numbers = np.random.normal(size=1000)

sns.distplot(random_normal_numbers, hist=False)
plt.title('Graph 2')
plt.show()

