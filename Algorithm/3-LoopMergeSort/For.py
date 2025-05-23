def merge_for(left, right):
    result = []
    i = j = 0
    total = len(left) + len(right)
    
    # Use a for loop that runs exactly total times
    for _ in range(total):
        if i < len(left) and (j >= len(right) or left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result

def iterative_merge_sort_for(arr):
    n = len(arr)
    width = 1

    # Use a for loop to process subarrays in chunks of 2*width
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i: i + width]
            right = arr[i + width: i + 2 * width]
            merged = merge_for(left, right)
            arr[i: i + 2 * width] = merged
        width *= 2

    return arr

# Example usage:
if __name__ == "__main__":
    arr2 = [5, 1, 8, 2, 9, 3, 7, 4]
    sorted_arr_for = iterative_merge_sort_for(arr2.copy())
    print("Sorted array using for loops:", sorted_arr_for)
