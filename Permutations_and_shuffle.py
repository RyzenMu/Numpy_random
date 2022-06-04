# Generating permutations and shuffle in numpy

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

np.random.shuffle(arr)

print(arr)

print('---------------------------------')

arr = np.array([1, 2, 3, 4, 5])

np.random.permutation(arr)
print('# permutation leave the original array unchanged')
print(arr) # permutation leave the original array unchanged

print(np.random.permutation(arr))