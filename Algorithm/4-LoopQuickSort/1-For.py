def quick_sort_for(arr):
    # Base case: a list with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot (here, the last element)
    pivot = arr[-1]
    left = []
    right = []
    
    # Partition the array using a for loop
    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    # Recursively sort and combine the partitions
    return quick_sort_for(left) + [pivot] + quick_sort_for(right)


# Example usage
if __name__ == "__main__":
    arr = [5, 1, 8, 2, 9, 3, 7, 4]
    sorted_arr = quick_sort_for(arr)
    print("Sorted with for loop partitioning:", sorted_arr)
