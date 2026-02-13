import numpy as np


data = np.loadtxt("numbers.txt")


total_sum = np.sum(data)
mean_value = np.mean(data)


print("Numbers:", data)
print("Sum:", total_sum)
print("Mean:", mean_value)