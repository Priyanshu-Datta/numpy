import numpy as np

data = np.array([12, 15, 18, 20, 22, 25, 30])


mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
maximum = np.max(data)
minimum = np.min(data)

print("Data:", data)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)
