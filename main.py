import csv
import os
import random
import time

# Algoritmo de Ordenação: Selection Sort
def selection_sort(arr):
    comparisons = 0  # Contador de comparações
    swaps = 0  # Contador de trocas
    n = len(arr)
    
    # Percorre cada elemento do array
    for i in range(n):
        min_idx = i
        # Encontra o menor elemento na parte não ordenada do array
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Troca o menor elemento com o elemento atual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    return comparisons, swaps


# Algoritmo de Ordenação: Insertion Sort
def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    
    # Percorre cada elemento do array a partir do segundo elemento
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move os elementos maiores que a chave para a direita
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        # Insere a chave na posição correta
        arr[j + 1] = key
    return comparisons, swaps


# Algoritmo de Ordenação: Quick Sort
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
        if low < high:
            pi = partition(arr, low, high)
            quicksort_helper(arr, low, pi - 1)
            quicksort_helper(arr, pi + 1, high)
    
    n = len(arr)
    quicksort_helper(arr, 0, n - 1)
    return comparisons, swaps


# Algoritmo de Ordenação: Merge Sort
def mergesort(arr):
    comparisons = 0
    swaps = 0
    
    def merge(arr, left, mid, right):
        nonlocal comparisons, swaps
        n1 = mid - left + 1
        n2 = right - mid
        L = arr[left:mid+1]
        R = arr[mid+1:right+1]
        
        i = 0
        j = 0
        k = left
        while i < n1 and j < n2:
            comparisons += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                swaps += 1
                i += 1
            else:
                arr[k] = R[j]
                swaps += 1
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            swaps += 1
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            swaps += 1
            j += 1
            k += 1

    def mergesort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            mergesort_helper(arr, left, mid)
            mergesort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)

    n = len(arr)
    mergesort_helper(arr, 0, n - 1)
    return comparisons, swaps


# Algoritmo de Ordenação: Heap Sort
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
            arr[i], arr[largest] = arr[largest], arr[i]
            swaps += 1
            heapify(arr, n, largest)

    def heapsort_helper(arr):
        nonlocal comparisons, swaps
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            swaps += 1
            heapify(arr, i, 0)

    heapsort_helper(arr)
    return comparisons, swaps


# Algoritmo de Ordenação: Shell Sort
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


# Gera uma lista aleatória de tamanho n
def generate_random_list(n):
    return [random.randint(1, 1000) for _ in range(n)]


def write_to_csv(results):
    with open('results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Tamanho da entrada", "Comparisons (Bubble Sort)", "Swaps (Bubble Sort)", "Time (Bubble Sort)",
                         "Comparisons (Insertion Sort)", "Swaps (Insertion Sort)", "Time (Insertion Sort)",
                         "Comparisons (Selection Sort)", "Swaps (Selection Sort)", "Time (Selection Sort)",
                         "Comparisons (Quick Sort)", "Swaps (Quick Sort)", "Time (Quick Sort)",
                         "Comparisons (Merge Sort)", "Swaps (Merge Sort)", "Time (Merge Sort)",
                         "Comparisons (Heap Sort)", "Swaps (Heap Sort)", "Time (Heap Sort)",
                         "Comparisons (Shell Sort)", "Swaps (Shell Sort)", "Time (Shell Sort)"])

        for row in results:
            size = row[0]
            comparisons = row[1]
            swaps = row[2]
            times = row[3]

            writer.writerow([size] +
                            comparisons[0:1] + [swaps[0]] + [times[0]] +
                            comparisons[1:2] + [swaps[1]] + [times[1]] +
                            comparisons[2:3] + [swaps[2]] + [times[2]] +
                            comparisons[3:4] + [swaps[3]] + [times[3]] +
                            comparisons[4:5] + [swaps[4]] + [times[4]] +
                            comparisons[5:6] + [swaps[5]] + [times[5]] +
                            comparisons[6:7] + [swaps[6]] + [times[6]])



def run_simulations():
    sizes = [10, 100, 1000]
    num_simulations = 30
    results = []

    for size in sizes:
        total_comparisons = [0] * size
        total_swaps = [0] * size
        total_time = [0] * size

        for _ in range(num_simulations):
            arr = generate_random_list(size)

            algorithms = [
                (selection_sort, "Selection Sort"),
                (insertion_sort, "Insertion Sort"),
                (quicksort, "Quick Sort"),
                (mergesort, "Merge Sort"),
                (heapsort, "Heap Sort"),
                (shellsort, "Shell Sort")
            ]

            for algorithm, algorithm_name in algorithms:
                start_time = time.time()
                comparisons, swaps = algorithm(arr.copy())
                end_time = time.time()
                total_comparisons[size - 1] += comparisons
                total_swaps[size - 1] += swaps
                total_time[size - 1] += end_time - start_time

        average_comparisons = [count / num_simulations for count in total_comparisons]
        average_swaps = [count / num_simulations for count in total_swaps]
        average_time = [t / num_simulations for t in total_time]

        result_row = [size, average_comparisons, average_swaps, average_time]
        results.append(result_row)

    if os.path.exists('results.csv'):
    # Exclui o arquivo
        os.remove('results.csv')

    write_to_csv(results)


run_simulations()
