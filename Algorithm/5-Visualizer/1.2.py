import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generate a random array of integers (each representing a bar's height)
N = 60  # number of elements
arr = [random.randint(10, 400) for _ in range(N)]
# We'll use a parallel list to store the "state" of each element:
#   -1: default, 1: currently processed, 2: pivot
states = [-1] * len(arr)

def quicksort(arr, low, high):
    if low < high:
        # Partition the array and yield state changes for visualization
        p, arr = partition(arr, low, high)
        yield arr, states.copy()
        yield from quicksort(arr, low, p - 1)
        yield from quicksort(arr, p + 1, high)
        
def partition(arr, low, high):
    pivot = arr[high]
    states[high] = 2  # mark pivot in state 2 (red)
    i = low
    for j in range(low, high):
        states[j] = 1  # mark current element being processed in state 1 (green)
        yield arr, states.copy()  # yield before comparison\n        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            yield arr, states.copy()  # yield after swap\n            i += 1
        states[j] = -1  # reset state after processing
    # Finally, swap pivot into its correct position
    arr[i], arr[high] = arr[high], arr[i]
    states[high] = -1
    yield arr, states.copy()  # yield after pivot swap
    return i, arr

def generate_states(arr):
    # Run quicksort and yield every intermediate state for visualization
    yield from quicksort(arr, 0, len(arr) - 1)
    yield arr, states.copy()

# Set up the plot
fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(arr)), arr, align="edge", color="blue")
ax.set_xlim(0, N)
ax.set_ylim(0, int(1.1 * max(arr)))
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
iteration = [0]

def update_fig(data):
    a, state = data
    for rect, val, s in zip(bar_rects, a, state):
        rect.set_height(val)
        if s == 2:
            rect.set_color("red")      # pivot element
        elif s == 1:
            rect.set_color("green")    # currently being processed\n        else:
            rect.set_color("blue")     # default color\n    iteration[0] += 1\n    text.set_text(f\"Operations: {iteration[0]}\")\n    return bar_rects\n\nanim = animation.FuncAnimation(fig, update_fig, frames=generate_states(arr.copy()),\n                                  repeat=False, interval=100, blit=False)\nplt.show()\n```\n\n### How It Works:\n\n1. **Data Generation:** The array `arr` is filled with random integers between 10 and 400. Each integer represents the height of a bar.\n\n2. **Quicksort Generator:** The `quicksort` and `partition` functions yield the state of the array and a parallel `states` list at each important step (before/after comparisons and swaps). The `states` list helps us decide which color to display for each bar:\n   - **Red:** Current pivot.\n   - **Green:** Element currently being compared or swapped.\n   - **Blue:** Default (unsorted/processed) elements.\n\n3. **Visualization:** We use matplotlib's `FuncAnimation` to update the bar heights and colors based on each yielded state, creating an animated visualization of the QuickSort process.\n\nFeel free to modify parameters (like `N` for the number of elements or the `interval` for the animation speed) as needed. Let me know if you have any questions or need further adjustments!
