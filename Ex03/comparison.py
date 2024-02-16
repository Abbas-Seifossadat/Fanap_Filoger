from random_array import generate_random_array
from time import perf_counter
import numpy as np

arr = generate_random_array()

start_quicksort = perf_counter()
quicksorted_array = np.sort(arr, kind='quicksort')
end_quicksort = perf_counter()

start_heapsort = perf_counter()
heapsorted_array = np.sort(arr, kind='heapsort')
end_heapsort = perf_counter()

start_mergesort = perf_counter()
mergesorted_array = np.sort(arr, kind='mergesort')
end_mergesort = perf_counter()

print(#'Sorted array in quicksort:\n', quicksorted_array,
      f'Quick Sort Time: {(end_quicksort - start_quicksort):.3f} seconds')

print(#'Sorted array in heapsort:\n', heapsorted_array,
      f'Heap Sort Time: {(end_heapsort - start_heapsort):.3f} seconds')

print(#'Sorted array in mergesort:\n', mergesorted_array,
      f'Merge Sort Time: {(end_mergesort - start_mergesort):.3f} seconds')