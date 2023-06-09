import csv
import random
import time
import numpy as np

def selection_sort(arr):
    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
                swaps += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        

    return comparisons, swaps

def insertion_sort(arr):
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
        

    return comparisons, swaps

def quicksort(arr):
    comparisons = 0
    swaps = 0

    def partition(arr, low, high):
        nonlocal comparisons, swaps
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def quicksort_helper(arr, low, high):
        nonlocal comparisons, swaps
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort_helper(arr, low, pivot_index - 1)
            quicksort_helper(arr, pivot_index + 1, high)

    quicksort_helper(arr, 0, len(arr) - 1)
    return comparisons, swaps

def mergesort(arr):
    comparisons = 0
    swaps = 0

    def merge(arr, left, middle, right):
        nonlocal comparisons, swaps
        left_arr = arr[left:middle+1]
        right_arr = arr[middle+1:right+1]

        i = j = 0
        k = left

        while i < len(left_arr) and j < len(right_arr):
            comparisons += 1
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            swaps += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    def mergesort_helper(arr, left, right):
        nonlocal comparisons, swaps
        if left < right:
            middle = (left + right) // 2
            mergesort_helper(arr, left, middle)
            mergesort_helper(arr, middle + 1, right)
            merge(arr, left, middle, right)

    mergesort_helper(arr, 0, len(arr) - 1)
    return comparisons, swaps

def heapsort(arr):
    comparisons = 0
    swaps = 0

    def heapify(arr, n, i):
        nonlocal comparisons, swaps
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            comparisons += 1
            largest = left

        if right < n and arr[largest] < arr[right]:
            comparisons += 1
            largest = right

        if largest != i:
            swaps += 1
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def heapsort_helper(arr):
        nonlocal comparisons, swaps
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            swaps += 1
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

    heapsort_helper(arr)
    return comparisons, swaps

def shellsort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                swaps += 1
                j -= gap
            arr[j] = temp

        gap //= 2

    return comparisons, swaps

def generate_random_array(size):
    return np.random.randint(1, 60000, size)

def run_sorting_algorithm(algorithm, array):
    start_time = time.time()
    comparisons, swaps = algorithm(array.copy())
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000

    return comparisons, swaps, execution_time

def measure_sorting_algorithm(algorithm_name, algorithm, sizes, num_simulations):
    results = []

    for size in sizes:
        print("Current size:", size)
        comparisons_list = []
        swaps_list = []
        execution_times = []

        for _ in range(num_simulations):
            array = generate_random_array(size)
            comparisons, swaps, execution_time = run_sorting_algorithm(algorithm, array)
            comparisons_list.append(comparisons)
            swaps_list.append(swaps)
            execution_times.append(execution_time)

        max_comparisons = max(comparisons_list)
        min_comparisons = min(comparisons_list)
        avg_comparisons = sum(comparisons_list) / num_simulations

        max_swaps = max(swaps_list)
        min_swaps = min(swaps_list)
        avg_swaps = sum(swaps_list) / num_simulations

        max_execution_time = max(execution_times)
        min_execution_time = min(execution_times)
        avg_execution_time = sum(execution_times) / num_simulations

        result = {
            'Algorithm': algorithm_name,
            'Size': size,
            'Max Comparisons': max_comparisons,
            'Min Comparisons': min_comparisons,
            'Avg Comparisons': avg_comparisons,
            'Max Swaps': max_swaps,
            'Min Swaps': min_swaps,
            'Avg Swaps': avg_swaps,
            'Max Execution Time': max_execution_time,
            'Min Execution Time': min_execution_time,
            'Avg Execution Time': avg_execution_time
        }

        results.append(result)

    return results

def save_results_to_csv(results, file_path):
    keys = results[0].keys()

    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

def main():
    sizes = [100, 1000, 5000, 10000, 25000, 30000, 35000, 40000, 45000, 50000]  # Tamanhos de entrada
    num_simulations = 30  # Número de simulações para cada tamanho de entrada

    algorithms = {
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Quicksort': quicksort,
        'Mergesort': mergesort,
        'Heapsort': heapsort,
        'Shellsort': shellsort
    }

    selected_algorithms = ['Selection Sort']  # Escolha os algoritmos que deseja testar

    results = []

    for algorithm_name, algorithm_func in algorithms.items():
        if algorithm_name in selected_algorithms:
            algorithm_results = measure_sorting_algorithm(algorithm_name, algorithm_func, sizes, num_simulations)
            results.extend(algorithm_results)

    save_results_to_csv(results, 'sorting_results.csv')
    print('Os resultados foram salvos no arquivo sorting_results.csv.')

if __name__ == '__main__':
    main()
