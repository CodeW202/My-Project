def quick_sort(arr):
    # Base case: A list with 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot (here, we take the last element)
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elements <= pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements > pivot

    # Recursively sort left and right parts, then combine
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
if __name__ == "__main__":
    arr = [5, 1, 8, 2, 9, 3, 7, 4]
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)


