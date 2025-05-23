def merge(left, right):
    result = []  # This will store the merged list
    i = j = 0

    # Use a while loop to compare elements of left and right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from left or right
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def iterative_merge_sort(arr):
    n = len(arr)
    width = 1  # initial size of sublists to merge

    # Continue increasing the width until it exceeds the list length
    while width < n:
        # For loop to iterate over the array in chunks of 2*width
        for i in range(0, n, 2 * width):
            left = arr[i: i + width]
            right = arr[i + width: i + 2 * width]
            # Merge the two sublists and replace that section in the original array
            arr[i: i + 2 * width] = merge(left, right)
        width *= 2  # Increase the width for the next iteration
    return arr

# Example usage
if __name__ == "__main__":
    arr = [5, 1, 8, 2, 9, 3, 7, 4]
    sorted_arr = iterative_merge_sort(arr)
    print("Sorted array:", sorted_arr)

'''
In the provided iterative merge sort:
The while loop inside the merge function is responsible for the actual merging of two sorted sublists. It compares elements from each sublist and builds a new sorted list.
The for loop in the iterative_merge_sort function is used to iterate over the entire array in chunks, selecting pairs of sublists to merge with the merge function.
So, while both loops are part of the overall process, the merging itself is done by the while loop, and the for loop organizes which sublists to merge.
'''