def quick_sort(data, low, high):
    if low < high:
        # Choose pivot (last element is common, can be modified)
        pivot = data[high]

        # Partitioning: elements < pivot to left, > pivot to right
        i = low - 1
        for j in range(low, high):
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]

        # Place pivot in its final position
        data[i + 1], data[high] = data[high], data[i + 1]

        # Recursively sort subarrays
        quick_sort(data, low, i)
        quick_sort(data, i + 2, high)  # Adjust for 1-based indexing

# Input
############Write#####################
# Open the file in append mode ("a")
with open("Food-Unsort.txt", "a") as f:
    # Get user input
    food_item = input("Enter a food item to add: ")
    # Write the input to the file, followed by a newline
    f.write(food_item + "\n")
############Write#####################

# Output
############Read#####################
# Read data from Food-Unsort.txt (assuming simple line-based structure)
with open("Food-Unsort.txt", "r") as f:
    data = [line.strip() for line in f]  # Remove leading/trailing whitespace

# Convert data to integers if necessary (assuming numerical sorting)
try:
    data = [int(x) for x in data]
except ValueError:
    pass  # Handle non-numerical data (sorting strings remains)

# Sort the data (modify low and high based on your data structure)
quick_sort(data, 0, len(data) - 1)

# Print the sorted data
print(data)
############Read#####################

############Instruction1#####################
'''
    Open the input file in read only mode.
    Read the contents into a list.
    Sort the list using quicksort.
'''

############Instruction2#####################
'''
    Open the output file in write mode.
    Write out the sorted list.
'''

#Terminal
'''
python "ReadWrite.py" Food-Unsort.txt FoodSort.txt
'''

#Food-Unsort.txt
'''
apple
Tree
banana
'''

#FoodSort.txt
'''
    Open the output file in write mode.
    Write out the sorted list.
'''
# Print the sorted data and write it to "FoodSort.txt"
with open("FoodSort.txt", "w") as f:  # Open in write mode to overwrite
    for item in data:
        f.write(f"{item}\n")  # Write each item with a newline
