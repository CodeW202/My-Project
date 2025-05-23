def merge_sort(arr):
    # Base case: a list with 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])

    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []  # This will store the merged list
    i = j = 0

    # Compare the elements of left and right lists and merge them in order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from left or right (only one of these will have elements)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
if __name__ == "__main__":
    arr = [5, 1, 8, 2, 9, 3, 7, 4]
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
