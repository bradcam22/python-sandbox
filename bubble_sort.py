
def bubble_sort(arr):
    n = len(arr) - 1
    for i in range(n):
        is_sorted = True
        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            break

arr = [9, 3, 6, 1, 15, 2, 8, 2]
print("before", arr)

bubble_sort(arr)
print("after", arr)

