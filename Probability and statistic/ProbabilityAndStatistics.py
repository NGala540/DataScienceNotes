import numpy as np

'''
ex.1 
Create numpy array with values 1 to 9, show it and then reverse the table
'''
# a1 = np.arange(1,10)
# print(a1)
# a1 = np.flip(a1)
# print(a1)

'''
ex. 2
Create numpay array [1, 23, 4, 31, 1, 1, 4, 23, 4, 1] and print unique values
'''
# a2 = np.array([1, 23, 4, 31, 1, 1, 4, 23, 4, 1])
# a2 = np.unique(a2)
# print(a2)

'''
ex. 3
Create 3x3 matrix using reshape with values from 2 to 10
'''
# a3 = np.arange(2,11).reshape(3, 3)
# print(a3)

'''
ex. 4
Create table with 6 random values from 10 to 30
'''
# a4 = np.random.randint(10, 30, 6)
# print(a4)

'''
ex. 5
From array of numbers: [23, 45, 112, 150, 43, 254, 95, 8]  
filter those higher than 100
'''
# a5 = np.array([23, 45, 112, 150, 43, 254, 95, 8])
# a5 = a5[a5 > 100]
# print(a5)

'''
ex 6
Create given matrix 4x4: 
[1, 15, 4, 13][8, 21, 3, 12][11, 13, 11, 5][32, 13, 0, 2]
- show its element from second row and third column
- calculate its determinant
- calculate its trace
- find largest and smallest element'''

# A1 = np.array([[1, 15, 4, 13],[8, 21, 3, 12],[11, 13, 11, 5],[32, 13, 0, 2]])
# print(A1[1,2])
# A1_det = np.linalg.det(A1)
# print(A1_det)
# A1_tr = np.trace(A1)
# print(A1_tr)
# A1_max = np.max(A1)
# A1_min = np.min(A1)
# print(f"max: {A1_max}, min: {A1_min}")

'''
ex. 7
Create an array and calculate mean and median
'''
# a7 = np.random.normal(size=10)
# print(np.mean(a7))
# print(np.median(a7))

'''
ex. 8
Create an array and normalize it substarct mean and divide by standard dividation
'''
# a8 = np.random.random(10)
# print(a8)
# print(np.mean(a8))
# print(np.std(a8))
# a8_normal = (a8 - np.mean(a8))/np.std(a8)
# print(a8_normal)

'''
ex. 9
Create function that takes two vectors 
and returns euclidean distance between them
'''
# def calculate_euclidean_distance(v1: np.ndarray, v2: np.ndarray):
#     return np.sqrt(np.sum((v1 - v2)**2))
#
# v1 = np.array([2,0])
# v2 = np.array([0,1])
#
# print(calculate_euclidean_distance(v1,v2))

'''
ex. 10
Using Shapiro-Wilk test check if given sample have a normal distribution
[0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]. 
'''
import scipy.stats as sps

sample = np.array([0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869])
results = sps.shapiro(sample)
print(results)
