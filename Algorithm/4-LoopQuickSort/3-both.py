def quick_sort_for_while(arr):
    # Work on a copy to avoid modifying the original array
    a = arr.copy()
    # Stack to hold subarray indices (low, high)
    stack = [(0, len(a) - 1)]
    
    # Process the stack until empty using a while loop
    while stack:
        low, high = stack.pop()
        if low < high:
            # Partition the subarray; pivot is chosen as the last element
            pivot = a[high]
            i = low - 1
            # Use a for loop for partitioning
            for j in range(low, high):
                if a[j] <= pivot:
                    i += 1
                    a[i], a[j] = a[j], a[i]
            i += 1
            a[i], a[high] = a[high], a[i]
            pivot_index = i

            # Add subarrays indices to the stack
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    
    return a


# Example usage
if __name__ == "__main__":
    arr = [5, 1, 8, 2, 9, 3, 7, 4]
    sorted_arr = quick_sort_for_while(arr)
    print("Sorted with iterative (while + for) approach:", sorted_arr)
