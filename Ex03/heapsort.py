from random_array import generate_random_array
import numpy as np

'''
There are two approaches to using Heap Sort:
1. defining the heapsort function from scratch
2. using np.sort(array, kind='heapsort')
'''
# Algorithm
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)


arr = generate_random_array()
print("Original array:", arr)

# with np.sort
sorted_arr_np = np.sort(arr, kind='heapsort')
print("Sorted array using np.sort:", sorted_arr_np)

# with algorithm
heapsort(arr)
print("Sorted array using algorithm:", arr)