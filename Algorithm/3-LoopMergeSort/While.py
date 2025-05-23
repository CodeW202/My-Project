def merge_while(left, right):
    result = []
    i = j = 0

    # Merge using while loops
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements using while loops
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def iterative_merge_sort_while(arr):
    n = len(arr)
    width = 1

    # Use a while loop to iterate over increasing subarray widths
    while width < n:
        i = 0
        # Use a while loop to process subarrays in chunks of 2*width
        while i < n:
            left = arr[i: i + width]
            right = arr[i + width: i + 2 * width]
            merged = merge_while(left, right)
            arr[i: i + 2 * width] = merged
            i += 2 * width
        width *= 2

    return arr

# Example usage:
if __name__ == "__main__":
    arr1 = [5, 1, 8, 2, 9, 3, 7, 4]
    sorted_arr_while = iterative_merge_sort_while(arr1.copy())
    print("Sorted array using while loops:", sorted_arr_while)
