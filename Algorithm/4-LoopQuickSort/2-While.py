def quick_sort_while(arr):
    # Base case: a list with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot (using the last element)
    pivot = arr[-1]
    left = []
    right = []
    
    # Partition the array using a while loop
    i = 0
    while i < len(arr) - 1:
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
        i += 1

    # Recursively sort and combine the partitions
    return quick_sort_while(left) + [pivot] + quick_sort_while(right)


# Example usage
if __name__ == "__main__":
    arr = [5, 1, 8, 2, 9, 3, 7, 4]
    sorted_arr = quick_sort_while(arr)
    print("Sorted with while loop partitioning:", sorted_arr)
