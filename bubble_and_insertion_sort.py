import time
import random

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end_time = time.time()
    return arr, end_time - start_time

def selection_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    end_time = time.time()
    return arr, end_time - start_time

def print_iteration_results(arr, algorithm_name):
    print(f"--- {algorithm_name} ---")
    print("5 Iterasi Pertama:")
    for i in range(min(5, len(arr))):
        print(arr[i], end=" ")
    print()
    print("5 Iterasi Terakhir:")
    for i in range(max(0, len(arr) - 5), len(arr)):
        print(arr[i], end=" ")
    print()

def print_execution_time(execution_time):
    print("Waktu Eksekusi: {:.6f} detik".format(execution_time))

def print_before_after(arr, algorithm_name):
    print(f"\n--- {algorithm_name} ---")
    print("Sebelum pengurutan:")
    print(arr)
    sorted_arr, execution_time = algorithm(arr.copy())
    print("Setelah pengurutan:")
    print(sorted_arr)
    print_execution_time(execution_time)

# Array yang akan diurutkan
arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
       26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
       17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
       40, 7, 41, 81]

# Mengacak urutan array
random.shuffle(arr)

# Pilihan pengguna
print("Pilihan pengurutan:")
print("1. Bubble Sort")
print("2. Selection Sort")
choice = input("Masukkan pilihan (1/2): ")

if choice == '1':
    algorithm = bubble_sort
    algorithm_name = "Bubble Sort"
elif choice == '2':
    algorithm = selection_sort
    algorithm_name = "Selection Sort"
else:
    print("Pilihan tidak valid.")
    exit()

# Menampilkan sebelum dan sesudah pengurutan
print_before_after(arr, algorithm_name)

# Menampilkan iterasi pertama dan terakhir
sorted_arr, execution_time = algorithm(arr.copy())
print_iteration_results(sorted_arr, algorithm_name)

# Menampilkan waktu komputasi pengurutan
print_execution_time(execution_time)

