def recursive_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    # Partition the list into elements less than or equal to the pivot and greater than the pivot
    left = [x for x in data[1:] if x <= pivot]
    right = [x for x in data[1:] if x > pivot]
    return recursive_sort(left) + [pivot] + recursive_sort(right)

# Input: Append a new item to Food-Unsort.txt
with open("Food-Unsort.txt", "a") as f:
    food_item = input("Enter a food item to add: ")
    f.write(food_item + "\n")

# Read: Load the data from Food-Unsort.txt
with open("Food-Unsort.txt", "r") as f:
    data = [line.strip() for line in f]

# Attempt to convert data to integers (if possible); otherwise sort as strings.
try:
    data = [int(x) for x in data]
except ValueError:
    pass

# Sort the data using the recursive sort function.
sorted_data = recursive_sort(data)
print(sorted_data)

# Output: Write the sorted data to FoodSort.txt
with open("FoodSort.txt", "w") as f:
    for item in sorted_data:
        f.write(f"{item}\n")
