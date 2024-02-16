from random_array import generate_random_array
import numpy as np

'''
There are two approaches to using Merge Sort:
1. defining the mergesort function from scratch
2. using np.sort(array, kind='mergesort')
'''

# Algorithm
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


arr = generate_random_array()
print("Original array:", arr)

# np.sort
sorted_arr_np = np.sort(arr, kind='mergesort')
print("Sorted array using np.sort:", sorted_arr_np)

# algorithm
sorted_arr = mergesort(arr)
print("Sorted array using algorithm:", sorted_arr)