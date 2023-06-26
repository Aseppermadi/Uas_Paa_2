import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
        if i < 5 or i >= n-5:
            print(f"Iteration {i+1}: {arr}")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print("\n*** Bubble Sort ***")
    print("Before Sorting:", arr)
    print("After Sorting:", arr)
    print("Elapsed Time:", elapsed_time, "seconds")
    
def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
        if i < 5 or i >= n-5:
            print(f"Iteration {i+1}: {arr}")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print("\n*** Insertion Sort ***")
    print("Before Sorting:", arr)
    print("After Sorting:", arr)
    print("Elapsed Time:", elapsed_time, "seconds")

# Main program
data = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
        26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
        17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
        40, 7, 41, 81]

print("Before Sorting:", data)

choice = input("Enter sorting algorithm (bubble/insertion): ")

if choice.lower() == "bubble":
    bubble_sort(data.copy())
elif choice.lower() == "insertion":
    insertion_sort(data.copy())
else:
    print("Invalid choice. Please choose either 'bubble' or 'insertion'.")
