import numpy


def arrays(arr):
    np_array = numpy.array(arr, float)
    return np_array[::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
