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
            j -= 1
        # Insere a chave na posição correta
        arr[j + 1] = key
        swaps += 1
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
                
                j -= gap
            arr[j] = temp
            swaps += 1
        gap //= 2

    return comparisons, swaps


# Gera uma lista aleatória de tamanho n
def generate_random_list(n):
    population = list(range(100000, 1000000))
    random.shuffle(population)
    return population[:n]


def calculate_averages(metrics):
    averages = {}
    for algorithm_name, algorithm_metrics in metrics.items():
        algorithm_averages = {}
        for metric_name, metric_values in algorithm_metrics.items():
            average = sum(metric_values) / len(metric_values)
            algorithm_averages[metric_name] = average
        averages[algorithm_name] = algorithm_averages
    return averages

def write_to_csv(results):
    with open('results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Tamanho da entrada",
                         "Comparisons (Selection Sort)", "Swaps (Selection Sort)", "Time (Selection Sort)",
                         "Comparisons (Insertion Sort)", "Swaps (Insertion Sort)", "Time (Insertion Sort)",
                         "Comparisons (Quick Sort)", "Swaps (Quick Sort)", "Time (Quick Sort)",
                         "Comparisons (Merge Sort)", "Swaps (Merge Sort)", "Time (Merge Sort)",
                         "Comparisons (Heap Sort)", "Swaps (Heap Sort)", "Time (Heap Sort)",
                         "Comparisons (Shell Sort)", "Swaps (Shell Sort)", "Time (Shell Sort)"])

        for row in results:
            size = row[0]
            metrics = row[1]

            averages = calculate_averages(metrics)

            writer.writerow([size] +
                            [str(averages['Selection Sort']['Comparisons'])] + [str(averages['Selection Sort']['Swaps'])] + [str(averages['Selection Sort']['Time'])] +
                            [str(averages['Insertion Sort']['Comparisons'])] + [str(averages['Insertion Sort']['Swaps'])] + [str(averages['Insertion Sort']['Time'])] +
                            [str(averages['Quick Sort']['Comparisons'])] + [str(averages['Quick Sort']['Swaps'])] + [str(averages['Quick Sort']['Time'])] +
                            [str(averages['Merge Sort']['Comparisons'])] + [str(averages['Merge Sort']['Swaps'])] + [str(averages['Merge Sort']['Time'])] +
                            [str(averages['Heap Sort']['Comparisons'])] + [str(averages['Heap Sort']['Swaps'])] + [str(averages['Heap Sort']['Time'])] +
                            [str(averages['Shell Sort']['Comparisons'])] + [str(averages['Shell Sort']['Swaps'])] + [str(averages['Shell Sort']['Time'])])

def run_simulations():
    sizes = [1000,5000,10000]
    num_simulations = 30
    results = []

    for size in sizes:
        metrics = {
            'Selection Sort': {'Comparisons': [], 'Swaps': [], 'Time': []},
            'Insertion Sort': {'Comparisons': [], 'Swaps': [], 'Time': []},
            'Quick Sort': {'Comparisons': [], 'Swaps': [], 'Time': []},
            'Merge Sort': {'Comparisons': [], 'Swaps': [], 'Time': []},
            'Heap Sort': {'Comparisons': [], 'Swaps': [], 'Time': []},
            'Shell Sort': {'Comparisons': [], 'Swaps': [], 'Time': []}
        }

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
                metrics[algorithm_name]['Comparisons'].append(comparisons)
                metrics[algorithm_name]['Swaps'].append(swaps)
                metrics[algorithm_name]['Time'].append(end_time - start_time)

        result_row = [size, metrics]
        results.append(result_row)

    if os.path.exists('results.csv'):
        os.remove('results.csv')

    write_to_csv(results)


run_simulations()
