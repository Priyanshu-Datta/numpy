import numpy as np


arr = np.arange(1, 21)

print("Array:", arr)

even_numbers = arr[arr % 2 == 0]
print("Even Numbers:", even_numbers)

greater_than_10 = arr[arr > 10]
print("Numbers greater than 10:", greater_than_10)
