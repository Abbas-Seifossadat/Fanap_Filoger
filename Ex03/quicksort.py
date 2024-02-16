from random_array import generate_random_array
import numpy as np

'''
There are two approaches to using Quick Sort:
1. defining the quicksort function from scratch
2. using np.sort(array, kind='quicksort')
'''

# Algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = np.random.choice(arr)
    left = arr[arr < pivot]
    middle = arr[arr == pivot]
    right = arr[arr > pivot]
    return np.concatenate((quicksort(left), middle, quicksort(right)))


arr = generate_random_array()
print("Original array:", arr)

# with np.sort
sorted_arr_np = np.sort(arr, kind='quicksort')
print("Sorted array using np.sort:", sorted_arr_np)

# with algorithm
sorted_arr = quicksort(arr)
print("Sorted array using algorithm:", sorted_arr)