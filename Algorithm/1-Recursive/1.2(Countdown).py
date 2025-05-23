# Countdown from 5
n = 5

# Recursive
def countdown_recursive(n):
    if n <= 0:
         print("Time's up!")
         return
    print(n)
    countdown_recursive(n - 1)

# Iterative (using a function with a for loop)
def countdown_iterative(n):
    for i in range(n, 0, -1):
         print(i)
    print("Time's up!")

# Both are iterative and efficient

# For
print("For Loop Countdown:")
for i in range(n, 0, -1):
    print(i)
print("Time's up!")

# While
print("\nWhile Loop Countdown:")
i = n
while i > 0:
    print(i)
    i = i - 1
print("Time's up!")

# Optionally, call the functions to see them in action:
print("\nRecursive Countdown:")
countdown_recursive(n)

print("\nIterative Countdown (Function):")
countdown_iterative(n)
